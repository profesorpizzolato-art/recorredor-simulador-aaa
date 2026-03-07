import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def simulador_bombeo():

    st.header("Simulador Bombeo Mecánico")

    carrera = st.slider("Carrera pulgadas",50,200,144)
    spm = st.slider("Golpes por minuto",1,20,10)
    diametro = st.slider("Diámetro pistón pulgadas",1,4,2)

    area = 3.1416*(diametro/2)**2

    produccion = area*carrera*spm*0.0001

    st.success(f"Producción estimada {produccion:.2f} m3/d")

    x = np.linspace(0,100,100)
    y = np.sin(x/10)*1000

    fig,ax=plt.subplots()

    ax.plot(x,y)

    ax.set_title("Carta Dinamométrica")

    st.pyplot(fig)
