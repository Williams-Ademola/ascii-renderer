from PIL import Image
from .loader import load_image
from .preprocess import preprocess_img
from .map_ascii import mapping_ascii
from .render import render_ascii


def main():
    img_path = input("Enter image path: ")
    width = int(input("Enter your preferred width for ascii art: "))
    height = int(input("Enter your preferred height for ascii art: "))
    img_size = (width, height)

    image = load_image(img_path)
    processed_image = preprocess_img(image, img_size)
    ascii_image = mapping_ascii(processed_image)
    ascii_art = render_ascii(ascii_image)

    print(ascii_art)


if __name__ == "__main__":
    main()
