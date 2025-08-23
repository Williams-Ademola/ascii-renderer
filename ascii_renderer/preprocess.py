from PIL import Image


def preprocess_img(img, size):
    # convert to grayscale
    processed_img = img.convert("L")
    # resize image
    processed_img = processed_img.resize(size)
    return processed_img
