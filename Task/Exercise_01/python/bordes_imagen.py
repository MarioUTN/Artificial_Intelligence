# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:38:27 2022

@author: Mario Salazar
"""

import cv2 as opencv
import matplotlib.pyplot as plt
from Artificial_Intelligence.functions import mario_functions as mario

file = "../img/imagen_line.jpeg"

image = mario.ReadImage(file)
erode = mario.Erode(file, 2, 2)
canny = mario.Canny(file, 100, 200)
canny_az = mario.CannyApertureSize(file, 100, 200)
canny_l2gradient = mario.CannyL2Gradient(file, 100, 200)
canny_l2gradient_az = mario.CannyL2Gradient(file, 100, 200)

mi = [image, erode, canny, canny_az, canny_l2gradient, canny_l2gradient_az]
titles = ['Original', 'Erode', 'Canny', 'canny_az', 'canny_l2gradient', 'canny_l2gradient_az']

mario.ShowImageMorphology(erode, "Erode")
mario.ShowImageMorphology(canny, "Canny")
mario.ShowImageMorphology(canny_az, "Aperture")
mario.ShowImageMorphology(canny_l2gradient, "L2Gradient")
mario.ShowImageMorphology(canny_l2gradient_az, "L2Gradient")
mario.ShowImageOriginal(file)
# mario.ShowImagesPlot(mi, titles)
plt.show()
opencv.waitKey(0)
opencv.destroyAllWindows()
