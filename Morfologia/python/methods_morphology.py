# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:05:01 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy

i = "../img/imagen_line.jpeg"

img = opencv.imread(i)

kernel = numpy.ones((10, 10), numpy.uint8)
#opencv.imshow("Original Image {:} - ".format(img), img)


erosion = opencv.erode(img, kernel, iterations = 1)
opencv.imshow("Erode Image {:} - ".format(erosion), erosion)

canny = opencv.Canny(img, 100, 200)
opencv.imshow("Dilate Image {:} - ".format(canny), canny)
"""

dilation = opencv.dilate(img,kernel,iterations = 1)
opencv.imshow("Dilate Image {:} - ".format(dilation), dilation)

opening = opencv.morphologyEx(img, opencv.MORPH_OPEN, kernel)
opencv.imshow("Opening Image {:} - ".format(opening), opening)

closing = opencv.morphologyEx(img, opencv.MORPH_CLOSE, kernel)
opencv.imshow("Closing Image {:} - ".format(closing), closing)

gradient = opencv.morphologyEx(img, opencv.MORPH_GRADIENT, kernel)
opencv.imshow("Gradient Image {:} - ".format(gradient), gradient)

tophat = opencv.morphologyEx(img, opencv.MORPH_TOPHAT, kernel)
opencv.imshow("Tophat Image {:} - ".format(tophat), tophat)

blackhat = opencv.morphologyEx(img, opencv.MORPH_BLACKHAT, kernel)
opencv.imshow("Blackhat Image {:} - ".format(blackhat), blackhat)
"""
"""
byte = numpy.uint8


def ShowMatriz(matriz):
    resp = ""
    for rows in range(len(matriz)):
        for column in range(len(matriz[0])):
            resp = resp + str(matriz[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


vector_low_green = numpy.array([36, 100, 20], byte)
vector_tall_green = numpy.array([70, 255, 255], byte)

square = opencv.getStructuringElement(opencv.MORPH_RECT, (5, 5))

ellipse = opencv.getStructuringElement(opencv.MORPH_ELLIPSE, (25, 15))

cross = opencv.getStructuringElement(opencv.MORPH_CROSS, (5, 5))

line = opencv.getStructuringElement(opencv.MORPH_RECT, (10, 1))

print(ShowMatriz(line))
"""

opencv.waitKey(0)
opencv.destroyAllWindows()
