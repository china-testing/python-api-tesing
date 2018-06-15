# rotate_right.py

from PIL import Image

def rotate_right(img):
    """Return copy of img rotated right 90 degrees."""
    width, height = img.size
    newimg = Image.new("RGB", (height, width))
    for j in range(height):
        for i in range(width):
            color = img.getpixel((i, j))
            newimg.putpixel((height - j - 1, i), color)
    return newimg

def main():
    img = Image.open("lake.jpg")
    newimg = rotate_right(img)
    newimg.save("lake_rotate_right.jpg")

main()
