"""
Archivo: test_agent_service.py

Módulo:
    tests

Objetivo:
    Validar el comportamiento de AgentService como capa de orquestación
    del pipeline RAG, verificando la correcta comunicación entre los
    módulos de recuperación, reranking y generación de respuestas.

Descripción:
    Este módulo contiene pruebas unitarias para comprobar que AgentService
    coordina correctamente las distintas etapas del pipeline RAG.

    Las pruebas utilizan objetos simulados para evitar depender de
    servicios externos como ChromaDB, modelos de embeddings o proveedores
    LLM, enfocándose en validar la responsabilidad del servicio como
    punto de entrada de la aplicación.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""
from unittest.mock import Mock, patch

from src.services.agent_service import AgentService


def test_agent_service_executes_pipeline():
    """AgentService.ask coordina retrieval, reranking y generation."""

    question = "¿Qué hacer ante una inundación?"

    expected_answer = (
        "Mantenerse informado por canales oficiales."
    )

    fake_chunks = [Mock()]

    with patch.object(
        AgentService, "_retrieve_context", return_value=fake_chunks
    ) as mock_retrieve, \
    patch.object(
        AgentService, "_rerank_chunks", return_value=fake_chunks
    ) as mock_rerank, \
    patch.object(
        AgentService, "_generate_answer", return_value=expected_answer
    ) as mock_generate:

        service = AgentService(
            collection=Mock(),
            embedding_model=Mock(),
            reranker_model=Mock(),
        )

        result = service.ask(question)

    assert result == expected_answer

    mock_retrieve.assert_called_once_with(question)

    mock_rerank.assert_called_once_with(question, fake_chunks)

    mock_generate.assert_called_once_with(question, fake_chunks)