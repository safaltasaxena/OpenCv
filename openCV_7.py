#WARP perspective to get its bird eye view
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\KIIT\Downloads\ChatGPT Image Aug 15, 2025, 12_46_27 AM.png")

width,height=300,270
#defining the 4 corner points of the image which i need to be flatten properly and shown to me
pts1=np.float32([[490,200],[790,200],[790,470],[490,470]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
