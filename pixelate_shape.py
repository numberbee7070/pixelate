import cv2
img=cv2.imread("pixelate0.jpeg",0)
_,img2=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
cv2.imshow("sample",img2)
cv2.waitKey(2000)
contours,_=cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img,[approx],0,128,3)
    print(len(approx))
    if len(approx)==4:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(img,"sq",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(128),1)
    if len(approx)>10:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(128),1)

cv2.imshow("img",img)    
cv2.waitKey(2000)
