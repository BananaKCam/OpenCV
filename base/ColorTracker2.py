#!/usr/bin/env python 

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
 

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    ## (152, 105, 127)), np.array((180, 145, 167))
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    #lower_blue = np.array([150,105,125])
    #upper_blue = np.array([180,145,170])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    
    contours,hierarchy = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    #Finding contour with maximum area and store it as best_cnt
    max_area = 0
    for cnt in contours:
       area = cv2.contourArea(cnt)
       if area > max_area:
           max_area = area
           best_cnt = cnt
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    print("x : " + str(cx) + " :: y : " + str(cy) + " :: area : " + str(max_area))
    cv2.circle(res,(cx,cy),10,255,-1)

    #moments = cv2.moments(mask)
    ##area = cv2.GetCentralMoment(moments, 0, 0)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
