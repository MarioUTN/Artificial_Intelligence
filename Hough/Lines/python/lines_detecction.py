# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:09:56 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy
import functions as mario

file = "../img/cerca2.jpg"
image = mario.ReadImage(file)
gray = mario.GrayImageCOLOR_BGR2GRAY(file)
canny = mario.Canny(file, 100, 255)
lines_detected = opencv.HoughLinesP(canny, 1, numpy.pi / 180, 90, minLineLength=100, maxLineGap=10)

for line in lines_detected:
    coordx1, coordy1, coordx2, coordy2 = line[0]
    opencv.line(image, (coordx1, coordy1), (coordx2, coordy2), (255, 0, 0), 2, opencv.LINE_AA)

opencv.imshow('Canny Image', canny)
opencv.imshow('Lines Detected', image)
opencv.waitKey()
