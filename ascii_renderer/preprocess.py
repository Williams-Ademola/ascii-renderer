from PIL import Image


def to_grayscale(img):
    """Converts an image to grayscale"""
    return img.convert("L")


def resize_img(img, size):
    """Resizes an image"""
    return img.resize(size)
