import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import pandas as pd
import sys

bcdata = pd.read_csv('wdbc2.data.csv')
data = bcdata.values
entrada = data[:, 1:31]
salida = data[:, 0]

# cargamos los datos
training_data = np.array(entrada, "float32")

# ground truth
target_data = np.array(salida, "float32")

model = Sequential()
model.add(Dense(30, input_dim=30, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # you don't can change

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['binary_accuracy'])

model.fit(training_data, target_data, epochs=100)  # epochs

# evaluamos el modelo
scores = model.evaluate(training_data, target_data)
print("\%s: %.4f" % (model.metrics_names[0], scores[0]))  # loss
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))  # accuracy

# Metrics
y_true = target_data
y_pred = model.predict(training_data).round()

# Matriz de confusión:
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
cm = confusion_matrix(y_true, y_pred)
print("confusion matrix: \n", cm)
# gráfica cm
plt.figure(figsize=(8, 4))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Prediction', fontsize=12)
plt.ylabel('Real', fontsize=12)
plt.show()

# Exactitud:
from sklearn.metrics import accuracy_score
acc = accuracy_score(y_true, y_pred)
print("accuracy: ", acc)

# Sensibilidad:
from sklearn.metrics import recall_score

recall = recall_score(y_true, y_pred)
print("recall: ", recall)

# Especificidad
from sklearn.metrics import recall_score

espe = recall_score(y_true, y_pred, pos_label=0)
print("especificidad: ", espe)

# Precisión:
from sklearn.metrics import precision_score

precision = precision_score(y_true, y_pred)
print("precision: ", precision)

# Puntuación F1:
from sklearn.metrics import f1_score

f1 = f1_score(y_true, y_pred)
print("f1 score: ", f1)

# Área bajo la curva:
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(y_true, y_pred)
print("auc: ", auc)

# Curva ROC
from sklearn.metrics import roc_curve

plt.figure()
lw = 2
plt.plot(roc_curve(y_true, y_pred)[0], roc_curve(y_true, y_pred)[1], color='darkorange', lw=lw,
         label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# R Score (R^2 coefficient of determination)
from sklearn.metrics import r2_score

R = r2_score(y_true, y_pred)
print("R: ", R)

sys.exit(0)

# serializar el modelo a JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serializar los pesos a HDF5
model.save_weights("model.h5")
print("Modelo Guardado!")

# cargar json y crear el modelo
from keras.models import model_from_json

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# cargar pesos al nuevo modelo
loaded_model.load_weights("model.h5")
print("Cargado modelo desde disco.")

# Compilar modelo cargado y listo para usar.
loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
