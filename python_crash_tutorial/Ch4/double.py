# double.py

from PIL import Image

def double(img):
    """Return copy of img with doubled width, height."""
    width, height = img.size
    newimg = Image.new("RGB", (2*width, 2*height))
    for j in range(height):
        for i in range(width):
            color = img.getpixel((i, j))
            newimg.putpixel((2*i, 2*j), color)
            newimg.putpixel((2*i, 2*j + 1), color)
            newimg.putpixel((2*i + 1, 2*j), color)
            newimg.putpixel((2*i + 1, 2*j + 1), color)
    return newimg

def main():
    img = Image.open("lake.jpg")
    newimg = double(img)
    newimg.save("lake_double.jpg")
    
main()
