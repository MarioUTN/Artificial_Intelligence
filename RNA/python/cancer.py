# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 08:01:41 2022

@author: Mario Salazar
"""
import pandas as pd
import numpy as np
import functions as function

bcdata = pd.read_csv('../matlab/wdbc2.data.csv')
bcdata = np.array(bcdata)
bcdata = bcdata.transpose()
target = bcdata[:1]
indata = bcdata[1:]
#print(function.ShowMatriz(indata))


def Min_Max(matrix):
    matriz_minmax = np.zeros((len(matrix), 2))
    for fila in range(len(matrix)):
        matriz_minmax[fila][0] = min(matrix[fila])
        matriz_minmax[fila][1] = max(matrix[fila])
    return matriz_minmax



matriz_minmax = Min_Max(indata)

