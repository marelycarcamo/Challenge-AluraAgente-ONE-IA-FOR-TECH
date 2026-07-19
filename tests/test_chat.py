"""
Archivo:
    test_chat.py

Módulo:
    Tests del componente chat.

Objetivo:
    Validar la interacción entre la interfaz conversacional
    y AgentService.

Descripción:
    Verifica que el componente chat capture preguntas del usuario,
    invoque el servicio del agente y almacene correctamente
    la conversación en session_state.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres.
"""


from unittest.mock import MagicMock, patch

import streamlit as st

from app.components.chat import render_chat


def test_render_chat_processes_user_question():

    question = "¿Qué hacer ante una inundación?"

    answer = (
        "Evacuar según instrucciones oficiales."
    )

    agent_service = MagicMock()

    agent_service.ask.return_value = answer

    st.session_state.clear()

    with patch(
        "app.components.chat.st.chat_input",
        return_value=question,
    ), patch(
        "app.components.chat.st.chat_message",
    ), patch(
        "app.components.chat.st.write",
    ):

        render_chat(
            agent_service=agent_service,
        )

    agent_service.ask.assert_called_once_with(
        question
    )

    assert st.session_state.messages == [
        {
            "role": "user",
            "content": question,
        },
        {
            "role": "assistant",
            "content": answer,
        },
    ]