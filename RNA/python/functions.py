# -*- coding: utf-8 -*-
"""
Created on Sat May 21 07:52:38 2022

@author: Mario Salazar
"""


import cv2 as opencv
import numpy as numpy
import os as os
import matplotlib.pyplot as plt


def ReadImage(file):
    if os.path.isfile(file):
        return opencv.imread(file)
    else:
        print("Error")


def ShowImageOriginal(file):
    if os.path.isfile(file):
        image = ReadImage(file)
        return opencv.imshow("Original Image", image)
    else:
        print("Error!")


def ShowImageMorphology(method, title):
    return opencv.imshow(title, method)


def Kernel(rows, columns):
    return numpy.ones((rows, columns), numpy.uint8)


def Erode(file, kernelx, kernely):
    return opencv.erode(ReadImage(file), Kernel(kernelx, kernely), iterations=1)


def Canny(file, t_lower, t_upper):
    return opencv.Canny(ReadImage(file), t_lower, t_upper)


def CannyApertureSize(file, t_lower, t_upper):
    return opencv.Canny(ReadImage(file), t_lower, t_upper, apertureSize=5)


def CannyL2Gradient(file, t_lower, t_upper):
    return opencv.Canny(ReadImage(file), t_lower, t_upper, L2gradient=True)


def CannyL2GradientApertureSize(file, t_lower, t_upper):
    return opencv.Canny(ReadImage(file), t_lower, t_upper, apertureSize=5, L2gradient=True)


def ShowImagesPlot(matrix_images, matrix_titles):
    for i in range(len(matrix_images)):
        plt.subplot(int(len(matrix_images) / 2 + 1), 2, i + 1)
        plt.imshow(opencv.cvtColor(matrix_images[i], opencv.COLOR_BGR2RGB), vmin=0, vmax=255)
        plt.title(matrix_titles[i])
        plt.xticks([]), plt.yticks([])


def ShowMatriz(matrix):
    resp = ""
    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            resp = resp + str(matrix[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


def GrayImageCOLOR_BGR2GRAY(file):
    return opencv.cvtColor(ReadImage(file), opencv.COLOR_BGR2GRAY)


def GrayImageIMREAD_GRAYSCALE(file):
    return opencv.imread(file, opencv.IMREAD_GRAYSCALE)


def ThreshOTSU(file):
    gray = GrayImageCOLOR_BGR2GRAY(file)
    return opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]


def Count(lines_found, count):
    mask = opencv.findContours(lines_found, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
    for i in enumerate(mask):
        count += 1
    return count


def MatrixCircle(radio):
    byte = numpy.uint8
    matriz = numpy.zeros((int(radio * 4), int(radio * 4)), byte)
    circle_matriz = opencv.circle(matriz, (int(radio * 2), int(radio * 2)), 2, (255, 0, 0), 1)
    return circle_matriz


def DetectCircle(file, radio):
    detected_circle = opencv.morphologyEx(ThreshOTSU(file), opencv.MORPH_OPEN, MatrixCircle(radio), iterations=2)
    return detected_circle


def CircleFound(file, radio):
    return opencv.findContours(DetectCircle(file, radio), opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)


def MatrixZeros(rows, columns):
    byte = numpy.uint8
    matriz = numpy.zeros((10, 10), byte)  # Create a matriz of zeros
    return matriz


def MatrizDiagonalNegative(matrix):
    return opencv.line(matrix, (0, 0), (25, 25), (255, 0, 0), 1)


def MatrixDiagonalPositive(matrix):
    return numpy.rot90(MatrizDiagonalNegative(matrix), 1)


def MatrixLineHorizontal(matrix):
    return opencv.getStructuringElement(opencv.MORPH_RECT, (10, 1))


def MatrixLineVertical(matrix):
    return opencv.getStructuringElement(opencv.MORPH_RECT, (1, 10))


def DetectLineDiagonalPos(file, matrix):
    return opencv.morphologyEx(ThreshOTSU(file), opencv.MORPH_OPEN, MatrixDiagonalPositive(matrix), iterations=2)


def DetectLineDiagonalNeg(file, matrix):
    return opencv.morphologyEx(ThreshOTSU(file), opencv.MORPH_OPEN, MatrizDiagonalNegative(matrix), iterations=2)


def DetectLineHorizontal(file, matrix):
    return opencv.morphologyEx(ThreshOTSU(file), opencv.MORPH_OPEN, MatrixLineHorizontal(matrix), iterations=2)


def DetectLineVertical(file, matrix):
    return opencv.morphologyEx(ThreshOTSU(file), opencv.MORPH_OPEN, MatrixLineVertical(matrix), iterations=2)




"""

erode = Erode(file, 2, 2)
canny = Canny(file, 100, 200)
canny_az = CannyApertureSize(file, 100, 200)
canny_l2gradient = CannyL2Gradient(file, 100, 200)
canny_l2gradient_az = CannyL2Gradient(file, 100, 200)

mi = [image, erode, canny, canny_az, canny_l2gradient, canny_l2gradient_az]
titles = ['Original', 'Erode', 'Canny', 'canny_az', 'canny_l2gradient', 'canny_l2gradient_az']

# ShowImageMorphology(erode, "Erode")
# ShowImageMorphology(canny, "Canny")
# ShowImageMorphology(canny_az, "Aperture")
# ShowImageMorphology(canny_l2gradient, "L2Gradient")
# ShowImageMorphology(canny_l2gradient_az, "L2Gradient")
# ShowImageOriginal(file)
ShowImagesPlot(mi, titles)

print(len(mi))
plt.show()
"""
opencv.waitKey(0)
opencv.destroyAllWindows()
