#now we will learn how to use a webcam
import cv2

#instead of path of vedio we use 0 as default webcam
cap = cv2.VideoCapture(0)

#now we will define some parameters for it
cap.set(3,640)#id no. 3 is width
cap.set(4,480)#id no. 4 is height
cap.set(10,100)#id no. 10 i brightness

#a vedio is a sequence of images so we gotta need a while loop to go thru each frame one by one
while True:
    #now we will capture our image
    success, img= cap.read()
    #img will store the image it is an obj whereas the success is a bool it will tell us whether capturing of image is successful or not?

    #now to show this result
    cv2.imshow("vedio",img)
    
    #delay,to break out we will use "q" manually
    if cv2.waitKey(1)& 0xFF==ord('q'):
    #this check at evry 1 ms if q is pressed or not
        break