import argparse
from PIL import Image
import numpy as np
from scipy import ndimage

def image_to_ascii(image_path, output_path, width=25, height=7, contrast_factor=1.5):
    """
    Convert an image to ASCII art optimized for small dimensions using
    enhanced image processing techniques.
    
    Args:
        image_path (str): Path to the input image
        output_path (str): Path for the output text file
        width (int): Width of the ASCII art in characters
        height (int): Height of the ASCII art in characters
        contrast_factor (float): Factor to enhance contrast
    """
    # Extended character set chosen for shape representation capability
    # Characters are roughly organized by their visual properties
    shape_chars = {
        'heavy_vertical': '┃',
        'light_vertical': '│',
        'heavy_horizontal': '━',
        'light_horizontal': '─',
        'slash': '/',
        'backslash': '\\',
        'top_left': '┌',
        'top_right': '┐',
        'bottom_left': '└',
        'bottom_right': '┘',
        'left_curl': '(',
        'right_curl': ')',
        'solid': '█',
        'medium': '▓',
        'light': '▒',
        'sparse': '░',
        'dot': '·',
        'empty': ' '
    }
    
    # Open the image
    img = Image.open(image_path)
    
    # Enhance contrast before processing
    img = Image.fromarray(np.uint8(np.clip((np.array(img) - 128) * contrast_factor + 128, 0, 255)))
    
    # Convert to grayscale and resize
    img = img.convert('L').resize((width, height), Image.Resampling.LANCZOS)
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Apply Sobel filters for better edge detection
    sobel_x = ndimage.sobel(img_array, axis=1)
    sobel_y = ndimage.sobel(img_array, axis=0)
    
    # Calculate magnitude and direction of gradient
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    direction = np.arctan2(sobel_y, sobel_x)
    
    # Normalize magnitude for easier thresholding
    magnitude = magnitude / magnitude.max() * 255
    
    # Function to select character based on pixel properties
    def select_char(x, y):
        mag = magnitude[y, x]
        dir_angle = (np.degrees(direction[y, x]) + 180) % 180
        pixel_val = img_array[y, x]
        
        # Strong edge detection - higher threshold for small images
        if mag > 50:
            # Determine edge direction and return appropriate character
            if 22.5 <= dir_angle < 67.5:
                return shape_chars['slash']
            elif 112.5 <= dir_angle < 157.5:
                return shape_chars['backslash']
            elif 67.5 <= dir_angle < 112.5:
                return shape_chars['light_horizontal'] if mag < 100 else shape_chars['heavy_horizontal']
            else:
                return shape_chars['light_vertical'] if mag < 100 else shape_chars['heavy_vertical']
                
        # For non-edge pixels, use intensity-based characters
        else:
            if pixel_val < 50:
                return shape_chars['solid']
            elif pixel_val < 100:
                return shape_chars['medium']
            elif pixel_val < 150:
                return shape_chars['light']
            elif pixel_val < 200:
                return shape_chars['sparse']
            elif pixel_val < 230:
                return shape_chars['dot']
            else:
                return shape_chars['empty']
    
    # Check for corner patterns
    def is_corner(x, y):
        # Skip edge pixels
        if x == 0 or y == 0 or x == width-1 or y == height-1:
            return None
        
        # Get surrounding magnitudes - check for corner patterns
        top = magnitude[y-1, x] > 50
        bottom = magnitude[y+1, x] > 50
        left = magnitude[y, x-1] > 50
        right = magnitude[y, x+1] > 50
        
        # Check for corner patterns
        if top and left and not right and not bottom:
            return shape_chars['bottom_right']
        elif top and right and not left and not bottom:
            return shape_chars['bottom_left']
        elif bottom and left and not right and not top:
            return shape_chars['top_right']
        elif bottom and right and not left and not top:
            return shape_chars['top_left']
        
        return None
    
    # Generate ASCII art
    ascii_image = []
    for y in range(height):
        row = []
        for x in range(width):
            # First check if this could be a corner
            corner_char = is_corner(x, y)
            if corner_char:
                row.append(corner_char)
            else:
                row.append(select_char(x, y))
        ascii_image.append(''.join(row))
    
    # Join the rows and write to file
    with open(output_path, 'w') as f:
        f.write('\n'.join(ascii_image))
    
    print(f"Enhanced ASCII art created and saved to {output_path}")
    print(f"Dimensions: {width}x{height} characters")

def main():
    parser = argparse.ArgumentParser(description='Convert PNG images to enhanced ASCII art')
    parser.add_argument('image_path', help='Path to the input PNG image')
    parser.add_argument('output_path', help='Path for the output text file')
    parser.add_argument('--width', type=int, default=25, help='Width of ASCII art in characters (default: 25)')
    parser.add_argument('--height', type=int, default=7, help='Height of ASCII art in characters (default: 7)')
    parser.add_argument('--contrast', type=float, default=1.5, help='Contrast enhancement factor (default: 1.5)')
    
    args = parser.parse_args()
    
    image_to_ascii(args.image_path, args.output_path, args.width, args.height, args.contrast)

if __name__ == "__main__":
    main()