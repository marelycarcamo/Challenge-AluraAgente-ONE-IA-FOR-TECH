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

Punto de entrada de la aplicación Streamlit.

Responsable de:
- Configurar la interfaz principal.
- Cargar los recursos visuales.
- Inicializar el servicio de aplicación.
- Renderizar la interfaz conversacional.
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


from app.bootstrap import load_agent_service
import streamlit as st

from app.bootstrap import load_agent_service
from app.components.chat import render_chat
from app.config import (
    APP_DESCRIPTION,
    APP_ICON,
    APP_NAME,
    # ALESSIA_AVATAR_PATH,
    # USER_AVATAR_PATH,
    LOGO_PATH,
    AVATAR_PATH
)


# --------------------------------------------------
# Configuración de la aplicación
# --------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
)

# --------------------------------------------------
# Barra lateral
# --------------------------------------------------

with st.sidebar:

    if LOGO_PATH.exists():
        st.image(
            str(LOGO_PATH),
            use_container_width=True,
        )
    
    if AVATAR_PATH.exists():
        st.image(
            str(AVATAR_PATH),
            use_container_width=True,
        )   
        st.markdown(APP_DESCRIPTION)
# --------------------------------------------------
# Inicializar servicio
# --------------------------------------------------

agent_service = load_agent_service()

# --------------------------------------------------
# Interfaz conversacional
# --------------------------------------------------

render_chat(
    agent_service=agent_service,
)