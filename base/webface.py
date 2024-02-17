#! /usr/bin/env python 

import cv2
import sys

import random


cascPath = "haarcascade/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()



    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		#for r in range(10):
		#	randx = random.randint(x,w)
		#	randy = random.randint(y,h)
		#	cv2.circle(frame, (x + randx , y + randy), 1, (0, 255, 0))
			
		crop_img = frame[y:y + h, x:x + w] # Crop from x, y, w, h -> 100, 200, 300, 400
		cv2.imshow('cropped', crop_img)
	# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
