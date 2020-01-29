import cv2
im=cv2.imread("pixelate0.jpeg")
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
im=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
_,binaryim=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
cv2.imshow("sample",binaryim)
cv2.waitKey(2000)
contours,_=cv2.findContours(binaryim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx=cv2.approxPolyDP(cnt,0.0075*cv2.arcLength(cnt,True),True)
    cv2.drawContours(im,[approx],0,128,3)
    print(len(approx))
    if len(approx)==4:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"square",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.75,[60,100,100],1)
    if len(approx)>10:
        x=approx.ravel()[0]
        y=approx.ravel()[1]
        cv2.putText(im,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.75,[60,100,100],1)
im=cv2.cvtColor(im,cv2.COLOR_HSV2BGR)
cv2.imshow("gray",im)    
cv2.waitKey(2000)
