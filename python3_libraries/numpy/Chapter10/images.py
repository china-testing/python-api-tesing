from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


image = misc.lena().astype(np.float32)

plt.subplot(221)
plt.title("Original Image") 
img = plt.imshow(image, cmap=plt.cm.gray) 
plt.axis("off")

plt.subplot(222) 
plt.title("Median Filter") 
filtered = ndimage.median_filter(image, size=(42,42))
plt.imshow(filtered, cmap=plt.cm.gray) 
plt.axis("off")

plt.subplot(223) 
plt.title("Rotated") 
rotated = ndimage.rotate(image, 90)
plt.imshow(rotated, cmap=plt.cm.gray) 
plt.axis("off")

plt.subplot(224) 
plt.title("Prewitt Filter") 
filtered = ndimage.prewitt(image)
plt.imshow(filtered, cmap=plt.cm.gray) 
plt.axis("off")
plt.show()
