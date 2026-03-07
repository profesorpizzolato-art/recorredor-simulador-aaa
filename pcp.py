import streamlit as st

def simulador_pcp():

    st.header("Simulador Bombeo PCP")

    viscosidad = st.slider("Viscosidad cP",1,5000,200)
    profundidad = st.slider("Profundidad bomba (m)",100,2000,800)

    capacidad = 100 - profundidad*0.02

    if viscosidad > 1000:
        capacidad *= 0.7

    st.success(f"Capacidad estimada {capacidad:.2f} m3/d")
