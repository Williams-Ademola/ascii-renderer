from PIL import Image

# Trying to open the image file
try:
    img = Image.open(
        "/home/williamArch/Downloads/aleks-dahlberg-pVATCBKLH8w-unsplash.jpg"
    )
    # Convert to grayscale
    gray = img.convert("L")

    # resize grayscale image
    new_size = (300, 200)
    resized_img = gray.resize(new_size)

    # Show the resized_img image
    resized_img.show()

    # Save the resized img
    resized_img.save("resized_img.jpg")

    # Mapping brightness to ascii characters that'll serves as art base


except FileNotFoundError:
    print("Error: Image file not found, please check path")
except IOError:
    print("Error: Could not open or identify image file.")
