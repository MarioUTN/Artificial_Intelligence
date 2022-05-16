# -*- coding: utf-8 -*-
"""
Created on Sat May 14 23:23:57 2022

@author: Mario Salazar
"""

import cv2 as opencv
import matplotlib.pyplot as plt
import numpy as numpy

img = opencv.imread('pieza-1.png', 0)
gray = opencv.imread('pieza-1.png', opencv.IMREAD_GRAYSCALE)
ret, threshold = opencv.threshold(img, 0, 255, opencv.THRESH_BINARY | opencv.THRESH_OTSU)
ret1, threshold1 = opencv.threshold(gray, 122, 255, opencv.THRESH_BINARY_INV)
print(ret)
im_floodfill = threshold1.copy()

h, w = threshold1.shape[:2]
mask = numpy.zeros((h+2, w+2), numpy.uint8)

a = opencv.floodFill(im_floodfill, mask, (0, 0), 255)

im_floodfill_inv = opencv.bitwise_not(im_floodfill)
im_out = threshold1 | im_floodfill_inv

opencv.imshow("O", img)
opencv.imshow("Otsu", threshold)
opencv.imshow("Rel", im_floodfill_inv)
opencv.waitKey(0)