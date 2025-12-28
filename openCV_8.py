#joining images
#drawback-both of them should have same no of RGB (channels) and u cant rezise the final image,to deal w this drawback we gotta prep a fnc
import cv2
import numpy as np 

img = cv2.imread(r"C:\Users\KIIT\Downloads\ChatGPT Image Aug 15, 2025, 12_46_27 AM.png")

#horizontal stack
imghor=np.hstack((img,img))
#vertical stack
imgVer=np.vstack((img,img))

imghor = cv2.resize(imghor, (640, 360))  
imgVer = cv2.resize(imgVer, (640, 360))  

cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)