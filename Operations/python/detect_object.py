# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:05:55 2022

@author: Mario Salazar
"""

import cv2 
import numpy as np 
  
image = cv2.imread('../img/Figuras-Geometricas-para-Ninos.jpg', 0) 
  
params = cv2.SimpleBlobDetector_Params() 
  
params.filterByArea = True
params.minArea = 100
  
params.filterByCircularity = True 
params.minCircularity = 0.9
  
params.filterByConvexity = True
params.minConvexity = 0.2
      
params.filterByInertia = True
params.minInertiaRatio = 0.01
  
detector = cv2.SimpleBlobDetector_create(params) 
      
keypoints = detector.detect(image) 
  
blank = np.zeros((1, 1))  
blobs = cv2.drawKeypoints(image, keypoints, blank,(0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
  
number_of_blobs = len(keypoints) 
text = "Number of Circular Blobs: " + str(len(keypoints)) 
cv2.putText(blobs, text,(20, 550), 
            cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 100, 255), 2) 
  
cv2.imshow("Filtering Circular Blobs Only", blobs) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = "../img/Figuras-Geometricas-para-Ninos.jpg"
img = cv2.imread(img1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshold = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

for contour in contours:

    if i == 0:
        i = 1
        continue

    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    print(len(approx))

    cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)

    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    elif len(approx) == 4:
        cv2.putText(img, 'Quadrilateral', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    else:
        cv2.putText(img, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""