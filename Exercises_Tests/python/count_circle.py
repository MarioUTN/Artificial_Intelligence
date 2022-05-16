# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:40:57 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy


def ShowMatriz(matriz):
    resp = ""
    for rows in range(len(matriz)):
        for column in range(len(matriz[0])):
            resp = resp + str(matriz[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


img_python = "../img/morfologia.jpeg"
image = opencv.imread(img_python)
opencv.imshow("Original Image", image)
gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)

thresh = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]  # Matriz binary original

byte = numpy.uint8
matriz = numpy.zeros((20, 20), byte)

circle_matriz = opencv.circle(matriz, (10, 10), 2, (1, 1, 1), 1)

print(ShowMatriz(circle_matriz))
detected_circle = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, circle_matriz, iterations=2)
opencv.imshow("U", detected_circle)
# Matriz of lines found
circle_found = opencv.findContours(detected_circle, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

#   print(ShowMatriz(detected_circle))

circle_found = circle_found[0] if len(circle_found) == 2 else circle_found[1]
for c in circle_found:
    opencv.drawContours(image, [c], -1, (255, 255, 255), 2)


def Count(lines_found, count):
    mask = opencv.findContours(lines_found, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
    for i in enumerate(mask):
        count += 1
    return count


print(Count(detected_circle, 0))
#opencv.imshow("Image Circle", detected_circle)
opencv.waitKey(0)
opencv.destroyAllWindows()
