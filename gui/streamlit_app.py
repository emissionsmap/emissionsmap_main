from tkinter.tix import COLUMN
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu
from consultas import consultas2
import os 
import xlrd
import openpyxl
import pickle
from pathlib import Path


with st.sidebar:
    choose = option_menu("Galeria", ["Consulta", "Diccionario"],
                        icons=['house', "house"],
                        menu_icon="app-indicator", default_index=0,
                        styles={
        "container": {"padding": "8!important", "background-color": "#202022"},
        "icon": {"color": "#00747C", "font-size": "15px"}, 
        "nav-link": {"font-size": "18px", "text-align": "down", "margin":"0px", "--hover-color": "#363333"},
        "nav-link-selected": {"background-color": "#579DFF"},
    }
    )

if choose == "Consulta":
    text = st.text_area("Consulta SQL")

    if st.button("consultar"):
        df = consultas2(text)
        if type(df) == type(pd.DataFrame()):
            st.table(df.head())
            df = df.to_csv().encode("utf-8")
            st.download_button("Descargar", data=df, file_name="tabla.csv", mime="text/csv")
        else:
            st.error(df)


if choose == "Diccionario":
    text = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"
    algo = consultas2(text)
    df = pd.DataFrame(algo)
    df = list(df["tablename"])
    box = st.selectbox("Elegir Tabla",df)
    tabla = pd.read_csv("archivos/Dict solo formato.csv", delimiter=";", encoding="utf-8")
    for e in df:
        if box == e:
            try:
                nom = e + ".csv"
                cons = 'select * from public."{}"'.format(e)
                data = consultas2(cons)
                data = data.to_csv().encode("utf-8")
                dicc = tabla[tabla["Entidad"] == e]
                st.write(dicc)
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button("Descargar tabla", data=data, file_name=nom, mime="text/csv")
                with col2:
                    dicc = dicc.to_csv().encode("utf-8")
                    st.download_button("Descargar diccionario", data=dicc, file_name="Dicc" + nom, mime="text/csv")
                #st.write(data)
            except Exception as ex:
                st.write(ex)
    
      
