#now we will learn how to import a vedio
import cv2

#creating a vedio capture object
cap = cv2.VideoCapture(r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250805_00_49_44_Pro.mp4")

#a vedio is a sequence of images so we gotta need a while loop to go thru each frame one by one
while True:
    #now we will capture our image
    success, img= cap.read()
    #img will store the image it is an obj whereas the success is a bool it will tell us whether capturing of image is successful or not?

    # Resize the frame to, say, 640x360 
    img = cv2.resize(img, (640, 360))  # (width, height)

    #now to show this result
    cv2.imshow("vedio",img)
    
    #delay,to break out we will use "q" manually
    if cv2.waitKey(1)& 0xFF==ord('q'):
    #this check at evry 1 ms if q is pressed or not
        break