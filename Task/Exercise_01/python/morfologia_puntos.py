# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:41:57 2022

@author: Mario Salazar
"""

"""
backup
respaldos
duplicados
No d 6 7 8  : xw2wSCMNN7Zsn%p   25:02 
"""
"""


Display name
appregmarioutn
Application (client) ID
66961e75-214b-422d-9faa-2625daa84f1a
Object ID
a3e87240-5dc5-4536-bdfd-42fddc919fdb
Directory (tenant) ID
8dbe1469-c79c-4e21-9d43-ca65d9e9c475

secret id = 9fe4fcaa-b315-4c18-97a4-45901fafea6e

"""
# Today email: kA!mR6UZzdwyjb2  Heroku: qd-ArFr2PR2cTh)UA&/vqv3N6bf(U2  
# Git: VwXR#maXtOq*!)W^LS&yF|ZgZcCEyE   username: gitmario10salazarutn
# Netlify: jrdvqR/3u6Ou)Auc0Q$lbt1Bq$k-HG   username: netlifymario10salazar
# bitwarden: ImlbWhlnN/v1tfL9Z/1o39/Tyg-mc|     master_optional: %&J|Lr9|BQSwyaFU75!T$RfeAdiH!t
# Azure: ZLU9S!1!b-QroTu7&83SqL@E8|ye-Y
# DB : marioutn 346@$#njmAhT2097&*%##WCEVEWVGRCEU
# prtgadmin
# marioutn  password-dbwath

# M@r!0Sal@z@R_10-r!0Sal@z@R
# M@r!0Sal@z@R_10guefwvcwawjtctywec61dxbjvc
# gmail update: M@r!0Sal@z@R_10guefwvcwawjtctywec61dxbjvc
# BXbhvHeubrfe3363746bd 2u@#$&%vxhdcw
# in: kHTnv5^589%bbgBHC46h25@#!
# utn: Huyu7074
# UTN NEW PASSWORD: 346@$#njmAhT2097&*%##WCEVEWVGRCEU
# SIIU UTN: 25J2@M@R!object1234
# SIIU UEM: 25J2@M@R!object1235
# https://www.sqlshack.com/es/tecnicas-de-optimizacion-de-consultas-en-sql-server-consejos-y-trucos-de-aplicacion/
# https://www.amazon.com/Samsung-Galaxy-A325F-DS-Factory-Unlocked/dp/B08X6RR3T1/ref=sr_1_7?crid=373T8Z7ZH7P6A&keywords=samsung+a31&qid=1654890276&sprefix=samsung+a31%2Caps%2C191&sr=8-7
# https://sale.alibaba.com/p/rank/detail/index.html?spm=a27aq.21715648a27aq.6382395180.3.38682d67MXatVO&cardType=101001165&cardId=103000003457502&topOfferIds=1600484017571&templateBusinessCode=rank-new-functions
# auditoria: https://www.globalsuitesolutions.com/es/auditoria-interna-sgsi-basado-iso-27001/
# https://books.google.com.ec/books?id=9irSCgAAQBAJ&lpg=PA300&dq=strel%20python&pg=PA14#v=onepage&q=strel%20python&f=false
import cv2 as opencv
import numpy as numpy
import functions as f


file = "../img/morfologia.jpeg"
image = f.ReadImage(file)

f.ShowImageOriginal(file)
matrix = f.MatrixZeros(10, 10)
det = f.DetectCircle(file, 2)
f.ShowImageMorphology(det, "M")
print("Numero de puntos: {:}".format(f.Count(det, 0)))

"""
def ShowMatriz(matriz):
    resp = ""
    for rows in range(len(matriz)):
        for column in range(len(matriz[0])):
            resp = resp + str(matriz[rows][column]) + "\t"
        resp = resp + "\n"
    return resp


img_python = "../img/morfologia.jpeg"
image = opencv.imread(img_python)
opencv.imshow("Original Image", image)
gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)

thresh = opencv.threshold(gray, 0, 255, opencv.THRESH_BINARY + opencv.THRESH_OTSU)[1]  # Matriz binary original

byte = numpy.uint8
matriz = numpy.zeros((8, 8), byte)

circle_matriz = opencv.circle(matriz, (4, 4), 2, (255, 0, 0), 1)

print(ShowMatriz(circle_matriz))
detected_circle = opencv.morphologyEx(thresh, opencv.MORPH_OPEN, circle_matriz,iterations=2)
opencv.imshow("U", detected_circle)
# Matriz of lines found
circle_found = opencv.findContours(detected_circle, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)

#   print(ShowMatriz(detected_circle))

circle_found = circle_found[0] if len(circle_found) == 2 else circle_found[1]
for c in circle_found:
    a =opencv.drawContours(image, [c], -1, (255, 255, 255), 2)
    print(a)


def Count(lines_found, count):
    mask = opencv.findContours(lines_found, opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)[0]
    for index in enumerate(mask):
        count += 1
    return count


print(Count(detected_circle, 0))
opencv.imshow("Image Circle", detected_circle)
"""
opencv.waitKey(0)
opencv.destroyAllWindows()


