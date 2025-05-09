# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pC5tSt7jlHYamV7yqnLYusXpPJzf-0ka
"""

# @title
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Train a Logistic Regression model (Softmax)
X = df[iris.feature_names]
y = df['species']
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)
model.fit(X, y)

# Streamlit app
st.title("🌸 Iris Flower Classification (Logistic Softmax) 🌸")
st.write("Predict the species of an iris flower based on its features.")

# User inputs
sepal_length = st.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))


# Predict species
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(features)[0]
prediction_proba = model.predict_proba(features)

st.write(f"### Predicted Species: **{prediction.capitalize()}**")
st.write("### Prediction Probabilities:")
st.write(f"Setosa: {prediction_proba[0][0]:.2f}, Versicolor: {prediction_proba[0][1]:.2f}, Virginica: {prediction_proba[0][2]:.2f}")

st.write("#### About the App:")
st.write("This app uses Multinomial Logistic Regression (Softmax) trained on the Iris dataset to classify iris flowers into three species: Setosa, Versicolor, and Virginica.")

st.write("Made by Sharad 😀")

