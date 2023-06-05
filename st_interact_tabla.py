import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

#Funciones
@st.cache_resource #data
def data_upload():
    df = pd.read_csv("nombres.csv")
    return df

#st.header("Este es el Dataframe de Streamlit por defecto")
df = data_upload()
#st.dataframe(data=df)
#st.info(len(df))

_funct = st.sidebar.radio(label="Funciones", options=['Mostrar', 'Destacar','Eliminar'])

st.header("Esta en una tabla AgGrid")

gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)

if _funct == 'Mostrar':
    sel_mode = st.radio('Tipo de Seleccion', options=['single', 'multiple'])
    gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
    gridOptions = gd.build()
    grid_table = AgGrid(df, gridOptions=gridOptions, 
                        update_mode=GridUpdateMode.SELECTION_CHANGED, height=500,
                        allow_unsafe_jscode=True, 
                        theme='balham') # alpine, balham, material

    sel_fila = grid_table["selected_rows"]
    st.subheader("Salida")
    st.write(sel_fila)

if _funct == 'Destacar':
    col_opc = st.selectbox(label='Seleccionar columna', options=df.columns)
    cellstyle_jscode = JsCode("""
        function(params){
            if (params.value == 'Tom') {
                return {
                    'color':'black',
                    'backgroundColor':'orange'
                }
            }
            if (params.value == 'Lisa'){
                return{
                    'color':'black',
                    'backgroundColor':'red'
                }
            }
            else{
                return{
                    'color':'black',
                    'backgroundColor':'lightpink'
                }
            }
        };
    """)

    gd.configure_columns(col_opc, cellStyle = cellstyle_jscode)
    gridOptions = gd.build()
    grid_table = AgGrid(df, 
                        gridOptions = gridOptions,
                        enable_enterprise_modules=True,
                        fit_columns_on_grid_load=True,
                        height=500,
                        width='100%',
                        theme="balham",
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        reload_data=True,
                        allow_unsafe_jscode=True,
                        )
    
if _funct == 'Eliminar':
    js = JsCode("""
            function(e) {
                let api = e.api;
                let sel = api.getSelectedRows();
                api.applyTransaction({remove: sel})
            };
        """
        )
    gd.configure_selection('single', use_checkbox=True)
    gd.configure_grid_options(onRowSelected=js, pre_selected_rows=[])
    gridOptions = gd.build()
    grid_table = AgGrid(df, 
                    gridOptions = gridOptions,
                    enable_enterprise_modules=True,
                    fit_columns_on_grid_load=True,
                    height=500,
                    width='100%',
                    theme="balham",
                    update_mode=GridUpdateMode.SELECTION_CHANGED,
                    reload_data=True,
                    allow_unsafe_jscode=True,
                    )
st.balloons()
st.info('Total Filas :' + str(len(grid_table['data'])))
