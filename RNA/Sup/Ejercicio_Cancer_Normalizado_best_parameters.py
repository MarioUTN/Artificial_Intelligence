# https://machinelearningmastery.com/grid-search-hyperparameters-deep-learning-models-python-keras/

import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
import pandas as pd
from sklearn import preprocessing


admissions = pd.read_excel('banknote.xlsx')
datos = admissions.values

# Escalado de datos
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,1)) # [0,1]
datos_scaled = min_max_scaler.fit_transform(datos)


entrada = datos_scaled[:,0:4]  # 30 columnas (1-30)
salida = datos_scaled[:,4] # primera columna (0)

 
# cargamos los datos (variables predictoras)
training_data = np.array(entrada, "float32")

# ground truth
target_data = np.array(salida, "float32")

 
 # GridSearchCV
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier
from keras.optimizers import Adam

def create_model(neurons=10, learn_rate=0.01):
    model = Sequential()
    model.add(Dense(neurons, activation='relu', input_dim=30))
    model.add(Dense(1, activation='sigmoid'))
    opt = Adam(learning_rate=learn_rate)
    
    model.compile(loss='binary_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    return model


optimizers = ('rmsprop', 'adam', 'SDG') # as a tupla (), not a list []
epochs = [5, 10]
batches = [8, 16]
lr=[0.01, 0.001]
neurons = [5, 10, 15]
# momentum=[0.9, 0.99]

# These new arguments must also be defined in the signature of your create_model() function with default parameters.
# parameters = dict(optimizer=optimizers, nb_epoch=epochs,...
parameters = dict(nb_epoch=epochs, batch_size=batches, learn_rate=lr, neurons=neurons)
model = KerasClassifier(build_fn=create_model)
# The GridSearchCV process will then construct and evaluate one model for each combination of parameters. 
# n_jobs=-1 to parallelize, but it can freeze or hang the laptop
clf = GridSearchCV(estimator=model, param_grid=parameters, scoring='accuracy', n_jobs=1, cv=5)
clf = clf.fit(training_data, target_data)
print("\nbest parameters:")
print("Acc: ", clf.best_score_) # accuracy
print(clf.best_params_)