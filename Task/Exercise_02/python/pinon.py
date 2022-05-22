# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:47:14 2022

@author: Mario Salazar
"""


import cv2 as opencv
import numpy as numpy
from Artificial_Intelligence.functions import mario_functions as mario

img = "../img/pinon.png"

# Read image
im_in = opencv.imread(img, opencv.IMREAD_UNCHANGED)
output = opencv.resize(im_in, (480, 350))
gray = mario.GrayImageIMREAD_GRAYSCALE(img)

# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
ret, threshold = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY | opencv.THRESH_OTSU)
th, im_th = opencv.threshold(gray, int(ret), 255, opencv.THRESH_BINARY_INV)
print(ret)
# Copy the threshold image.
im_floodfill = im_th.copy()
# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
height, weight = im_th.shape[:2]
mask = numpy.zeros((height + 2, weight + 2), numpy.uint8)

# Floodfill from point (0, 0)0
a = opencv.floodFill(im_floodfill, mask, (0, 0), 255)

# Invert flood filled image
im_floodfill_inv = opencv.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
circle = im_th | ~im_floodfill_inv
outline, jerarq = opencv.findContours(im_th, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
cnt = outline[len(outline) - 1]
M = opencv.moments(cnt)
x, y, weight, height = opencv.boundingRect(cnt)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print("({:},{:})".format(cx, cy))
byte = numpy.uint8
matriz = 255 * numpy.ones((len(im_out), len(im_out[0]), 3), byte)
circle_matriz1 = opencv.circle(circle, (cx, cy), int(height / 2) - 25, (0, 0, 255), -1)
circle_matriz2 = opencv.circle(im_th, (cx, cy), int(height / 2) - 25, (0, 0, 255), -1)

_, td = opencv.threshold(gray, int(ret) + 50, 255, opencv.THRESH_BINARY_INV)
conts, j = opencv.findContours(circle_matriz2, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
# circle_center = opencv.circle(im_out, (cx, cy), 1, (255, 255, 255), -1)
# opencv.putText(im_out, " (" + str(cx) + "," + str(cy) + ")", (cx, cy), 1, 1, (255, 255, 255), 1)
opencv.drawContours(circle_matriz2, conts, 0, (255, 255, 0), -1)

# opencv.rectangle(im_out, (x, y), (x+weight, y+height), (234, 26, 127), 1)

# Display images.

output1 = opencv.resize(im_out, (480, 350))
mario.ShowImageMorphology(output1, "A")
output2 = opencv.resize(~circle_matriz1, (480, 350))
mario.ShowImageMorphology(output2, "B")
output3 = opencv.resize(circle_matriz2, (480, 350))
mario.ShowImageMorphology(output3, "C")
mario.ShowImageMorphology(output, "D")

print("Numero de dientes del piñon: {:}".format(len(conts)))

opencv.waitKey(0)
opencv.destroyAllWindows()
