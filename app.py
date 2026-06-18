import streamlit as st
import streamlit.components.v1 as components
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="La Web de JUAN", layout="centered")

st.title("🧩 La Web de JUAN")

# --- LÓGICA DE ESTADO ---
if 'score_final' not in st.session_state: st.session_state.score_final = 0
if 'juego_terminado' not in st.session_state: st.session_state.juego_terminado = False

# --- PESTAÑAS PARA ORGANIZAR ---
tab1, tab2 = st.tabs(["🧩 Sopa de Letras", "🕹️ Runner de Juan"])

with tab1:
    st.header("Sopa de Letras")
    st.write("Aquí iría tu código de la sopa de letras.")

with tab2:
    st.subheader("🕹️ ¡Competición: El Runner de JUAN!")
    
    # --- SELECTOR DE JUGADOR (Aparece al perder) ---
    if st.session_state.juego_terminado:
        st.warning(f"¡Has perdido con {st.session_state.score_final} puntos! Registra tu marca:")
        nombre_elegido = st.selectbox("Selecciona tu nombre:", 
                                      ["Sierra", "Joaquín", "Ejkar", "Vecina", "Telenti", "Miguel Ángel", "Mírete", "Juan"])
        if st.button("Guardar Puntuación"):
            st.success(f"¡Marca de {nombre_elegido} guardada con {st.session_state.score_final} puntos!")
            st.session_state.juego_terminado = False
            st.rerun()

    # --- CARGA DEL JUEGO DESDE ARCHIVO EXTERNO ---
    def cargar_juego():
        with open("juego.txt", "r", encoding="utf-8") as f:
            return f.read()

    components.html(cargar_juego(), height=300)
