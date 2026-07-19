"""
Archivo:
    streamlit_app.py

Módulo:
    app

Objetivo:
    Inicializar la aplicación Streamlit de ALESSIA.

Descripción:
    Este módulo constituye el punto de entrada de la aplicación.
    Se encarga de configurar la interfaz, cargar los recursos
    necesarios para ejecutar el pipeline RAG e inicializar el
    servicio de aplicación.

    La lógica conversacional es delegada al componente chat.py,
    mientras que el procesamiento de las consultas es responsabilidad
    de AgentService.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""

"""
Archivo:
    streamlit_app.py

Módulo:
    app

Objetivo:
    Inicializar la aplicación Streamlit de ALESSIA.

Descripción:
    Este módulo constituye el punto de entrada de la aplicación.
    Se encarga de configurar la interfaz, cargar el servicio de
    aplicación y renderizar la interfaz conversacional.

    La lógica del pipeline RAG se encuentra encapsulada en
    AgentService.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""
"""
Archivo:
    streamlit_app.py

Módulo:
    app

Objetivo:
    Inicializar la aplicación Streamlit de ALESSIA.

Descripción:
    Este módulo constituye el punto de entrada de la aplicación.
    Se encarga de configurar la interfaz, cargar el servicio de
    aplicación y renderizar la interfaz conversacional.

    La lógica del pipeline RAG se encuentra encapsulada en
    AgentService.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""

import streamlit as st

st.cache_resource.clear()

from app.components.chat import render_chat
from app.config import (
    APP_DESCRIPTION,
    APP_ICON,
    APP_NAME,
    LOGO_PATH,
)
from src.services.agent_service import AgentService


st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="centered",
)


@st.cache_resource
def load_agent_service() -> AgentService:
    """
    Inicializa el servicio de aplicación.

    Returns
    -------
    AgentService
        Instancia del servicio utilizada por la aplicación.
    """
    return AgentService.create()


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

agent_service = load_agent_service()


# -----------------------------
# Interfaz conversacional
# -----------------------------

render_chat(
    agent_service=agent_service,
)