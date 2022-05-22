# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:45:38 2022

@author: Mario Salazar
"""
import cv2 as opencv

capture = opencv.VideoCapture("../img/mejores_goles.mp4")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        opencv.imshow("gato0", frame)
        if opencv.waitKey(30) == ord('s'):
            break
    else:
        break

capture.release()
opencv.waitKey(0)
opencv.destroyAllWindows()
