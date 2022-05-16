# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:23:57 2022

@author: Mario Salazar
"""

import cv2 as opencv
import numpy as numpy
import matplotlib.pyplot as plt

img = opencv.imread("pieza-1.png")

gray = opencv.cvtColor(img, opencv.COLOR_BGR2GRAY)
ret, th = opencv.threshold(gray, 122, 255, opencv.THRESH_BINARY)

img2 = th.copy()

h, w = img2.shape

mask = numpy.zeros((h + 2, w + 2), numpy.uint8)
opencv.floodFill(img2, mask, (0, 0), 255)

inv = opencv.bitwise_not(img2)

sin_huecos = th | inv

contours, hierarchy = opencv.findContours(th, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_NONE)
cnt = opencv.convexHull(contours[0])
angle = opencv.minAreaRect(cnt)[-1] - 90
print("Actually angle is:" + str(angle))

(h, w) = img.shape[:2]
print(h, w)
center = (w // 2, h // 2)
print(center)
M = opencv.getRotationMatrix2D(center, angle, 1.0)
rotated = opencv.warpAffine(th, M, (w, h), flags=opencv.INTER_CUBIC, borderMode=opencv.BORDER_REPLICATE)

imgs = [img, th, sin_huecos, rotated]
t = ['Original', 'Binary', 'Filled', 'Rotation: {:.2f}'.format(angle)]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(opencv.cvtColor(imgs[i], opencv.COLOR_BGR2RGB), vmin=0, vmax=255)
    plt.title(t[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# opencv.imshow("1", img)
# opencv.imshow("3", rotated)
# opencv.imshow("4", th)
# opencv.imshow("5", no gaps)

opencv.waitKey(0)
opencv.destroyAllWindows()
