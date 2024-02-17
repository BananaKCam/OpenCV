#! /usr/bin/env python 

import cv2
import sys

cascPath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        frame, # Changed from gray to frame
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )



    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0, 255, 0),2)
        #print w
        #print h

        s_img=cv2.imread('pics/img1.png')

        dim=(w,h)

        s_img= cv2.resize(s_img, dim, interpolation =cv2.INTER_AREA)
        c1=y
        r1=x
        offset1=s_img.shape[0]
        frame[c1:c1+offset1,r1:r1+offset1]=s_img
        x_offset=x+w
        y_offset=y+h



        offsetx=s_img.shape[0]
        offsety=s_img.shape[1]



    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
