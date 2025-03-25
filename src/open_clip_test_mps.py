# Ensure necessary packages are installed
from clip2loss import create_loss_function
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    install_package("open_clip_torch")
    install_package("torch")
    install_package("torchvision")
    install_package("Pillow")
    install_package("requests")
except subprocess.CalledProcessError:
    pass

import open_clip
import torch
from PIL import Image
import requests
def run_open_clip(image_path: str, label_list: list):
    # Check if MPS (Metal Performance Shaders) is available
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    cpu_device = torch.device("cpu")  # Keep text processing on CPU
    print(f"Using device for image: {device}")
    print(f"Using device for text: {cpu_device}")

    # Load the model and tokenizer
    model, preprocess = open_clip.create_model_from_pretrained('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')
    tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')

    # Move model to MPS (Apple GPU)
    model.to(device)

    # Load and preprocess image
    url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
    image = Image.open(requests.get(url, stream=True).raw)
    image = preprocess(image).unsqueeze(0).to(device, dtype=torch.float32)

    # Tokenize text (keep on CPU)
    text = tokenizer(label_list).to(cpu_device)

    # Compute features
    with torch.no_grad():
        # Image encoding on MPS
        image_features = model.encode_image(image)

        # Temporarily move model to CPU for text encoding
        model.to(cpu_device)
        text_features = model.encode_text(text)

        # Move features back to MPS for computation
        image_features = image_features.to(device)
        text_features = text_features.to(device)

        # Normalize features
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        # Compute similarity
        text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    return text_probs.cpu().numpy()

print("Label probs:", run_open_clip("", ["a diagram", "a dog", "a cat"]))  # Move results to CPU for printing
