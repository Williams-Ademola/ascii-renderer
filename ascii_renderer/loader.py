from PIL import Image


# Loading up the image file
def load_image(path):
    # Open an image and return it
    try:
        img = Image.open(path)
        return img
    except FileNotFoundError:
        print("Error: Image file not found, please check path")
        return None
    except IOError:
        print("Error: Could not open or identify image file.")
        return None
