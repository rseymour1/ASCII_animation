import argparse
from PIL import Image
import numpy as np

def image_to_ascii(image_path, output_path, width=25, height=7):
    """
    Convert an image to ASCII art using characters based on their shapes rather than just density.
    Optimized for small output dimensions.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path for the output text file
        width (int): Width of the ASCII art in characters
        height (int): Height of the ASCII art in characters
    """
    # Characters selected for their shapes, not just density
    # / and \ for diagonals, | and - for lines, () for curves, etc.
    shape_chars = {
        'vertical': '|',
        'horizontal': '-',
        'diagonal1': '/',
        'diagonal2': '\\',
        'corner1': '┌',
        'corner2': '┐',
        'corner3': '└',
        'corner4': '┘',
        'curve1': '(',
        'curve2': ')',
        'dot': '.',
        'solid': '#',
        'empty': ' '
    }
    
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Resize the image to target dimensions
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Convert image to numpy array for easier manipulation
    img_array = np.array(img)
    
    # Calculate edge detection using simple gradient
    edges_x = np.zeros_like(img_array, dtype=float)
    edges_y = np.zeros_like(img_array, dtype=float)
    
    # Simple horizontal and vertical gradient for edge detection
    edges_x[:, 1:-1] = img_array[:, 2:] - img_array[:, :-2]
    edges_y[1:-1, :] = img_array[2:, :] - img_array[:-2, :]
    
    # Calculate gradient magnitude and direction
    gradient_magnitude = np.sqrt(edges_x**2 + edges_y**2)
    gradient_direction = np.arctan2(edges_y, edges_x)
    
    # Function to select character based on gradient properties
    def select_char(magnitude, direction, intensity):
        if magnitude < 30:  # Not an edge
            if intensity < 85:  # Dark region
                return shape_chars['solid']
            elif intensity < 170:  # Medium region
                return shape_chars['dot']
            else:  # Light region
                return shape_chars['empty']
        else:  # Is an edge
            # Convert radians to degrees and normalize to 0-180
            angle = (np.degrees(direction) + 180) % 180
            
            if 22.5 <= angle < 67.5:  # Diagonal /
                return shape_chars['diagonal1']
            elif 112.5 <= angle < 157.5:  # Diagonal \
                return shape_chars['diagonal2']
            elif 67.5 <= angle < 112.5:  # Horizontal
                return shape_chars['horizontal']
            else:  # Vertical
                return shape_chars['vertical']
    
    # Generate ASCII art based on image features
    ascii_image = []
    for y in range(height):
        row = []
        for x in range(width):
            char = select_char(
                gradient_magnitude[y, x],
                gradient_direction[y, x],
                img_array[y, x]
            )
            row.append(char)
        ascii_image.append(''.join(row))
    
    # Join the rows and write to file
    with open(output_path, 'w') as f:
        f.write('\n'.join(ascii_image))
    
    print(f"Shape-based ASCII art created and saved to {output_path}")
    print(f"Dimensions: {width}x{height} characters")

def main():
    parser = argparse.ArgumentParser(description='Convert PNG images to shape-based ASCII art')
    parser.add_argument('image_path', help='Path to the input PNG image')
    parser.add_argument('output_path', help='Path for the output text file')
    parser.add_argument('--width', type=int, default=25, help='Width of ASCII art in characters (default: 25)')
    parser.add_argument('--height', type=int, default=7, help='Height of ASCII art in characters (default: 7)')
    
    args = parser.parse_args()
    
    image_to_ascii(args.image_path, args.output_path, args.width, args.height)

if __name__ == "__main__":
    main()