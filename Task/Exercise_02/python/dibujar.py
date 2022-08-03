# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:46:39 2022

@author: Mario Salazar
"""


import os as os
import cv2 as opencv
import functions as f


img = "../img/llaves.png"
image = opencv.imread(img)
image = opencv.resize(image, (520, 320))
gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
ret, th = opencv.threshold(gray, 225, 255, opencv.THRESH_BINARY_INV)
outline, jerarquia = opencv.findContours(th, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

for i in range(len(outline)):
    cnt = outline[i]
    m = opencv.moments(cnt)
    # cx
    cx = int(m["m10"]/m["m00"])
    cy = int(m["m01"]/m["m00"])
    # opencv.circle(image, (cx, cy), 2, (255, 255, 255), -1)
    opencv.drawMarker(th, (cx, cy),(0, 0, 255), opencv.MARKER_CROSS, 8)
    print("({:},{:})".format(cx, cy))
    area = opencv.contourArea(cnt)
    perimeter = opencv.arcLength(cnt, True)
    # opencv.putText(th, "x: "+str(cx)+" y: "+str(cy), (cx, cy), 1, 1, (0, 0, 0), 1)
    x, y, w, h = opencv.boundingRect(cnt)
    opencv.rectangle(th, (x, y), (x+w, y+h), (255, 0, 0), 1)
    print("Area: {:}".format(area))
    print("Perimeter: {:}".format(perimeter))

print("Existed {:} numbers of objects".format(len(outline)))

opencv.imshow("Image", image)
opencv.imshow("TH", th)


opencv.waitKey(0)
opencv.destroyAllWindows()

