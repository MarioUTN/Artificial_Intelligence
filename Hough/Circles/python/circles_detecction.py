# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:02:37 2022

@author: Mario Salazar
"""
import cv2 as opencv
import numpy as np

img = opencv.imread('../img/valvulas-industriales.jpg')
src = opencv.medianBlur(img, 7)
src = opencv.cvtColor(src, opencv.COLOR_BGR2GRAY)

circles = opencv.HoughCircles(src, opencv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=30, maxRadius=50)

circles = np.uint16(np.around(circles))
for index in circles[0, :]:
    opencv.circle(img, (index[0], index[1]), index[2], (255, 0, 0), 2)
    opencv.circle(img, (index[0], index[1]), 2, (0, 0, 255), 1)

opencv.imshow('Detected Circles: {0}'.format(len(circles[0, :])), img)
opencv.waitKey(0)
opencv.destroyAllWindows()
