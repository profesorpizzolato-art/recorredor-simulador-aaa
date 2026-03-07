import streamlit as st

def calculo_produccion():

    st.header("Cálculo producción en tanque control")

    nivel_inicial = st.number_input("Nivel inicial cm",0.0,200.0,20.0)
    nivel_final = st.number_input("Nivel final cm",0.0,200.0,170.0)

    coeficiente = st.number_input("Coeficiente tanque m3/cm",0.0,1.0,0.64)

    if st.button("Calcular"):

        volumen = (nivel_final - nivel_inicial) * coeficiente

        st.success(f"Producción ensayo: {volumen:.2f} m3")
