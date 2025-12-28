#color detection
import cv2
import numpy as np

def empty(a):
    pass

path=r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250811_23_50_59_Pro.jpg"

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("hue min","TrackBars",170,179,empty)
cv2.createTrackbar("hue max","TrackBars",179,179,empty)
cv2.createTrackbar("sat min","TrackBars",62,255,empty)
cv2.createTrackbar("sat max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)

#If you didn’t have the while True:, the image and trackbar would only be read once, and moving the slider after that wouldn’t do anything.
while True:
 img=cv2.imread(path)

 #now our task to detect the pink color of my shirt
 imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

 #reading the trackbar so that we can apply these features on our image
 h_min=cv2.getTrackbarPos("hue min","TrackBars")
 h_max=cv2.getTrackbarPos("hue max","TrackBars")
 s_min=cv2.getTrackbarPos("sat min","TrackBars")
 s_max=cv2.getTrackbarPos("sat max","TrackBars")
 v_min=cv2.getTrackbarPos("val min","TrackBars")
 v_max=cv2.getTrackbarPos("val max","TrackBars")
 print(h_min,h_max,s_min,s_max,v_min,v_max)

 #now we gonna use these values to filter out the particular color in that range
 lower=np.array([h_min,s_min,v_min])
 upper=np.array([h_max,s_max,v_max])
 mask=cv2.inRange(imgHSV,lower,upper)

 #now instead of white part we gonna display the real image color in the mask
 imgResult=cv2.bitwise_and(img,img,mask=mask)
 #bitwise and bascially idenitfies where are pixels present in both the images then combine them to show

 img = cv2.resize(img, (640, 360)) 
 imgHSV = cv2.resize(imgHSV, (640, 360)) 
 mask=cv2.resize(mask,(640,360))
 imgResult = cv2.resize(imgResult, (640, 360)) 
 
 cv2.imshow("Original",img)
 cv2.imshow("HSV",imgHSV)
 cv2.imshow("Mask",mask)
 cv2.imshow("Rsult",imgResult)
 #we will keep all the colors in black which we dont want to detect and the ones w e want odetect in white.then will change the min values above acc.then by default we will get the mask
 
 cv2.waitKey(1)
 #changed it to 0 to 1 since after every 1ms it would read the images and show us changed vlues thus giving real time live effect