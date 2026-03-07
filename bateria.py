import streamlit as st

def simulador_bateria():

    st.header("Simulador de batería de producción")

    pozos = st.number_input("Cantidad de pozos",1,50,10)

    produccion_total = 0

    for i in range(pozos):

        prod = st.slider(f"Producción pozo {i+1}",0.0,100.0,20.0)
        produccion_total += prod

    st.write("Producción total batería")

    st.success(f"{produccion_total} m3/d")

    corte_agua = st.slider("Corte de agua (%)",0,100,70)

    petroleo = produccion_total*(1-corte_agua/100)

    st.write("Producción de petróleo")

    st.success(f"{petroleo:.2f} m3/d")
