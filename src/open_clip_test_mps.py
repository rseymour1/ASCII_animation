# Ensure necessary packages are installed
from clip2loss import create_loss_function
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
'''
try:
    install_package("open_clip_torch")
    install_package("torch")
    install_package("torchvision")
    install_package("Pillow")
    install_package("requests")
except subprocess.CalledProcessError:
    pass
'''
import open_clip
import torch
from PIL import Image
import torch.nn.functional as F
#import requests


# Check if MPS (Metal Performance Shaders) is available
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
cpu_device = torch.device("cpu")  # Keep text processing on CPU
print(f"Using device for image: {device}")
print(f"Using device for text: {cpu_device}")

# Load the CLIP model and tokenizer (frozen feature extractor)
model, preprocess = open_clip.create_model_from_pretrained('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')
model.eval()  # Freeze the model; you can also set requires_grad=False for parameters if needed.
model.to(cpu_device)




def clip_loss(generated_images, labels, true_label_index):
    """
    Compute a loss based on the CLIP model.

    Args:
        generated_images (Tensor): A batch of images (shape: [batch_size, C, H, W])
                                   already preprocessed and on `device` (MPS).
        labels (list of str): Candidate text labels.
        true_label_index (int or Tensor): The index of the correct label.

    Returns:
        loss (Tensor): A scalar loss computed via cross entropy.
    """
    # Tokenize and encode the text on the CPU to avoid MPS issues
    text_tokens = tokenizer(labels).to(cpu_device)  # Keep text on CPU
    model.to(cpu_device)

    with torch.no_grad():
        text_features = model.encode_text(text_tokens)  # Runs on CPU
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    # Move text features to MPS for similarity calculations
    text_features = text_features.to(device)
    model.to(device)

    # Encode the generated images (which are already on MPS)
    image_features = model.encode_image(generated_images)
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)

    # Compute the similarity logits
    logits = 100.0 * image_features @ text_features.T  # Shape: [batch_size, num_labels]
    print((100.0 * image_features @ text_features.T).softmax(dim=-1))

    # Prepare the true labels tensor
    true_label_tensor = torch.tensor([true_label_index], device=device, dtype=torch.long)

    # Compute cross-entropy loss
    loss = F.cross_entropy(logits, true_label_tensor)
    return loss


if __name__ == "__main__":
    # Load and preprocess image
    #url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
    #image = Image.open(requests.get(url, stream=True).raw)
    image = Image.open("./Data/Image/castle_710.png")
    image_tensor = preprocess(image).unsqueeze(0).to(device, dtype=torch.float32)

    # Example labels and true label index.
    candidate_labels = ["a bird", "a dog", "a cat", "a castle"]
    true_label = 3

    print("Label probs:", clip_loss(image_tensor, candidate_labels, true_label))  # Move results to CPU for printing
