# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 13:33:53 2022

@author: Mario Salazar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# En Python Extraer datos de diferentes fuentes:

a = pd.read_csv("mystery.csv", encoding='utf-16', sep=',', header=0)

b = pd.read_csv('electricity_access_percent.csv', encoding='utf-8', sep=',')

c = pd.read_csv('gdp_data.csv', encoding='utf-8', sep=',')

d = pd.read_csv('population_data.csv', encoding='utf-8', sep=',')

e = pd.read_csv('projects_data.csv', encoding='utf-8', sep=',', index_col=False, dtype='unicode')

f = pd.read_csv('rural_population_percent.csv', encoding='utf-8', sep=',', index_col=False, dtype='unicode')

g = pd.read_json('population_data.json', encoding='utf-8', dtype='unicode')

#print(g)

a.plot(kind='scatter', x='1960', y='1961', color='red')
plt.show()


# Transformar datos en Python. concat = rural_population_percent.csv, electricity_access_percent.csv

ca = pd.read_csv('rural_population_percent.csv', encoding='utf-8', sep=',', index_col=False, dtype='unicode')
cb = pd.read_csv('electricity_access_percent.csv', encoding='utf-8', sep=',')

con = pd.concat([ca, cb]).drop_duplicates()
con.fillna('Ecuador')
#print(con)

dates=['April-10', 'April-11', 'April-12', 'April-13']
fruits=['Apple', 'Papaya', 'Banana', 'Mango']
prices=[3, 1, 2, 4]

df = pd.DataFrame({'Date':dates ,
                   'Fruit':fruits ,
                   'Price': prices})



import random
from datetime import datetime

inicio = datetime(2017, 1, 30)
final =  datetime(2017, 5, 28)

random_date = inicio + (final - inicio) * random.random()

print(random_date)
print(df)
df.insert(3, "Fecha", random_date, allow_duplicates=False)

print(df)

dt_int = pd.date_range(random_date, periods=5, freq='D')
print(dt_int)

df['F']= pd.date_range(random_date, periods=4, freq='D')
print(df)
print(len(df))