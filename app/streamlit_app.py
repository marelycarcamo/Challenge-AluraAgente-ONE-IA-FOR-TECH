"""
Archivo:
    streamlit_app.py

Módulo:
    Aplicación Streamlit.

Objetivo:
    Proporcionar una interfaz conversacional para interactuar
    con el agente RAG.

Descripción:
    Este módulo representa la capa de presentación de la aplicación.
    Su responsabilidad es configurar Streamlit, cargar recursos
    visuales y conectar la interfaz con el servicio del agente.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres.
"""


import streamlit as st

from app.bootstrap import load_agent_service
from app.components.chat import render_chat
from app.config import (
    APP_DESCRIPTION,
    APP_ICON,
    APP_NAME,
    LOGO_PATH,
)


st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="centered",
)


# -----------------------------
# Identidad visual
# -----------------------------

if LOGO_PATH.exists():
    st.image(
        str(LOGO_PATH),
        width=180,
    )

st.title(APP_NAME)

st.write(APP_DESCRIPTION)

st.divider()


# -----------------------------
# Inicialización del servicio
# -----------------------------

@st.cache_resource
def get_agent_service():
    """
    Carga el servicio principal de la aplicación.

    Streamlit mantiene una única instancia en memoria para evitar
    reconstruir los modelos del pipeline RAG en cada interacción.
    """

    return load_agent_service()


agent_service = get_agent_service()


# -----------------------------
# Interfaz conversacional
# -----------------------------

render_chat(
    agent_service=agent_service,
)