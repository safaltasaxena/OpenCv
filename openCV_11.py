#face detection
#vioala and jones method(Allowed real time object detection )
import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img=cv2.imread(r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250811_23_50_59_Pro.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#find faces in this image
faces=faceCascade.detectMultiScale(imgGray,1.1,4)

#we will create a bounding box around the faces we have detected
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)

img = cv2.resize(img, (640, 360))  
cv2.imshow("Result",img)
cv2.waitKey(0)