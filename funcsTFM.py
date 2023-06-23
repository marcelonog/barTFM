import streamlit as st
#import pandas as pd
import csv

def origen():
    # Agrega un componente para seleccionar el archivo
    file = st.file_uploader('Explorar', type=["csv", "xlsx"])
    return file


def explorar(file):
    """ 
    df_types = pd.DataFrame(data.dtypes, 
                            columns=['Tipo Dato'])
    numerical_cols = df_types[~df_types['Tipo Dato'].isin(['object',
                'bool'])].index.values

    df_types['Count'] = data.count()
    df_types['Valores Unicos'] = data.nunique()
    df_types['Min'] = data[numerical_cols].min()
    df_types['Máx'] = data[numerical_cols].max()
    df_types['Promedio'] = data[numerical_cols].mean()
    df_types['Mediana'] = data[numerical_cols].median()
    df_types['Dev.Std.'] = data[numerical_cols].std()
    df_types = pd.DataFrame(data)
    return df_types.astype(str)
    """    
    line_count = 0
    if file:
        # Lee el archivo seleccionado
        # df = pd.read_csv(file) if file.name.endswith('csv') else pd.read_excel(file)
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if line_count == 0:
                    st.write(f'Nombres de Columna {", ".join(row)}')
                else:
                    st.write(f'Columna 0 \t{row[0]} columna 1 {row[1]}, columna 2 {row[2]}.')
                line_count += 1
            st.write(line_count)
        return df


explorar(origen())