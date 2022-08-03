# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 07:02:06 2022

@author: Mario Salazar
"""


# https://www.aprendemachinelearning.com/una-sencilla-red-neuronal-en-python-con-keras-y-tensorflow/ 


# libraries
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import sys
 
# cargamos las 4 combinaciones de las compuertas XOR
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
 
# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[0],[1],[1],[0]], "float32") # ground truth

# arquitectura de la red 
model = Sequential() # feed-forward
model.add(Dense(10, input_dim=2, activation='relu')) # input (2) and hidden (10) layers
# model.add(Dense(5, activation='relu')) # other hidden layer
model.add(Dense(1, activation='sigmoid')) # output layer
model.summary()
 
model.compile(loss='mean_squared_error',    # loss function
              optimizer='adam',             # optimization algorithm
              metrics=['binary_accuracy'])  # metric

# training process 
model.fit(training_data, target_data, epochs=100)

# Recuperamos bias and weights de la capa oculta
weights_HL, biases_HL = model.layers[0].get_weights()
# Recuperamos bias and weights de la capa de salida
weights_OL, biases_OL = model.layers[1].get_weights()
 
# evaluamos el modelo
scores = model.evaluate(training_data, target_data)
print("\n%s: %.4f" % (model.metrics_names[0], scores[0])) # loss
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) # accuracy

# predecimos con las posibles entradas (ejemplo trivial)
print (model.predict(training_data)) # con decimales
print (model.predict(training_data).round()) # enteros

sys.exit(0)


# una vez entrenada la red puede guardar en disco y luego cargar (sin entrenar nuevamente) para usarla.
# vea el archivo "save_load_net.py"
model_json = model.to_json()
with open("model.json", "w") as json_file: # *.jeson --> metadatos, etiquetas
    json_file.write(model_json)
# serializar los pesos a HDF5
model.save_weights("model.h5") # *.h5 --> pesos
print("Modelo Guardado!")
 
# mas tarde... deployment
 
# cargar json y crear el modelo
from keras.models import model_from_json
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# cargar pesos al nuevo modelo
loaded_model.load_weights("model.h5")
print("Cargado modelo desde disco.")
 
# Compilar modelo cargado y listo para usar usando los mismos parámetros.
loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])

# predecir usando el modelo cargado
print(loaded_model.predict(training_data).round()) # en enteros





