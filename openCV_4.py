#now we will look into some basic fncs
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250811_23_50_59_Pro.jpg")

#for dilation purposes
kernel=np.ones((5,5),np.uint8)
#matrix of ones and 0-255 scale

#converting our image into greyscale,cvtColor converts stuff into diff color spaces whatever u define in the parameter,BGR is just a convention
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#blur
imgBlur=cv2.GaussianBlur(imgGray,(25,25),0)

#to find edges
imgCanny=cv2.Canny(img,100,100)

#dilation(making white reigons of canny image thicker)
imgDilate=cv2.dilate(imgCanny,kernel,iterations=1)
#iterations is related to giving thickness

#Erosion(opp to dilation)
imgErode=cv2.erode(imgDilate,kernel,iterations=1)

imgGray = cv2.resize(imgGray, (640, 360))  
imgBlur = cv2.resize(imgBlur, (640, 360)) 
imgCanny = cv2.resize(imgCanny, (640, 360)) 
imgDilate = cv2.resize(imgDilate, (640, 360)) 
imgErode = cv2.resize(imgErode, (640, 360)) 

cv2.imshow("gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dilated image",imgDilate)
cv2.imshow("Eroded image",imgErode)


cv2.waitKey(0)