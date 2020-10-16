import sys
import numpy as np
import cv2
import json
import os
import math

cwd = os.path.dirname(os.path.abspath(__file__))
face_cascade = cv2.CascadeClassifier(cwd + ".\\data\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cwd + ".\\data\\haarcascade_eye.xml")
eyeglasses_cascade = cv2.CascadeClassifier(cwd + ".\\data\\haarcascade_eye_tree_eyeglasses.xml")
img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, int(sys.argv[2]))

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, int(sys.argv[3]))
    eyeglasses = eyeglasses_cascade.detectMultiScale(roi_gray, 1.2, int(sys.argv[4]))
    for (ex,ey,ew,eh) in eyes:
        print(x+ex+math.floor(ew/2),y+ey+math.floor(eh/2), end=";")
    for (ex,ey,ew,eh) in eyeglasses:
        print(x+ex+math.floor(ew/2),y+ey+math.floor(eh/2), end=";")