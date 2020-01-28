import cv2
import numpy as np


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

img = cv2.imread('pixelate0.jpeg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image', img)

rect = cv2.selectROI('image', img)
cropped_hsv = img_hsv[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
rng = getRange(cropped_hsv)
print(rng)
mask = cv2.inRange(img_hsv, rng[0], rng[1])
cv2.imshow('mask', mask)
