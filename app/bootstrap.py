"""
Archivo:
    bootstrap.py

Módulo:
    Inicialización de aplicación.

Objetivo:
    Centralizar la creación de servicios necesarios para la aplicación.

Descripción:
    Este módulo contiene las funciones encargadas de inicializar
    las dependencias principales de la aplicación.

    Permite mantener la capa de presentación desacoplada de la
    configuración interna del pipeline RAG.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres.
"""


from src.services.agent_service import AgentService


def load_agent_service() -> AgentService:
    """
    Inicializa el servicio principal del agente.

    Esta función actúa como punto único de entrada para crear
    AgentService dentro de la aplicación.

    Returns
    -------
    AgentService
        Servicio configurado para ejecutar consultas RAG.
    """

    return AgentService.create()

