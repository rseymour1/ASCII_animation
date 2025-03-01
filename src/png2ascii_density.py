import argparse
from PIL import Image

def image_to_ascii(image_path, output_path, width=100, height=None):
    """
    Convert an image to ASCII art using a wide range of ASCII characters and save it to a text file.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path for the output text file
        width (int): Width of the ASCII art in characters
        height (int): Height of the ASCII art in characters (optional)
    """
    # Comprehensive ASCII characters from darkest to lightest
    # Characters arranged roughly by visual density
    ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate new dimensions while maintaining aspect ratio
    original_width, original_height = img.size
    if height is None:
        # Calculate height to maintain aspect ratio
        aspect_ratio = original_height / original_width
        height = int(width * aspect_ratio * 0.5)  # * 0.5 to account for character height/width ratio
    
    # Resize the image
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Convert pixels to ASCII characters
    pixels = list(img.getdata())
    ascii_image = []
    for i in range(0, len(pixels), width):
        # Get a row of pixels
        row = pixels[i:i+width]
        # Map each pixel to an ASCII character
        ascii_row = ''.join([ascii_chars[min(int(pixel * len(ascii_chars) / 256), len(ascii_chars) - 1)] for pixel in row])
        ascii_image.append(ascii_row)
    
    # Join the rows and write to file
    with open(output_path, 'w') as f:
        f.write('\n'.join(ascii_image))
    
    print(f"ASCII art created and saved to {output_path}")
    print(f"Character set used: {ascii_chars}")

def main():
    parser = argparse.ArgumentParser(description='Convert PNG images to ASCII art')
    parser.add_argument('image_path', help='Path to the input PNG image')
    parser.add_argument('output_path', help='Path for the output text file')
    parser.add_argument('--width', type=int, default=100, help='Width of ASCII art in characters (default: 100)')
    parser.add_argument('--height', type=int, default=None, help='Height of ASCII art in characters (maintains aspect ratio if not specified)')
    
    args = parser.parse_args()
    
    image_to_ascii(args.image_path, args.output_path, args.width, args.height)

if __name__ == "__main__":
    main()