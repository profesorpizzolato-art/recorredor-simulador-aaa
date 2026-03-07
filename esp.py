import streamlit as st

def simulador_esp():

    st.header("Simulador Bombeo Electrosumergible")

    nivel = st.number_input("Nivel dinámico (m)",0,3000,1500)
    friccion = st.number_input("Pérdidas fricción (m)",0,200,70)
    boca = st.number_input("Presión boca pozo (m)",0,200,100)

    tdh = nivel + friccion + boca

    st.success(f"TDH = {tdh} m")

    altura_etapa = st.number_input("Altura por etapa (m)",1.0,10.0,4.4)

    etapas = tdh/altura_etapa

    st.success(f"Número de etapas requerido: {int(etapas)}")
