# recorredor-simulador
simular_opera_campoç

pip install -r requirements.txt
streamlit run app.py
pip install -r requirements.txt
streamlit run app.py
import streamlit as st

st.title("SIMULADOR OPERATIVO MENFA")

presion = st.slider("Presión de pozo",0,100,20)
nivel = st.slider("Nivel dinámico",0,2000,800)

produccion = (2000-nivel)*0.03

st.write("Producción estimada:",produccion,"m3/d")
streamlit
numpy
pandas
matplotlib
plotly
fpdf

menfa_simulator/

app.py
pozos.py
bateria.py
bombeo_mecanico.py
esp.py
pcp.py
produccion.py
requirements.txt
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication
simulador.py
ModuleNotFoundError: No module named 'PyQt6'
