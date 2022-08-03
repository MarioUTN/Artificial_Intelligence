# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:38:27 2022

@author: Mario Salazar
"""

import cv2 as opencv
import matplotlib.pyplot as plt
import functions as f

file = "../img/imagen_line.jpeg"

image = f.ReadImage(file)
erode = f.Erode(file, 2, 2)
canny = f.Canny(file, 100, 200)
canny_az = f.CannyApertureSize(file, 100, 200)
canny_l2gradient = f.CannyL2Gradient(file, 100, 200)
canny_l2gradient_az = f.CannyL2Gradient(file, 100, 200)

mi = [image, erode, canny, canny_az, canny_l2gradient, canny_l2gradient_az]
titles = ['Original', 'Erode', 'Canny', 'canny_az', 'canny_l2gradient', 'canny_l2gradient_az']

f.ShowImageMorphology(erode, "Erode")
f.ShowImageMorphology(canny, "Canny")
f.ShowImageMorphology(canny_az, "Aperture")
f.ShowImageMorphology(canny_l2gradient, "L2Gradient")
f.ShowImageMorphology(canny_l2gradient_az, "L2Gradient")
f.ShowImageOriginal(file)
# f.ShowImagesPlot(mi, titles)
plt.show()
opencv.waitKey(0)
opencv.destroyAllWindows()
