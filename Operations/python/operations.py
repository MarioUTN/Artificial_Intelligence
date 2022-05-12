# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:40:37 2022

@author: Mario Salazar
"""

import os as os
import cv2 as opencv
import numpy as numpy


def Area(image):
    area = 0
    if os.path.isfile(image):
        img = opencv.imread(image)
        gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
        canny = opencv.Canny(gray, 10, 150)

    return area


def ShowMatriz(matriz):
    resp = ""
    for rows in range(len(matriz)):
        for column in range(len(matriz[0])):
            resp = resp + str(matriz[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


def Perimeter(image):
    perimeter = 0
    return perimeter


def OutLine(image):
    return


def InclinationAngle(image):
    return


def MassCenter(image):
    return


def Semi_MajorAxis(image):
    return


def Semi_MinorAxis(image):
    return


img = "../img/figuras-geometricas.png"
image = opencv.imread(img)
gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
ret, th = opencv.threshold(gray, 225, 255, opencv.THRESH_BINARY_INV)

outline, jerarq = opencv.findContours(th, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

for i in range(len(outline)):
    cnt = outline[i]
    m = opencv.moments(cnt)
    # cx
    cx = int(m["m10"]/m["m00"])
    cy = int(m["m01"]/m["m00"])
    opencv.circle(image, (cx, cy), 2, (255, 255, 255), -1)
    print("({:},{:})".format(cx, cy))
    area = opencv.contourArea(cnt)
    perimeter = opencv.arcLength(cnt, True)
    opencv.putText(image, "x: "+str(cx)+" y: "+str(cy), (cx, cy), 1, 1, (0, 0, 0), 1)
    x, y, w, h = opencv.boundingRect(cnt)
    opencv.rectangle(image, (x, y), (x+w, y+h), (234, 26, 127), 1)
    print("Area: {:}".format(area))
    print("Perimeter: {:}".format(perimeter))

opencv.imshow("Image", image)
opencv.imshow("TH", th)


opencv.waitKey(0)
opencv.destroyAllWindows()

