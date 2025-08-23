from PIL import Image

ascii_charset = "@%#*=+-:. "  # ascii characters from darkest to lightest


def mapping_ascii(processed_img):
    """Maps ascii characters to pixels relative to their brightness with a linear scaling formula
    Assumes image is already grayscaled and resized
    """
    width, height = processed_img.size
    pixels = processed_img.load()
    ascii_rows = []

    for y in range(height):
        row = ""
        for x in range(width):
            pixel_value = pixels[x, y]  # returns the 0 - 255 range
            # Linear scaling formula
            scale_form = int((pixel_value / 255) * (len(ascii_charset) - 1))
            row += ascii_charset[scale_form]
        ascii_rows.append(row)
    return "\n".join(ascii_rows)
