"""
Archivo:
    test_bootstrap.py

Módulo:
    Tests del módulo bootstrap.

Objetivo:
    Validar la inicialización del servicio principal
    de la aplicación.

Descripción:
    Verifica que bootstrap delegue la creación del agente
    en AgentService.create(), manteniendo desacoplada la
    capa de presentación.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres.
"""


from unittest.mock import patch

from app.bootstrap import load_agent_service


def test_load_agent_service_returns_agent_service():
    """
    Verifica que load_agent_service utilice
    AgentService.create() para inicializar el servicio.
    """

    fake_service = object()

    with patch(
        "app.bootstrap.AgentService.create",
        return_value=fake_service,
    ) as mock_create:

        service = load_agent_service()

    mock_create.assert_called_once()

    assert service is fake_service