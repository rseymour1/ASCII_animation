# Ensure necessary packages are installed
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

# Check if CUDA is available and set device accordingly
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the CLIP model and tokenizer
model, preprocess = open_clip.create_model_from_pretrained('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')

# Move model to the selected device and set to evaluation mode
model.to(device)
model.eval()

# Set model parameters to not require gradients for inference
for param in model.parameters():
    param.requires_grad = False

def clip_loss(generated_images, labels, true_label_index):
    """
    Compute a loss based on the CLIP model.
    
    Args:
        generated_images (Tensor): A batch of images (shape: [batch_size, C, H, W])
            already preprocessed and on `device`.
        labels (list of str): Candidate text labels.
        true_label_index (int or Tensor): The index of the correct label.
        
    Returns:
        loss (Tensor): A scalar loss computed via cross entropy.
    """
    # Tokenize and encode the text directly on the same device as the model
    text_tokens = tokenizer(labels).to(device)
    
    with torch.no_grad():
        # Encode text on the same device as the model
        text_features = model.encode_text(text_tokens)
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)
        
        # Encode the generated images
        image_features = model.encode_image(generated_images)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    
    # Compute the similarity logits
    logits = 100.0 * image_features @ text_features.T  # Shape: [batch_size, num_labels]
    
    # Optional: Print softmax probabilities
    probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    
    # Prepare the true labels tensor
    true_label_tensor = torch.tensor([true_label_index], device=device, dtype=torch.long)
    
    # Compute cross-entropy loss
    loss = F.cross_entropy(logits, true_label_tensor)
    
    return loss#, probs

if __name__ == "__main__":
    # Load and preprocess image
    image = Image.open("./Data/Image/castle_710.png")
    
    # Move image tensor to the selected device
    image_tensor = preprocess(image).unsqueeze(0).to(device, dtype=torch.float32)
    
    # Example labels and true label index
    candidate_labels = ["a bird", "a dog", "a cat", "a castle"]
    true_label = 3
    
    # Compute loss and probabilities
    loss, probs = clip_loss_cuda(image_tensor, candidate_labels, true_label)
    
    # Print results
    print(f"Loss: {loss.item()}")
    print("Label probabilities:")
    for i, label in enumerate(candidate_labels):
        print(f"  {label}: {probs[0][i].item():.4f}")