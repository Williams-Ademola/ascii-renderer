# This is the main page for the ASCII rendering project
from PIL import Image

def load_image():
    img = image.open(input("Enter file path: "))
    gray = img.convert("L")
    
    new_size = (300,200)
    resized_img = img.resize(new_size)

# Found a neat trick for this that confused me for a while called the interval scaling formula
def map_ascii(img,ascii_charset):
    """Map a pixel brightness value (0–255) to a single ASCII character"""

    pixel_brightness = list(img.getdata())
    ascii_set = ""
    for pixel_brightness in pixel_brightness:
        scale_form = int(pixel_brightness / 255) * (len(ascii_charset - 1))
        ascii_set += ascii_charset[scale_form]
    return ascii_set

def print_ascii(resized_img):
    for row in resized_img:
        map = ()



def main():
    """Main function to run application logic"""

if __name__ = "__main__":
    main()
