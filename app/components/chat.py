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

import streamlit as st


def render_chat(
    agent_service,
):
    """
    Renderiza la interfaz conversacional
    y procesa consultas del usuario.

    Parameters
    ----------
    agent_service:
        Servicio encargado de ejecutar el pipeline RAG.

    Returns
    -------
    None
    """

    # Inicializar historial de conversación.
    # Streamlit reinicia la ejecución del script en cada interacción,
    # por lo que session_state permite mantener la memoria temporal.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial existente.
    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.write(
                message["content"]
            )

    # Capturar nueva pregunta del usuario.
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
        with st.chat_message("user"):
            st.write(question)

        # Ejecutar consulta mediante la capa de aplicación.
        answer = agent_service.ask(
            question
        )

        # Guardar respuesta del asistente.
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        # Mostrar respuesta generada.
        with st.chat_message("assistant"):
            st.write(answer)