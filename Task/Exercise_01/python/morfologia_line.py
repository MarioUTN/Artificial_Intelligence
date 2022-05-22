# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:43:33 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy
from matplotlib import pyplot as plt
from sympy import primenu
from Artificial_Intelligence.functions import mario_functions as mario

file = "../img/imagen_line.jpeg"
mario.ShowImageOriginal(file)
# gray = opencv.cvtColor(mario.ReadImage(file), opencv.COLOR_BGR2GRAY)
gray = mario.GrayImageCOLOR_BGR2GRAY(file)
# thresh = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]  # Matriz binary original
thresh = mario.ThreshOTSU(file)
# print(ShowMatriz(thresh))
# Remove horizontal
# byte = numpy.uint8
# matriz = numpy.zeros((13, 13), byte)  # Create a matriz of zeros
matriz = mario.MatrixZeros(13, 13)

# matriz_diagonal_line_neg = opencv.line(matriz, (0, 0), (100, 100), (255, 0, 0), 1)  # Create the diagonal line
matriz_diagonal_line_neg = mario.MatrizDiagonalNegative(matriz)  # Create the diagonal line
# matriz_diagonal_line_pos = numpy.rot90(matriz_diagonal_line_neg, 1)  # Create the diagonal line
matriz_diagonal_line_pos = mario.MatrixDiagonalPositive(matriz)  # Create the diagonal line
# matriz_line_horizontal = opencv.getStructuringElement(opencv.MORPH_RECT, (10, 1))  # Matriz that represent a line H
matriz_line_horizontal = mario.MatrixLineHorizontal(matriz)  # Matriz that represent a line H
# matriz_line_vertical = opencv.getStructuringElement(opencv.MORPH_RECT, (1, 10))  # Matriz that represent a line V
matriz_line_vertical = mario.MatrixLineVertical(matriz)  # Matriz that represent a line V

# detected_lines_dp = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_pos, iterations=2)
# detected_lines_dn = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_neg, iterations=2)
# detected_lines_lh = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_horizontal, iterations=2)
# detected_lines_lv = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_vertical, iterations=2)

detected_lines_dp = mario.DetectLineDiagonalPos(file, matriz)
detected_lines_dn = mario.DetectLineDiagonalNeg(file, matriz)
detected_lines_lh = mario.DetectLineHorizontal(file, matriz)
detected_lines_lv = mario.DetectLineVertical(file, matriz)

# Matriz of lines found
c1, lines_found_dp = opencv.findContours(detected_lines_dp, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c2, lines_found_dn = opencv.findContours(detected_lines_dn, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c3, lines_found_lh = opencv.findContours(detected_lines_lh, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c4, lines_found_lv = opencv.findContours(detected_lines_lv, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

print("Numero de lineas diagonales possitivas: {:}".format(len(c1)))
print("Numero de lineas diagonales negativas: {:}".format(len(c2)))
print("Numero de lineas horizontales: {:}".format(len(c3)))
print("Numero de lineas diagonales verticales: {:}".format(len(c4)))

"""
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
"""
"""
images = [detected_lines_dp, detected_lines_dn, detected_lines_lh, detected_lines_lv]
titles = ["Pos: {:}".format(len(c1)), "Neg: {:}".format(len(c2)), "Hor: {:}".format(len(c3)), "Ver: {:}".format(len(c4))]

mario.ShowImagesPlot(images, titles)
plt.show()
"""
mario.ShowImageMorphology(detected_lines_dp, "Diagonal Positive")
mario.ShowImageMorphology(detected_lines_dn, "Diagonal Negative")
mario.ShowImageMorphology(detected_lines_lh, "Diagonal Horizontal")
mario.ShowImageMorphology(detected_lines_lv, "Diagonal Vertical")

opencv.waitKey(0)
opencv.destroyAllWindows()
