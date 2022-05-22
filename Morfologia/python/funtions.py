# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:45:58 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy
import os as os
import matplotlib.pyplot as plt

file = "../img/imagen_line.jpeg"


def ReadImage(file):
    return opencv.imread(file)


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


image = ReadImage(file)
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
opencv.waitKey(0)
opencv.destroyAllWindows()
