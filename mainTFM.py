#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:09:02 2023

@author: marceloh
"""

import streamlit as st
import pandas as pd

def origen():
    # Agrega un componente para seleccionar el archivo
    file = st.file_uploader("Seleccionar archivo", type=["csv", "xlsx"])
    if file:
        st.write(file)
        # Lee el archivo seleccionado
        df = pd.read_csv(file) if file.name.endswith('csv') else pd.read_excel(file)
        tipos = explorar(df)
        return tipos

def explorar(data):
    df_types = pd.DataFrame(data.dtypes, 
                            columns=['Data Type'])
    numerical_cols = df_types[~df_types['Data Type'].isin(['object',
                   'bool'])].index.values
    df_types['Count'] = data.count()
    df_types['Unique Values'] = data.nunique()
    df_types['Min'] = data[numerical_cols].min()
    df_types['Max'] = data[numerical_cols].max()
    df_types['Average'] = data[numerical_cols].mean()
    df_types['Median'] = data[numerical_cols].median()
    df_types['St.Dev.'] = data[numerical_cols].std()
    df_types['Omitir'] = False
    return df_types.astype(str)        

# Crear el menú de tipo sidebar
st.sidebar.header('Menú ETL. Barómetro Social')

# Definir las opciones del menú
opciones = ['Origen de datos', 'Resumen', 'Limpieza', 'Transformar', 'Exportar']

# Agregar el menú desplegable al menú de la barra lateral
#opcion_seleccionada = st.sidebar.selectbox('Selecciona una opción', opciones)

# Agregar las opciones al menú
opcion1 = st.sidebar.button(opciones[0])
opcion2 = st.sidebar.button(opciones[1])
opcion3 = st.sidebar.button(opciones[2])
opcion4 = st.sidebar.button(opciones[3])
opcion5 = st.sidebar.button(opciones[4])

# Mostrar contenido según la opción seleccionada
if opcion1:
    st.write('Origen de datos')
    file = origen()
        #st.table(df)

elif opcion2:
    st.write('Resumen')
    # Agregar aquí los componentes o secciones correspondientes a la Opción 2
elif opcion3:
    st.write('Limpieza')
    # Agregar aquí los componentes o secciones correspondientes a la Opción 3
elif opcion4:
    st.write('Transformar')
elif opcion5:
    st.write('Exportar')
