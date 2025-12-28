#shapes and texts
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#zeros actually represent black

#to color image
#img[:]=255,0,0#creates a blue image

cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,0),3)
#(0,0)is the start pt,(300,300)ending pt,(0,255,0)is color,3 is thickness

#rectangles
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
#filled to fill up

#circle 
cv2.circle(img,(400,50),30,(255,255,0),5)

#texts
cv2.putText(img,"OPENCV",(200,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,150,0),3)

cv2.imshow("image",img)
print(img)

cv2.waitKey(0)