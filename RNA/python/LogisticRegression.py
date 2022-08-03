"""
Regresión Logística

@author: ligdigonzalez
"""

########## LIBRERÍAS A UTILIZAR ##########

#Se importan la librerias a utilizar
from sklearn import datasets

########## PREPARAR LA DATA ##########

#Importamos los datos de la misma librería de scikit-learn
dataset = datasets.load_breast_cancer()
#print(dataset)



########## ENTENDIMIENTO DE LA DATA ##########

#Verifico la información contenida en el dataset
#print('Información en el dataset:')
#print(dataset.keys())
#print()

#Verifico las características del dataset
#print('Características del dataset:')
#print(dataset.DESCR)

#Seleccionamos todas las columnas
X = dataset.data

#Defino los datos correspondientes a las etiquetas
y = dataset.target

print(y)

########## IMPLEMENTACIÓN DE REGRESIÓN LOGÍSTICA ##########


from sklearn.model_selection import train_test_split



#Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Se escalan todos los datos
from sklearn.preprocessing import StandardScaler
escalar = StandardScaler()
X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)

#Defino el algoritmo a utilizar
from sklearn.linear_model import LogisticRegression
algoritmo = LogisticRegression()

#Entreno el modelo
algoritmo.fit(X_train, y_train)

#Realizo una predicción
y_pred = algoritmo.predict(X_test)



#Verifico la matriz de Confusión
from sklearn.metrics import confusion_matrix
import seaborn as sns
matriz = confusion_matrix(y_test, y_pred)
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("confusion matrix: \n", cm)
plt.figure(figsize = (8,4))
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Prediction', fontsize = 12)
plt.ylabel('Real', fontsize = 12)
plt.show()



#Calculo la precisión del modelo
from sklearn.metrics import precision_score
precision = precision_score(y_test, y_pred)
print('Precisión del modelo:')
print(precision)

#Calculo la exactitud del modelo
from sklearn.metrics import accuracy_score
exactitud = accuracy_score(y_test, y_pred)
print('Exactitud del modelo:')
print(exactitud)

from sklearn.metrics import recall_score
espe = recall_score(y_test, y_pred, pos_label=0)
print("especificidad: ", espe)



#Calculo la sensibilidad del modelo
from sklearn.metrics import recall_score

sensibilidad = recall_score(y_test, y_pred)
print('Sensibilidad del modelo:')
print(sensibilidad)

#Calculo el Puntaje F1 del modelo
from sklearn.metrics import f1_score
puntajef1 = f1_score(y_test, y_pred)
print('Puntaje F1 del modelo:')
print(puntajef1)

#Calculo la curva ROC - AUC del modelo
from sklearn.metrics import roc_auc_score

roc_auc = roc_auc_score(y_test, y_pred)
print('Curva ROC - AUC del modelo:')
print(roc_auc)


from sklearn.metrics import roc_curve
#plt.figure()
lw = 2
plt.plot(roc_curve(y_test, y_pred)[0], roc_curve(y_test, y_pred)[1], color='darkorange',lw=lw, label='ROC curve (area = %0.2f)' %roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()


print('Precisión del modelo:', precision)
print('Exactitud del modelo:', exactitud)
print('Sensibilidad del modelo:', sensibilidad)
print('Puntaje F1 del modelo:', puntajef1)
print('Curva ROC - AUC del modelo:', roc_auc)


