import streamlit as st

# Constante de los gases ideales
R = 0.0821  # atm·L/mol·K

st.title("Calculadora de Gases Ideales y Ley de Boyle-Mariotte")
st.write("Selecciona la ley que deseas usar para hacer el cálculo:")

# Botones para seleccionar la ley
ley = st.radio("Selecciona una ley", ["Ecuación de Gases Ideales", "Ley de Boyle y Mariotte"])

# Función para formatear los resultados
def mostrar_resultado(valor, unidad):
    st.success(f"**Resultado: {round(valor, 4)} {unidad}**")

# Ecuación de Gases Ideales
if ley == "Ecuación de Gases Ideales":
    st.write("Usamos la fórmula: **PV = nRT**")
    opcion = st.selectbox("Variable a calcular", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

    if opcion == "Presión (P)":
        volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
        temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.4f")
        moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")

        if st.button("Calcular Presión"):
            if volumen > 0:
                presion = (moles * R * temperatura) / volumen
                mostrar_resultado(presion, "atm")
            else:
                st.error("El volumen debe ser mayor que 0.")

    elif opcion == "Volumen (V)":
        presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
        temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.4f")
        moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")

        if st.button("Calcular Volumen"):
            if presion > 0:
                volumen = (moles * R * temperatura) / presion
                mostrar_resultado(volumen, "L")
            else:
                st.error("La presión debe ser mayor que 0.")

    elif opcion == "Temperatura (T)":
        presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
        volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
        moles = st.number_input("Número de moles (mol)", min_value=0.0, format="%.4f")

        if st.button("Calcular Temperatura"):
            if moles > 0:
                temperatura = (presion * volumen) / (moles * R)
                mostrar_resultado(temperatura, "K")
            else:
                st.error("Los moles deben ser mayores que 0.")

    elif opcion == "Número de moles (n)":
        presion = st.number_input("Presión (atm)", min_value=0.0, format="%.4f")
        volumen = st.number_input("Volumen (L)", min_value=0.0, format="%.4f")
        temperatura = st.number_input("Temperatura (K)", min_value=0.0, format="%.4f")

        if st.button("Calcular moles"):
            if temperatura > 0:
                moles = (presion * volumen) / (R * temperatura)
                mostrar_resultado(moles, "mol")
            else:
                st.error("La temperatura debe ser mayor que 0.")

# Ley de Boyle y Mariotte
elif ley == "Ley de Boyle y Mariotte":
    st.write("Usamos la fórmula: **P1 * V1 = P2 * V2**")
    
    opcion_boyle = st.selectbox("¿Qué deseas calcular?", ["Volumen final (V2)", "Presión final (P2)"])

    if opcion_boyle == "Volumen final (V2)":
        P1 = st.number_input("Presión inicial (P1) [atm]", min_value=0.0, format="%.4f")
        V1 = st.number_input("Volumen inicial (V1) [L]", min_value=0.0, format="%.4f")
        P2 = st.number_input("Presión final (P2) [atm]", min_value=0.0, format="%.4f")
        
        if st.button("Calcular Volumen Final (V2)"):
            if P1 > 0 and P2 > 0:
                V2_calculado = (P1 * V1) / P2
                mostrar_resultado(V2_calculado, "L")
            else:
                st.error("Las presiones deben ser mayores que 0.")

    elif opcion_boyle == "Presión final (P2)":
        P1 = st.number_input("Presión inicial (P1) [atm]", min_value=0.0, format="%.4f")
        V1 = st.number_input("Volumen inicial (V1) [L]", min_value=0.0, format="%.4f")
        V2 = st.number_input("Volumen final (V2) [L]", min_value=0.0, format="%.4f")
        
        if st.button("Calcular Presión Final (P2)"):
            if V1 > 0 and V2 > 0:
                P2_calculado = (P1 * V1) / V2
                mostrar_resultado(P2_calculado, "atm")
            else:
                st.error("Los volúmenes deben ser mayores que 0.")
