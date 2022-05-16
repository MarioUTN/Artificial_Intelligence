# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:37:51 2022

@author: Mario Salazar
"""

# -*- coding: utf-8 -*-

import cv2 as opencv
import numpy as numpy
from matplotlib import pyplot as plt


def ShowMatriz(matrix):
    resp = ""
    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            resp = resp + str(matrix[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


img_python = "../img/imagen_line.jpeg"
image = opencv.imread(img_python)

gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)

thresh = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]  # Matriz binary original

# Remove horizontal
byte = numpy.uint8
matriz = numpy.zeros((10, 10), byte)  # Create a matriz of zeros

matriz_diagonal_line_neg = opencv.line(matriz, (0, 0), (25, 25), (1, 1, 1), 1)  # Create the diagonal line

matriz_diagonal_line_pos = numpy.rot90(matriz_diagonal_line_neg, 1)  # Create the diagonal line
matriz_line_horizontal = opencv.getStructuringElement(opencv.MORPH_RECT, (10, 1))  # Matriz that represent a line H
matriz_line_vertical = opencv.getStructuringElement(opencv.MORPH_RECT, (1, 10))  # Matriz that represent a line V

detected_lines_dp = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_pos, iterations=2)
detected_lines_dn = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_neg, iterations=2)
detected_lines_lh = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_horizontal, iterations=2)
detected_lines_lv = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_vertical, iterations=2)


# Matriz of lines found
lines_found_dp = opencv.findContours(detected_lines_dp, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
lines_found_dn = opencv.findContours(detected_lines_dn, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
lines_found_lh = opencv.findContours(detected_lines_lh, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
lines_found_lv = opencv.findContours(detected_lines_lv, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)


print(lines_found_dp)

lines_found_dp = lines_found_dp[0] if len(lines_found_dp) == 2 else lines_found_dp[1]
for c in lines_found_dp:
    opencv.drawContours(image, [c], -1, (255, 255, 255), 2)

lines_found_dn = lines_found_dn[0] if len(lines_found_dn) == 2 else lines_found_dn[1]
for c in lines_found_dn:
    opencv.drawContours(image, [c], -1, (255, 255, 255), 2)

lines_found_lh = lines_found_lh[0] if len(lines_found_lh) == 2 else lines_found_lh[1]
for c in lines_found_lh:
    opencv.drawContours(image, [c], -1, (255, 255, 255), 2)

lines_found_lv = lines_found_lv[0] if len(lines_found_lv) == 2 else lines_found_lv[1]
for c in lines_found_lv:
    opencv.drawContours(image, [c], -1, (255, 255, 255), 2)


def Count(lines_found, count):
    mask = opencv.findContours(lines_found, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
    for i in enumerate(mask):
        count += 1
    return count


opencv.imshow("Original Image", image)
opencv.imshow("{:} Diagonal Pos".format(Count(detected_lines_dp, 0)), detected_lines_dp)
opencv.imshow("{:} Diagonal Neg".format(Count(detected_lines_dn, 0)), detected_lines_dn)
opencv.imshow("{:} Horizontal Line".format(Count(detected_lines_lh, 0)), detected_lines_lh)
opencv.imshow("{:} Vertical Line".format(Count(detected_lines_lv, 0)), detected_lines_lv)

opencv.waitKey(0)
opencv.destroyAllWindows()

"""
images = [image, detected_lines_dp, detected_lines_dn, detected_lines_lh, detected_lines_lv]
tittle = ['Image Original','Image Binary','Image Binary_INV','Image Trunk', 'Ultimo']

for i in range(len(images)):
    plt.subplot(3, 2, i+1)
    plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(tittle[i])
    plt.xticks([]),plt.yticks([])

plt.show()
"""
