from PIL import Image

ascii_charset = "@%#*=+-:. "  # ascii characters from darkest to lightest


def map_ascii(img):
    """Maps ascii characters to pixels relative to their brightness with a linear scaling formula
    Assumes image is already grayscaled and resized
    """
    width, height = img.size
    pixels = img.load()
    ascii_image = ""

    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]  # returns the 0 - 255 range
            # Linear scaling formula
            scale_form = int((pixel_value / 255) * (len(ascii_charset) - 1))
            ascii_image += ascii_charset[scale_form]
        ascii_image += "\n"  # new line after each row
    return ascii_image
