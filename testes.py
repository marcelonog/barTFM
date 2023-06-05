# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def apply_classification_algorithm(file_path, target_column):
    # Lee el archivo CSV o XLSX
    # extension = file_path.split('.')[-1]
    #if extension == 'csv':
    #    df = pd.read_csv(file_path)
    #elif extension == 'xlsx':
    #    df = pd.read_excel(file_path)
    #else:
    #    raise ValueError("Formato de archivo no válido. Debe ser CSV o XLSX.")

    # Aplica el árbol de clasificación
    y_test, y_pred = apply_decision_tree(df, target_column)

    # Visualiza los resultados
    visualize_classification_results(y_test, y_pred)

def apply_decision_tree(df, target_column):
    # Separa las características y la columna objetivo
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Divide los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crea y ajusta el modelo de árbol de clasificación
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Calcula las predicciones
    y_pred = model.predict(X_test)

    return y_test, y_pred

def visualize_classification_results(y_test, y_pred):
    # Calcula la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    st.write("Precisión del modelo: {:.2f}%".format(accuracy * 100))

    # Crea una matriz de confusión
    cm = confusion_matrix(y_test, y_pred)

    # Visualiza la matriz de confusión
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    st.pyplot()

# Configuración de la página de Streamlit
st.set_page_config(page_title="Selección de archivo")

# Agrega un componente para seleccionar el archivo
file = st.file_uploader("Seleccionar archivo", type=["csv", "xlsx"])

if file:
    # Lee el archivo seleccionado
    df = pd.read_csv(file) if file.name.endswith('csv') else pd.read_excel(file)

    # Solicita al usuario ingresar el nombre de la columna objetivo
    target_column = st.text_input("Ingrese el nombre de la columna objetivo")

    # Verifica si se ha ingresado el nombre de la columna objetivo
    if target_column:
        # Aplica el algoritmo de clasificación
        apply_classification_algorithm(df, target_column)
