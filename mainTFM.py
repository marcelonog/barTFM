#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:09:02 2023

@author: marceloh
"""

import streamlit as st
import pandas as pd
import json
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from funcsTFM import origen, explorar


st.header("ETL")
# Crear el menú de tipo sidebar

st.sidebar.header('Procesos del ETL')

# Definir las opciones del menú
opciones = ['Extraer', 'Transformar', 'Cargar']

# Agregar el menú desplegable al menú de la barra lateral
proceso = st.sidebar.radio(label="Opciones", options=opciones)


# Mostrar contenido según la opción seleccionada
extraer = False
if proceso == 'Extraer':
    #Buscar fuente de datos
    extraer = origen()
    # Configuración de la grilla
    if extraer:
        # Opciones de visualización
        ver_opcs = ['Tabla', 'Estadísticas', 'Agrupación']
        visualizar = st.radio(label="Visualizar:", options=ver_opcs)
        dfX = explorar(extraer)
        gb = GridOptionsBuilder.from_dataframe(dfX)
        gb.configure_pagination(enabled=True,paginationPageSize=30)
        gb.configure_default_column(editable=True, groupable=True, filterable=True,)    
        #gd.configure_selection(selection_mode='multiple',use_checkbox=True)
        gridOptions = gb.build() 
        column_defs = gridOptions["columnDefs"]
        for col_def in column_defs:
            col_name = col_def["field"]
            max_len = dfX[col_name].astype(str).str.len().max() # can add +5 here if things are too tight
            col_def["width"] = max_len+120
        grid_table = AgGrid(dfX, gridOptions=gridOptions, 
                            update_mode=GridUpdateMode.SELECTION_CHANGED, 
                            height=900, allow_unsafe_jscode=True, 
                            theme='balham') # alpine, balham, material
elif proceso == 'Transformar':
    st.write('Transformar')
elif proceso == 'Cargar':
    st.write('Cargar')
