import cv2
import numpy as np

#color detection
def getRange(img):
    h_max = int(np.max(img[:,:,0])+8)
    h_min = int(np.min(img[:,:,0])-8)
    s_max = int(np.max(img[:,:,1])+20)
    s_min = int(np.min(img[:,:,1])-20)
    v_max = int(np.max(img[:,:,2])+20)
    v_min = int(np.min(img[:,:,2])-20)

    if h_max>180:
        h_max -= 180
    if h_min<0:
        h_min += 180
    if s_max>255:
        s_max = 255
    if s_min<0:
        s_min = 0
    if v_max>255:
        v_max = 255
    if v_min<0:
        v_min = 0

    return (np.array([h_min,s_min,v_min],dtype='uint8'),np.array([h_max,s_max,v_max],dtype='uint8'))

def getMask(img, rng):
    if rng[0][0] < rng[1][0]:
        return cv2.inRange(img, rng[0], rng[1])
    else:
        upr1 = np.array([180,rng[1][1], rng[1][2]], dtype='uint8')
        lwr1 = np.array([0,rng[0][1], rng[0][2]], dtype='uint8')
        print(rng[0], upr1)
        print(lwr1, rng[1])
        mask1 = cv2.inRange(img, rng[0], upr1)
        mask2 = cv2.inRange(img, lwr1, rng[1])
        return mask1+mask2
img = cv2.imread('pixelate0.jpeg')
print(img.shape)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image', img)

rect = cv2.selectROI('image', img)
cropped_hsv = img_hsv[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
rng = getRange(cropped_hsv)
print(rng)
mask = getMask(img_hsv, rng)
res=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('mask', mask)
cv2.imshow("img",res)
cv2.waitKey(0)

#shape detection

im=res.copy()
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