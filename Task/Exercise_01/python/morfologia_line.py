# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:43:33 2022

@author: Mario Salazar
"""
# password-
import cv2 as opencv
import numpy as numpy
from matplotlib import pyplot as plt
from sympy import primenu
import functions as f

file = "../img/imagen_line.jpeg"
f.ShowImageOriginal(file)
# gray = opencv.cvtColor(f.ReadImage(file), opencv.COLOR_BGR2GRAY)
gray = f.GrayImageCOLOR_BGR2GRAY(file)
# thresh = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]  # Matriz binary original
thresh = f.ThreshOTSU(file)
# print(ShowMatriz(thresh))
# Remove horizontal
# byte = numpy.uint8
# matriz = numpy.zeros((13, 13), byte)  # Create a matriz of zeros
matriz = f.MatrixZeros(13, 13)

# matriz_diagonal_line_neg = opencv.line(matriz, (0, 0), (100, 100), (255, 0, 0), 1)  # Create the diagonal line
matriz_diagonal_line_neg = f.MatrizDiagonalNegative(matriz)  # Create the diagonal line
# matriz_diagonal_line_pos = numpy.rot90(matriz_diagonal_line_neg, 1)  # Create the diagonal line
matriz_diagonal_line_pos = f.MatrixDiagonalPositive(matriz)  # Create the diagonal line
# matriz_line_horizontal = opencv.getStructuringElement(opencv.MORPH_RECT, (10, 1))  # Matriz that represent a line H
matriz_line_horizontal = f.MatrixLineHorizontal(matriz)  # Matriz that represent a line H
# matriz_line_vertical = opencv.getStructuringElement(opencv.MORPH_RECT, (1, 10))  # Matriz that represent a line V
matriz_line_vertical = f.MatrixLineVertical(matriz)  # Matriz that represent a line V

# detected_lines_dp = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_pos, iterations=2)
# detected_lines_dn = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_diagonal_line_neg, iterations=2)
# detected_lines_lh = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_horizontal, iterations=2)
# detected_lines_lv = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, matriz_line_vertical, iterations=2)

detected_lines_dp = f.DetectLineDiagonalPos(file, matriz)
detected_lines_dn = f.DetectLineDiagonalNeg(file, matriz)
detected_lines_lh = f.DetectLineHorizontal(file, matriz)
detected_lines_lv = f.DetectLineVertical(file, matriz)

# Matriz of lines found
c1, lines_found_dp = opencv.findContours(detected_lines_dp, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c2, lines_found_dn = opencv.findContours(detected_lines_dn, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c3, lines_found_lh = opencv.findContours(detected_lines_lh, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
c4, lines_found_lv = opencv.findContours(detected_lines_lv, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

print("Positive diagonal line numbers: {:}".format(len(c1)))
print("Negative diagonal line numbers: {:}".format(len(c2)))
print("Horizontal line numbers: {:}".format(len(c3)))
print("Vertical line numbers: {:}".format(len(c4)))

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

f.ShowImagesPlot(images, titles)
plt.show()
"""
f.ShowImageMorphology(detected_lines_dp, "Diagonal Positive")
f.ShowImageMorphology(detected_lines_dn, "Diagonal Negative")
f.ShowImageMorphology(detected_lines_lh, "Diagonal Horizontal")
f.ShowImageMorphology(detected_lines_lv, "Diagonal Vertical")

opencv.waitKey(0)
opencv.destroyAllWindows()
