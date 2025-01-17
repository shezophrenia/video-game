# -*- coding: utf-8 -*-
"""Video Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i00ORwZroXXuMSMNq6rNpjLlAAEskFgf
"""

import numpy as np #linear algebro
import pandas as pd #data proccessing ,csv file i/o (e,g, pd read_csv)
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("vgsales.csv")
print(df)
#using labelencoder convert categorical data into numerical data

df.info()

df.shape

number = LabelEncoder()

df['Platform']=number.fit_transform(df['Platform'].astype('str'))
df['Genre']=number.fit_transform(df['Genre'].astype('str'))
df['Publisher']=number.fit_transform(df['Publisher'].astype('str'))

dff=df.drop(['Rank','Name','Year'],axis=1)
df3=dff.drop(['NA_Sales','EU_Sales','JP_Sales','Other_Sales'],axis=1)  #columns=["Platform","Genre","Publisher"]
                                                  #columns=["Platform","Genre","Publisher",'NA_Sales','EU_Sales']

columns=["Platform","Genre","Publisher",'NA_Sales','EU_Sales']

labels = df3['Global_Sales'].values
features =dff[list(columns)].values

X = features
Y = labels
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.30)
scaler = StandardScaler()
#scaler =processing.MinMaxScaler()

#fit only on traning data

scaler.fit(X_train)

X_train = scaler.transform(X_train)

#apply same transformation

X_test = scaler.transform(X_test)

regr = linear_model.LinearRegression()

regr.fit(X_train , Y_train)

Accuracy = regr.score(X_train , Y_train)

print("LinearRegression Accuracy in the traning data:" ,Accuracy * 100,"%")

from sklearn.ensemble import GradientBoostingRegressor

M = GradientBoostingRegressor()

M.fit(X_train , Y_train)

Accuracy = M.score(X_train , Y_train)

print("GradientBoostingRegressor Accuracy in the traning data:", Accuracy *100 , "%")

Accuracy = M.score(X_test , Y_test)

print("GradientBoostingRegressor Accuracy in the test data:", Accuracy *100 , "%")

from sklearn.svm import SVR

M4 = SVR()

M4.fit(X_train, Y_train)

Accuracy = M4.score(X_train , Y_train)

print("Support Vector Regression Accuracy in the traning data :" , Accuracy * 100, "%")

Accuracy = M4.score(X_test , Y_test)

print("Support Vector Regression Accuracy in the test data :" , Accuracy * 100, "%")

from sklearn.neighbors import KNeighborsRegressor
M5 = KNeighborsRegressor()

M5.fit(X_train , Y_train)

Accuracy = M5.score(X_train , Y_train)

print("KNeighborsRegressor Accuracy in the traning data :",Accuracy *100 , "%")

Accuracy = M5.score(X_test , Y_test)

print("KNeighborsRegressor Accuracy in the test data :",Accuracy *100 , "%")

print(X_train)

print(X_test)

print(Y_train)

print(Y_test)

"""**Deep Learning**

"""

from tensorflow.keras.models import Sequential # Changed 'sequential' to 'Sequential'
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

model = Sequential()

model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(19, activation='relu'))
model.add(Dense(1))

import numpy as np

# Generate random data for demonstration
X_train = np.random.rand(100, 10)  # 100 samples with 10 features
Y_train = np.random.rand(100)      # 100 target values
X_test = np.random.rand(20, 10)    # 20 test samples with 10 features
Y_test = np.random.rand(20)       # 20 test target values

model.compile(optimizer='adam', loss='mse')
model.fit(x=X_train, y=Y_train,
          validation_data=(X_test, Y_test),
          batch_size=128, epochs=200)

losses = pd.DataFrame(model.history.history)
losses.plot()
plt.show()

from sklearn.metrics import mean_squared_error, mean_absolute_error,explained_variance_score,r2_score

pradictions = model.predict(X_test)

print("Deep Learning:")
print(mean_absolute_error(Y_test,pradictions))
print(np.sqrt(mean_squared_error(Y_test,pradictions)))
print(explained_variance_score(Y_test,pradictions))
print(r2_score(Y_test,pradictions))

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Input # Import Input layer this way
from tensorflow.keras import metrics # Import the 'metrics' module

# Example of how to use Input layer
# input_layer = Input(shape=(10,))

model2 = Sequential()
model2.add(Dense(32,activation='relu'))
model2.add(Dense(64,activation='relu'))
model2.add(Dense(128,activation='relu'))
model2.add(Dropout(0.2))
model2.add(Dense(1))
model2.compile(optimizer=Adam(0.001),loss='mse',metrics=[metrics.mae])

r = model2.fit(X_train,Y_train,validation_data=(X_test,Y_test),batch_size=128,epochs=500)

losses = pd.DataFrame(model2.history.history)
losses.plot()
plt.show()

predictions = model2.predict(X_test)
print("Deep Learning:")
print(mean_absolute_error(Y_test,predictions))
print(np.sqrt(mean_squared_error(Y_test,predictions)))
print(explained_variance_score(Y_test,predictions))
print(r2_score(Y_test,predictions))

