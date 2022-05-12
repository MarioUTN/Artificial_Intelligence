# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:57:52 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy
from matplotlib import pyplot as plt
import os as os

img = "../img/imagen.jpeg"


# Method to show an original image
def ShowImageOriginal(image):
    if os.path.isfile(image):
        vector_image = opencv.imread(image)
        opencv.imshow("Original Image {:} - ".format(image), vector_image)
    else:
        print("No image found!")


def Histogram(image):
    if os.path.isfile(image):
        img = opencv.imread(image)
        image_gray = opencv.cvtColor(img, opencv.COLOR_BGR2RGB)
        hist = opencv.calcHist([image_gray], [0], None, [256], [0, 255])
        fig = plt.figure(1)
        pl = fig.add_subplot(312)
        pl.plot(hist)
        fig.show()
        opencv.waitKey(0)
        opencv.destroyAllWindows()
        plt.close(fig)
    else:
        print("Error")


def HistogramPlt(image):
    if os.path.isfile(image):
        image = opencv.imread(image, opencv.IMREAD_GRAYSCALE)
        plt.hist(image.ravel(), 256, [0, 256])
        plt.show()
    else:
        print("Error!")


ShowImageOriginal(img)
HistogramPlt(img)

opencv.waitKey(0)
opencv.destroyAllWindows()
