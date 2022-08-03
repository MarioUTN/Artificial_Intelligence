# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:14:53 2022

@author: HP
"""

import numpy as np
from keras import models
from keras.layers.core import Dense
from sklearn import preprocessing
import pandas as pd


"""Cargar el dataset"""
admissions = pd.read_excel('banknote.xlsx')
datos = admissions.values
entrada = datos[:,0:4] 
salida = datos[:,4]
 

training_data = np.array(entrada, "float32")

"""Normalizando los datos con el metodo/min_max_scaler"""
from sklearn import preprocessing
#returns a numpy array
#min_max_scaler = preprocessing.MinMaxScaler()
#x_scaled = min_max_scaler.fit_transform(training_data)
#training_data = pd.DataFrame(training_data)
#training_data


"""Normalizando los datos con StandarScaler"""
training_data = preprocessing.StandardScaler().fit_transform(training_data)
training_data = pd.DataFrame(training_data)
training_data
# ground truth
target_data = np.array(salida, "float32")
"""Entrenamos el modelo"""
from sklearn.model_selection import train_test_split
X_train,X_test, y_train,y_test = train_test_split(training_data,target_data,test_size=0.2,random_state=0)

"""RED NEURONAL"""
model = models.Sequential() 
model.add(Dense(25, activation='relu', input_dim=4))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
modelo=model.fit(training_data, target_data, epochs=20, batch_size=8, validation_split=0.25) 
 

"""Evaluando el modelo train y test"""

print("Evaluación del modelo test")
scores_test = model.evaluate(X_test, y_test)
print("\%s: %.4f" % (model.metrics_names[0], scores_test[0])) # loss
print("\n%s: %.2f%%" % (model.metrics_names[1], scores_test[1]*100)) # accuracy

print("Evaluación del modelo training")
scores = model.evaluate(training_data,target_data)
print("\%s: %.4f" % (model.metrics_names[0], scores[0])) # loss
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) # accuracy

test_loss, test_accuracy = model.evaluate(X_test, y_test)

print("Exactitud del Entrenmiento", test_accuracy)
print("Perdida del Entrenmiento", test_loss)



"""full metrics"""
y_pred = model.predict(training_data).round()
y_true = target_data

"""Matriz de confusión"""
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
print("Matriz de confusion:")
print(cm)
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (8,4))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Prediction', fontsize = 12)
plt.ylabel('Real', fontsize = 12)
plt.show()


"""Exactitud:"""
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_true, y_pred)
print('acc:', acc)

"""Sensibilidad:"""
from sklearn.metrics import recall_score
rec = recall_score(y_true, y_pred)
print('recall:', rec)

"""Precisión:"""
from sklearn.metrics import precision_score
prec = precision_score(y_true, y_pred)
print('precision:', prec)

"""Puntuación F1:"""
from sklearn.metrics import f1_score
f1 = f1_score(y_true, y_pred)
print('F1:', f1)

"""Área bajo la curva:"""
from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_true, y_pred)
print('AUC:', auc)

""" R Score:(R^2 coefficient of determination)"""
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
print('R2:', r2)

"""Curva ROC"""
from sklearn.metrics import roc_curve
lw = 2
plt.plot(roc_curve(y_true, y_pred)[0], roc_curve(y_true, y_pred)[1], 
         color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

#--------------------------------GRAFICAS---------------------------------------
"""Graficas de Training y Test  epocas /accuracy"""

acc = modelo.history['accuracy']
val_acc  = modelo.history['val_accuracy']
loss     = modelo.history['loss']
val_loss = modelo.history['val_loss']
epochs   = range(1,len(acc)+1,1)
plt.plot ( epochs,     acc, 'r--', label='Training Exactitud'  )
plt.plot ( epochs, val_acc,  'b', label='Validation Exactitud')
plt.title ('Training  y Validation Exactitud')
plt.ylabel('Accuracy')
plt.xlabel('epocs')
plt.legend()
plt.figure()

"""Entrenamiento epocas /perdida"""
plt.plot ( epochs,     loss, 'r--',label='Perdida' )
plt.plot ( epochs, val_loss ,  'b' , label='Validation Perdida')
plt.title ('Training y Validation Perdida '   )
plt.ylabel('Loss') # corregir por perdida
plt.xlabel('epocs')
plt.legend()
plt.figure()
plt.show()
