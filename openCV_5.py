#resizing and cropping
import cv2;
import numpy as np

img = cv2.imread(r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250811_23_50_59_Pro.jpg")
#to resize the image we gotta know the inital size of image
print(img.shape)
#(width,height,channels(BGR))

#resize
imgResize = cv2.resize(img,(300,200))

cv2.imshow("imgResize",imgResize)

print(imgResize.shape)

#cropping
imgCropped=img[0:200,200:500]
cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0)