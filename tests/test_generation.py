"""
Archivo:
    test_generation.py

Módulo:
    Tests del módulo generation.

Objetivo:
    Validar que el módulo de generación coordina correctamente
    la construcción del prompt y la llamada al proveedor LLM.

Descripción:
    Verifica que generate_answer() utilice el contexto recibido
    como objetos de dominio Chunk, manteniendo la arquitectura
    desacoplada del pipeline RAG.

Proyecto:
    ALESSIA
    Asistente basado en RAG para gestión del riesgo de desastres.
"""


from unittest.mock import patch

from src.models.chunk import Chunk
from src.processing.generation import generate_answer


def test_generate_answer_builds_prompt_and_returns_response():
    """
    Verifica que generate_answer construya el prompt utilizando
    los chunks recibidos y retorne la respuesta generada por el LLM.
    """

    question = "¿Qué hacer ante una inundación?"

    chunk = Chunk(
        id="chunk-1",
        document_id="document-1",
        chunk_index=0,
        content="Contenido de prueba.",
        metadata={
            "page": 1,
            "source": "Plan-Comunal-de-Emergencia-2025-2.pdf",
        },
    )

    context = [chunk]

    with patch(
        "src.processing.generation.build_prompt",
        return_value="PROMPT DE PRUEBA",
    ) as mock_build_prompt, patch(
        "src.processing.generation.generate_response",
        return_value="Respuesta generada.",
    ) as mock_generate_response:

        answer = generate_answer(
            question=question,
            context=context,
        )

    mock_build_prompt.assert_called_once_with(
        question=question,
        context=context,
    )

    mock_generate_response.assert_called_once_with(
        "PROMPT DE PRUEBA"
    )

    assert answer == "Respuesta generada."