# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:47:14 2022

@author: Mario Salazar
"""


import cv2 as opencv
import numpy as numpy


def ShowMatriz(matrix):
    resp = ""
    for rows in range(len(matrix)):
        for column in range(len(matrix[0])):
            resp = resp + str(matrix[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


img = "../img/pinon.png"

# Read image
im_in = opencv.imread(img)
im_in1 = opencv.imread(img, 0)
gray = opencv.imread(img, opencv.IMREAD_GRAYSCALE)
# Threshold.
# Set values equal to or above 220 to 0.
# Set values below 220 to 255.
ret, threshold = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY | opencv.THRESH_OTSU)
th, im_th = opencv.threshold(gray, int(ret) + 50, 255, opencv.THRESH_BINARY_INV)
print(ret)
# Copy the threshold image.
im_floodfill = im_th.copy()

# Mask used to flood filling.
# Notice the size needs to be 2 pixels than the image.
h, w = im_th.shape[:2]
mask = numpy.zeros((h + 2, w + 2), numpy.uint8)

# Floodfill from point (0, 0)0
a = opencv.floodFill(im_floodfill, mask, (0, 0), 255)

# Invert flood filled image
im_floodfill_inv = opencv.bitwise_not(im_floodfill)

# Combine the two images to get the foreground.
im_out = im_th | im_floodfill_inv
outline, jerarq = opencv.findContours(im_th, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
cnt = outline[len(outline) - 1]
M = opencv.moments(cnt)
x, y, w, h = opencv.boundingRect(cnt)
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
print("({:},{:})".format(cx, cy))
byte = numpy.uint8
matriz = 255 * numpy.ones((len(im_out), len(im_out[0]), 3), byte)
circle_matriz = opencv.circle(im_out, (cx, cy), int(h / 2) - 20, (0, 0, 255), -1)

_, td = opencv.threshold(gray, int(ret) + 50, 255, opencv.THRESH_BINARY_INV)
conts, j = opencv.findContours(circle_matriz, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
# circle_center = opencv.circle(im_out, (cx, cy), 1, (255, 255, 255), -1)
# opencv.putText(im_out, " (" + str(cx) + "," + str(cy) + ")", (cx, cy), 1, 1, (255, 255, 255), 1)

opencv.drawContours(im_in, conts, -1, (255, 255, 0), 5)

i = 0
for c in conts:
    i += 1
print(i-1)



def Count(object, count):
    mask = opencv.findContours(object, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
    print(mask)
    for i in enumerate(mask):
        count += 1
    return count


# opencv.rectangle(im_out, (x, y), (x+w, y+h), (234, 26, 127), 1)

# Display images.
#opencv.imshow("Original Image", im_in)
#opencv.imshow("Threshold Image", im_th)
#opencv.imshow("Flood-filled Image", im_floodfill)
opencv.imshow("Inverted Flood-filled Image", im_floodfill_inv)

opencv.imshow("Foreground", im_out)
opencv.waitKey(0)
opencv.destroyAllWindows()
