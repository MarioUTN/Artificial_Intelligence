# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:45:38 2022

@author: Mario Salazar
"""
# import the opencv library

import cv2 as opencv
import functions as f

file =  "../img/morfologia.jpeg"

# image = opencv.imread(file)
# opencv.imshow("Imagen", image)

f.ShowImageOriginal(file)
opencv.waitKey(0)
opencv.destroyAllWindows()