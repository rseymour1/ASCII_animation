from PIL import Image, ImageDraw, ImageFont

courier_new_path = "/System/Library/Fonts/Supplemental/Courier New.ttf"
arial_path = "/System/Library/Fonts/Supplemental/arial.ttf"
menlo_path = "/System/Library/Fonts/Menlo.ttc"
def txt_file_to_png(txt_file, output_png, font_path=menlo_path, font_size=20, save=True):
    with open(txt_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Load the Courier New font (monospaced)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise Exception("Font not found. Ensure 'Courier New' is installed or provide the correct font path.")

    # Get character dimensions
    char_width = font.getbbox("M")[2]  # Width of one character
    ascent, descent = font.getmetrics()  # Get font ascent and descent
    line_height = ascent + descent  # Total line height including spacing

    # Determine max width based on longest line (number of characters)
    max_chars = max(len(line.rstrip("\n")) for line in lines) if lines else 0
    max_width = max_chars * char_width  # Total image width

    # Calculate total image height
    img_height = line_height * len(lines)

    # Create a white background image
    img = Image.new("RGB", (max_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Draw text while maintaining exact spacing
    y = 0
    for line in lines:
        draw.text((0, y), line.rstrip("\n"), font=font, fill="black")
        y += line_height  # Move down exactly by the line height
    if save:
        img.save(output_png)

def txt_to_png(txt, output_png=None, font_path=menlo_path, font_size=20, save=False):
    # Load the Courier New font (monospaced)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise Exception("Font not found. Ensure 'Courier New' is installed or provide the correct font path.")

    # Get character dimensions
    char_width = font.getbbox("M")[2]  # Width of one character
    ascent, descent = font.getmetrics()  # Get font ascent and descent
    line_height = ascent + descent  # Total line height including spacing

    # Determine max width based on longest line (number of characters)
    max_chars = txt.find('\n')#max(len(line.rstrip("\n")) for line in txt) if txt else 0
    max_width = max_chars * char_width  # Total image width

    # Calculate total image height
    img_height = line_height * (txt.find('\n') + 1)

    # Create a white background image
    img = Image.new("RGB", (max_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    # Draw text while maintaining exact spacing
    y = 0
    for line in txt.split('\n'):
        draw.text((0, y), line.rstrip("\n"), font=font, fill="black")
        y += line_height  # Move down exactly by the line height
    if save:
        img.save(output_png)
    return img

if __name__ == "__main__":
    # Example usage
    txt_file_to_png("Data/Text/cat_792.txt", "Data/Image/cat_792.png", font_size=20)
