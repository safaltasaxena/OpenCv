#contours/shape detection
#get corner point to detect what is the shape of this object
import cv2
import numpy as np

path=r"C:\Users\KIIT\Downloads\shapes.opencv.jpg"
img=cv2.imread(path)

#preprocessing
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)

#finding edges in our image,from these edges we are gonna find out the contours
imgCanny=cv2.Canny(imgBlur,50,50)

#creating a copy of og img so as to put areas on it and keep og one as it is
imgContour=img.copy()

#creating a fnc
def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #RETR_EXTERNAL retrives the extreme outer contours
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,[cnt],-1,(255,0,0),3)
            #calculate the curve length 
            per=cv2.arcLength(cnt,True)
            print(per)
            #approximate corner pts
            approx=cv2.approxPolyDP(cnt,0.02*per,True)
            #true ensures the images with closed contour
            print(len(approx))
            objCor=len(approx)
            #drawing a bounding box around my image
            x,y,w,h=cv2.boundingRect(approx)
            
            #identifying indiviual shapes now
            if objCor==3:
                objectType="Tri"
            elif objCor==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType="Sq"
                else:
                    objectType="Rect"
            elif objcor>4:
                objectType="Circles"
            else:
                objectType="None"

            #draw them
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,(y+h//2-10)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
            #bounding box helps in total width height center 

        
img = cv2.resize(img, (400,400)) 
imgGray = cv2.resize(imgGray, (400,400)) 
imgBlur = cv2.resize(imgBlur, (400,400)) 
imgCanny = cv2.resize(imgCanny, (400,400)) 
imgContour = cv2.resize(imgContour, (400,400))

getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Contoured",imgContour)


cv2.waitKey(0)