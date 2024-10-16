import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def bright(image,factor):
    imgBright = image.astype(np.float32)
    imgBright = imgBright + factor
    imgBright = np.clip(imgBright, 0, 255)
    return imgBright.astype(np.uint8)

def contrast(image, factor):
    mean = 128
    img_contrast = image.astype(np.float32)
    img_contrast = mean + factor * (img_contrast - mean)
    img_contrast = np.clip(img_contrast,0,255)
    return img_contrast.astype(np.uint8)

path = "C:\\Users\\JARKOM 17\\Downloads\\Bright.jpg" 
image = img.imread(path)
hist,bins = np.histogram(image.flatten(), bins=256, range=[0,256])

imgContrast = contrast(image,1.5)
hist_c, bins = np.histogram(imgContrast.flatten(), bins=256, range=[0,256])
    
plt.figure(figsize =(10,10))

plt.subplot(2,2,1)
plt.imshow(image)

plt.subplot(2,2,2)
plt.imshow(imgContrast)

plt.subplot(2,2,3)
plt.plot(hist)

plt.subplot(2,2,4)
plt.plot(hist_c)

plt.show()