"""
Archivo:
    chat.py

Módulo:
    components

Objetivo:
    Gestionar la interfaz conversacional de la aplicación Streamlit.

Descripción:
    Este módulo contiene los componentes visuales relacionados con la
    interacción entre el usuario y el asistente.

    Su responsabilidad es administrar el historial de conversación,
    capturar preguntas del usuario y mostrar las respuestas generadas
    por AgentService.

    Este componente no contiene lógica del pipeline RAG. La recuperación
    de información, reranking y generación de respuestas son delegados
    al servicio de aplicación.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""

"""
Componente encargado de renderizar la interfaz conversacional
de ALESSIA.
"""

import streamlit as st

from app.config import (
    ALESSIA_AVATAR_PATH,
    USER_AVATAR_PATH,
)


def render_chat(agent_service):
    """
    Renderiza la interfaz conversacional y procesa
    las consultas del usuario.

    Parameters
    ----------
    agent_service :
        Servicio encargado de ejecutar el pipeline RAG.

    Returns
    -------
    None
    """

    # Inicializar historial de conversación.
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "¡Hola, vecino! 👋\n\n"
                    "Soy **ALESSIA**, tu asistente especializada en "
                    "gestión del riesgo de desastres para la comuna de Valdivia.\n\n"
                    "Puedo ayudarte a consultar información oficial sobre "
                    "planes comunales, amenazas, emergencias, zonas de riesgo "
                    "y medidas de preparación.\n\n"
                    "¿En qué puedo ayudarte hoy?"
                ),
            }
        ]
        
    # Mostrar historial existente.
    for message in st.session_state.messages:

        avatar = (
            str(ALESSIA_AVATAR_PATH)
            if message["role"] == "assistant"
            else str(USER_AVATAR_PATH)
        )

        with st.chat_message(
            message["role"],
            avatar=avatar,
        ):
            st.write(
                message["content"]
            )

    # Capturar nueva consulta.
    question = st.chat_input(
        "Escribe tu consulta..."
    )

    if question:

        # Guardar mensaje del usuario.
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        # Mostrar mensaje del usuario.
        with st.chat_message(
            "user",
            avatar=str(USER_AVATAR_PATH),
        ):
            st.write(question)

        # Ejecutar el pipeline RAG.
        with st.spinner(
            "ALESSIA está analizando la información oficial..."
        ):
            answer = agent_service.ask(question)

        # Guardar respuesta del asistente.
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        # Mostrar respuesta de ALESSIA.
        with st.chat_message(
            "assistant",
            avatar=str(ALESSIA_AVATAR_PATH),
        ):
            st.write(answer)