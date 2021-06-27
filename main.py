from PIL import Image


def image_to_ascii(path: str, width_per_line: int):
    """:arg path: file path to the image: str
       :arg width_per_line: number of characters per line: int
       The larger width per line, the better image detail"""

    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

    # open the image with the provided path
    img = Image.open(path)

    # get the width and height of the image, then calculate the aspect ratio
    width, height = img.size
    aspect_ratio = height / width

    # resize the image according to the width_per_line int
    new_height = aspect_ratio * width_per_line * 0.55
    img = img.resize((width_per_line, int(new_height)))

    # convert image to greyscale format
    img = img.convert('L')

    # Get the pixels from the image
    pixels = img.getdata()

    # replace each pixel with a character from array
    new_pixels = []
    for pixel in pixels:
        new_pixels.append(chars[pixel // 24])

    new_pixels = "".join(new_pixels)

    # get the number of pixels
    pixel_count = len(new_pixels)

    ascii_image = []
    for index in range(0, pixel_count, width_per_line):
        ascii_image.append(new_pixels[index:index + width_per_line])

    # Add a newline character after each line
    ascii_image = "\n".join(ascii_image)

    print(ascii_image)
