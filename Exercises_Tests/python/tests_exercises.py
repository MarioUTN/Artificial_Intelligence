# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:40:57 2022

@author: Mario Salazar
"""


import cv2 as opencv
import numpy as numpy
import os as os
import  skimage.morphology as mo
import scipy.ndimage as ndi

# Count Objects
from numba import prange

byte = numpy.uint8 # class

vector_low_yellow = numpy.array([20, 100, 20], byte)
vector_tall_yellow = numpy.array([32, 255, 255], byte)

vector_low_green = numpy.array([36, 100, 20], byte)
vector_tall_green = numpy.array([70, 255, 255], byte)


#print(image)

# Method to show an original image
def ShowImageOriginal(image):
    if os.path.isfile(image):
        vector_image = opencv.imread(image)
        opencv.imshow("Original Image {:} - ".format(image), vector_image)
    else:
        print("No image found!")

# Method to remove objects from an image and show the image with the objects not removed
def ShowObjectsByColour(image, colour_low, color_tall):
    if os.path.isfile(image):
        vector_image = opencv.imread(image)
        image_HSV = opencv.cvtColor(vector_image,opencv.COLOR_BGR2HSV)
        mask_colour = opencv.inRange(image_HSV, colour_low,color_tall)
        opencv.imshow("Image",mask_colour)
    else:
        print("Error")

# Method to count objects
def CountObjects(image,colour_low, color_tall):
    if os.path.isfile(image):
        vector_image = opencv.imread(image)
        image_HSV = opencv.cvtColor(vector_image,opencv.COLOR_BGR2HSV)
        mask_colour = opencv.inRange(image_HSV,colour_low,color_tall)
        outine_colour = opencv.findContours(mask_colour,opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
        coount = 0
        for i in enumerate(outine_colour):
            coount+=1
        return coount
    else:
        print("Error to Count")

# Method dilatation of an Image
def ErodeImage(image):
    if os.path.isfile(image):
        img = opencv.imread(image)
        kernel = numpy.ones((5,5),byte)
        img_erosion = opencv.erode(img, kernel, iterations=1)
        opencv.imshow("Erode Image", img_erosion)

# Method of dilate an Image
def DilatationImage(image):
    if os.path.isfile(image):
        img = opencv.imread(image)
        kernel = numpy.ones((5, 5), byte)
        img_erosion = opencv.dilate(img, kernel, iterations=1)
        opencv.imshow("Dilatation Image", img_erosion)
    else:
        print("Error of Image")

# Extrate circles of an image
def ExtrateColour(image):
    if os.path.isfile(image):
        img = opencv.imread(image)
        (b, g, r) = img[495, 85]
        return numpy.array([r, g, b])
    else:
        print("Error de Imagen")

def Binarizacion(image):
    if os.path.isfile(image):
        img = opencv.imread(image)
        imgGray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
        opencv.imshow("Original", img)
        opencv.imshow("Gray Image", imgGray)
        umbral = 85
        mask = numpy.uint8((imgGray < umbral)*255)
        opencv.imshow("Mask", mask)
    else:
        print("Error de image")


img_python = "../img/Python.jpg"
img_circles = "../img/circulos.png"
img_cat = "../img/gato.jpg"

# print(ExtrateColour(img_cat))



# ShowImageOriginal(img_python)
Binarizacion(img_cat)
# ShowObjectsByColour(image, vector_low_green, vector_tall_green)
# print(CountObjects(image, vector_low_green, vector_tall_green))

#ErodeImage(img_python)
#DilatationImage(img_python)

opencv.waitKey(0)
opencv.destroyAllWindows()

