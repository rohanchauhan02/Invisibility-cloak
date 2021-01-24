#Import Libraries
import numpy as np
import cv2
import time

window_name='Hey there!!'
#Capturing Webcam Feed
cap=cv2.VideoCapture(0)
cv2.nmaedWindow(window_name,cv2.WINDOW_NORMAL)
time.sleep(3)

background=0
#Capturing Static Background Frame
for i in range(60):
    ret,background=cap.read()

#Flip the Image
background=np.flip(background,axis=1)
#While Camera is open execute the Algorithm on each Frame
while(cap.isOpened()):
    ret,img=cap.read()
    cnt=cnt+1
    if not ret:
        break
    cnt+=1
    img=np.flip(img,axis=1)
#Coverting from BGR to HSV
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_red=np.array([0,120,70])
upper_red=np.array([10,255,255])
mask1=cv2.inRange(hsv,lower_red,upper_red)
lower_red=np.array([170,120,70])
upper_red=np.array([180,255,255])
mask2=cv2.inRange(hsv,lower_red,upper_red)
mask1=mask1+mask2
mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
mask1=cv2.morphologyEx(mask1,cv2.MORPH_DELATE,np.ones((3,3),np.uint8),iterations=1)
mask2=cv2.bitwise_not(mask1)
res1=cv2.bitwise_and(background,background,mask=mask1)
res2=cv2.bitwise_and(img,img,mask=mask2)
final_output=cv2.addWeighted(res1,1,res2,1,0)
cv2.imshow(window_name,final_output)
k=cv2.waitKey(10)
if k==27:
    break
cap.release()
cv2.destroyAllWindows()
