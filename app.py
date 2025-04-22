import streamlit as st
st.image("Captura de pantalla 2025-04-22 124140.png")
st.set_page_config(page_title="Leyes de los Gases", page_icon="🧪")

st.title("🧪 Calculadora de Leyes de Gases")
st.write("Selecciona una ley para realizar el cálculo de variables según las condiciones del gas.")
st.caption("ℹ️ Nota: Las temperaturas deben estar en Kelvin (K), no en °C. Los valores deben ser mayores que cero.")

# Función para mostrar el resultado
def mostrar_resultado(valor, unidad):
    st.success(f"🔍 **Resultado:** {round(valor, 4)} {unidad}")

# Ley seleccionada
ley = st.radio("📚 Elige una ley", [
    "Ley de Boyle y Mariotte",
    "Ley de Charles",
    "Ley de Gay-Lussac"
])

# ========== LEY DE BOYLE ==========
if ley == "Ley de Boyle y Mariotte":
    st.subheader("🧮 P₁ × V₁ = P₂ × V₂  (Temperatura constante)")
    st.info("La presión y el volumen de un gas son inversamente proporcionales si la temperatura es constante.")

    opcion = st.selectbox("¿Qué deseas calcular?", ["Volumen final (V₂)", "Presión final (P₂)"])

    col1, col2, col3 = st.columns(3)
    with col1:
        P1 = st.number_input("Presión inicial (P₁) [atm]", min_value=0.01)
    with col2:
        V1 = st.number_input("Volumen inicial (V₁) [L]", min_value=0.01)
    with col3:
        if opcion == "Volumen final (V₂)":
            P2 = st.number_input("Presión final (P₂) [atm]", min_value=0.01)
        else:
            V2 = st.number_input("Volumen final (V₂) [L]", min_value=0.01)

    if st.button("Calcular"):
        if opcion == "Volumen final (V₂)":
            V2 = (P1 * V1) / P2
            mostrar_resultado(V2, "L")
        else:
            P2 = (P1 * V1) / V2
            mostrar_resultado(P2, "atm")

# ========== LEY DE CHARLES ==========
elif ley == "Ley de Charles":
    st.subheader("📏 V₁ / T₁ = V₂ / T₂  (Presión constante)")
    st.info("El volumen de un gas es directamente proporcional a su temperatura absoluta si la presión es constante.")

    opcion = st.selectbox("¿Qué deseas calcular?", ["Volumen final (V₂)", "Temperatura final (T₂)"])

    col1, col2, col3 = st.columns(3)
    with col1:
        V1 = st.number_input("Volumen inicial (V₁) [L]", min_value=0.01)
    with col2:
        T1 = st.number_input("Temperatura inicial (T₁) [K]", min_value=0.01)
    with col3:
        if opcion == "Volumen final (V₂)":
            T2 = st.number_input("Temperatura final (T₂) [K]", min_value=0.01)
        else:
            V2 = st.number_input("Volumen final (V₂) [L]", min_value=0.01)

    if st.button("Calcular"):
        if opcion == "Volumen final (V₂)":
            V2 = (V1 * T2) / T1
            mostrar_resultado(V2, "L")
        else:
            T2 = (V2 * T1) / V1
            mostrar_resultado(T2, "K")

# ========== LEY DE GAY-LUSSAC ==========
elif ley == "Ley de Gay-Lussac":
    st.subheader("🌡️ P₁ / T₁ = P₂ / T₂  (Volumen constante)")
    st.info("La presión de un gas es directamente proporcional a su temperatura absoluta si el volumen es constante.")

    opcion = st.selectbox("¿Qué deseas calcular?", ["Presión final (P₂)", "Temperatura final (T₂)"])

    col1, col2, col3 = st.columns(3)
    with col1:
        P1 = st.number_input("Presión inicial (P₁) [atm]", min_value=0.01)
    with col2:
        T1 = st.number_input("Temperatura inicial (T₁) [K]", min_value=0.01)
    with col3:
        if opcion == "Presión final (P₂)":
            T2 = st.number_input("Temperatura final (T₂) [K]", min_value=0.01)
        else:
            P2 = st.number_input("Presión final (P₂) [atm]", min_value=0.01)

    if st.button("Calcular"):
        if opcion == "Presión final (P₂)":
            P2 = (P1 * T2) / T1
            mostrar_resultado(P2, "atm")
        else:
            T2 = (P2 * T1) / P1
            mostrar_resultado(T2, "K")
