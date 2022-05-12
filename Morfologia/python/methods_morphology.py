# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:05:01 2022

@author: Mario Salazar
"""


import cv2 as opencv
import numpy as numpy

import cv2 as cv
import numpy as np

i = "../img/j.jpg"

img = cv.imread("j.png")
kernel = np.ones((5, 5), np.uint8)
cv.imshow("Original Image {:} - ".format(img), img)

"""
erosion = cv.erode(img, kernel, iterations = 1)
cv.imshow("Erode Image {:} - ".format(erosion), erosion)

dilation = cv.dilate(img,kernel,iterations = 1)
cv.imshow("Dilate Image {:} - ".format(dilation), dilation)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow("Opening Image {:} - ".format(opening), opening)

closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow("Closing Image {:} - ".format(closing), closing)

gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow("Gradient Image {:} - ".format(gradient), gradient)

tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow("Tophat Image {:} - ".format(tophat), tophat)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow("Blackhat Image {:} - ".format(blackhat), blackhat)

"""
byte = numpy.uint8
def ShowMatriz(matriz):
    resp = ""
    for rows in range(len(matriz)):
        for column in range(len(matriz[0])):
            resp=resp+str(matriz[rows][column])+"\t"
        resp=resp+"\n"
    return resp
vector_low_green = numpy.array([36, 100, 20], byte)
vector_tall_green = numpy.array([70, 255, 255], byte)

square = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

elipse = cv.getStructuringElement(cv.MORPH_ELLIPSE,(25,15))

cross = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))

line = cv.getStructuringElement(cv.MORPH_RECT,(10,1))

print(ShowMatriz(line))

opencv.waitKey(0)
opencv.destroyAllWindows()
