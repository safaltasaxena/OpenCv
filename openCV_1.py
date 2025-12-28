#cv2 stands for computer vision
import cv2
print("package imported")

#read images-vedios-webcam

#reading the image,imread means reading an image,we gotta mention the path where the image is present
img = cv2.imread(r"C:\Users\KIIT\OneDrive\Pictures\Camera Roll\WIN_20250811_23_50_59_Pro.jpg")
#we put r so that \ is not treated as escape sequence rather as raw string

# Resize the frame to, say, 640x360 
img = cv2.resize(img, (640, 360))  # (width, height)

#to display this image we use the fnc having 2 perimeters first is window name then obj
cv2.imshow("output",img)
#now it did show but for very less time so we gotta add some delay

cv2.waitKey(0)
#0 means infite,any num in it represents the no of miliseconds