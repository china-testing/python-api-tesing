# blend.py

from PIL import Image

def avg(x, y):
    """Return average of x and y."""
    return (x + y)/2

def blend(img1, img2):
    """Return blend of two images of the same size."""
    if img1.size != img2.size:
        raise ValueError("Images are not the same size.")
    width, height = img1.size
    newimg = Image.new("RGB", (width, height))
    for j in range(height):
        for i in range(width):
            r1, g1, b1 = img1.getpixel((i, j))
            r2, g2, b2 = img2.getpixel((i, j))
            newimg.putpixel((i, j),
                            (int(avg(r1, r2)),
                             int(avg(g1, g2)),
                             int(avg(b1, b2))))
    return newimg
    
def main():
    try:
        img1 = Image.open("lake.jpg")
        img2 = Image.open("lake2.jpg")
        newimg = blend(img1, img2)
        newimg.save("lake_blend.jpg")
    except (OSError, ValueError) as err:
        print("Error:", err)
        print("Unable to process blending.")
    
main()
