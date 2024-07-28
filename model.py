import pandas as pd
import numpy as np


df = pd.read_csv('iris.csv')
df['Class'].value_counts()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Class'] = le.fit_transform(df['Class'])
df.head()

#Model Training
from sklearn.model_selection import train_test_split
# train - 70
# test - 30
X = df.drop(columns=['Class'])
Y = df['Class']
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)


from sklearn.tree import DecisionTreeClassifier
def training_model():
    model = DecisionTreeClassifier()
    trained_model = model.fit(x_train, y_train)
    return trained_model
