# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:14:15 2022

@author: Mario Salazar
"""


"""
import cv2 as opencv
import numpy as numpy
from matplotlib import pyplot as plt

image = i = "../img/imagen_line.jpeg"

img = opencv.imread(image)
u, th1 = opencv.threshold(img, 127, 255, opencv.THRESH_BINARY)
u, th2 = opencv.threshold(img, 127, 255, opencv.THRESH_BINARY_INV)
u, th3 = opencv.threshold(img, 127, 255, opencv.THRESH_TRUNC)
# u, th4 = opencv.threshold(img, 127, 255, opencv.THRESH_TOZERO)
# u, th5 = opencv.threshold(img, 127, 255, opencv.THRESH_TOZERO_INV)

images = [img, th1, th2, th3]
tittle = ['Image Original', 'Image Binary', 'Image Binary_INV', 'Image Trunk']

for i in range(len(images)):
    plt.subplot(3, 2, i + 1)
    plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(tittle[i])
    plt.xticks([]), plt.yticks([])

plt.show()
print(u)

"""
import numpy as np
import cv2


def main():

    # 1. Crea una imagen de fondo blanco
    d = 400
    img = np.ones((d, d, 3), np.uint8) * 255

    # 2. Establece el punto central de la elipse, el eje mayor y menor
    center = (round(d/2), round(d/2))
    size = (100, 200)

    # 2. Dibuja una elipse en un bucle
    for i in range(0, 10):

        # Ángulo aleatorio, ancho de línea
        angle = np.random.randint(0, 361)
        thickness = np.random.randint(1, 9)

        # Color aleatorio
        color = np.random.randint(0, high=256, size=(3,)).tolist()

        # Dibuja una elipse
        cv2.ellipse(img, center, size, angle, 0, 360, color, thickness)

    # 3. Muestra el resultado
    cv2.imshow("img", img)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

