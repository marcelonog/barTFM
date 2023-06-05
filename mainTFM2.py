#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:09:02 2023

@author: marceloh
"""

#import streamlit as st
#st.set_page_config(layout="wide")
import pandas as pd

def origen():
    # Agrega un componente para seleccionar el archivo
#    file = st.file_uploader("Seleccionar archivo", type=["csv", "xlsx"])
    file ='barDic2019.csv'
    if file:
        #st.write(file)
        # Lee el archivo seleccionado
        #df = pd.read_csv(file) if file.name.endswith('csv') else pd.read_excel(file)
        df = pd.read_csv(file)
        return df

#@st.cache_data
def explorar(data):
    df_types = pd.DataFrame(data.dtypes, 
                            columns=['Data Type'])
    numerical_cols = df_types[~df_types['Data Type'].isin(['object',
                   'bool'])].index.values
    df_types['Count'] = data.count()
    df_types['Unique Values'] = data.nunique()
    df_types['Min'] = data[numerical_cols].min()
    df_types['Max'] = data[numerical_cols].max()
    #df_types['Average'] = data[numerical_cols].mean()
    #df_types['Median'] = data[numerical_cols].median()
    #df_types['St.Dev.'] = data[numerical_cols].std()
   # df_types['Omitir'] = False
    
    return df_types.astype(str)       

# Crear el menú de tipo sidebar
#st.sidebar.header('Menú ETL. Barómetro Social')
#st.header('Menú ETL. Barómetro Social')
# Definir las opciones del menú

# Mostrar contenido según la opción seleccionada
#st.write('Origen de datos')
#st.dataframe(tipos) #, use_container_width=True)
#st.experimental_data_editor(origen())

df = origen()
tipos = explorar(df)
print(tipos)