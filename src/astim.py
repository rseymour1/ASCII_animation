from PIL import Image, ImageDraw, ImageFont
import os
import platform


def get_monospace_font(font_size=12):
    """Get appropriate monospace font for the current OS"""
    system = platform.system()

    try:
        if system == "Windows":
            return ImageFont.truetype("consola.ttf", font_size)  # Windows font name
        elif system == "Darwin":  # macOS
            return ImageFont.truetype("Menlo.ttc", font_size)
        else:  # Linux/Unix
            return ImageFont.truetype("DejaVuSansMono.ttf", font_size)
    except:
        # Fallback to default monospace font
        return ImageFont.load_default()


def ascii_to_image(ascii_file, output_file, font_size=12, padding=10):
    with open(ascii_file, 'r') as f:
        ascii_art = f.read().splitlines()

    font = get_monospace_font(font_size)

    # Calculate character dimensions using textbbox for modern PIL
    bbox = font.getbbox("M")
    char_width = bbox[2] - bbox[0]  # right - left
    char_height = bbox[3] - bbox[1]  # lower - upper

    max_line_length = max(len(line) for line in ascii_art)
    img_width = max_line_length * char_width + 3 * padding
    img_height = len(ascii_art) * char_height + 3 * padding

    image = Image.new('RGB', (img_width, img_height), color='white')
    draw = ImageDraw.Draw(image)

    for i, line in enumerate(ascii_art):
        y_position = padding + i * char_height
        draw.text((padding, y_position), line, font=font, fill='black')

    image.save(output_file)
    print(f"Image saved to: {os.path.abspath(output_file)}")
    return image


# Usage
ascii_file = 'cat.txt'
output_file = 'cat.png'

print(f"Current working directory: {os.getcwd()}")
image = ascii_to_image(ascii_file, output_file)
image.show()
