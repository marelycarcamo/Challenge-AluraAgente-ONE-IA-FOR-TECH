"""
Archivo:
    test_generation.py

Módulo:
    Tests unitarios - Generation

Objetivo:
    Validar el comportamiento del módulo generation.py,
    verificando que la función generate_answer construya el prompt
    correctamente y utilice el proveedor LLM configurado.

Descripción:
    Estos tests validan la integración interna entre:
    
    - generación del prompt;
    - envío del prompt al cliente LLM;
    - retorno de la respuesta generada.

    El proveedor real de lenguaje es reemplazado mediante mocks
    para validar únicamente la lógica del módulo.

Proyecto:
    ALESSIA - Asistente de gestión del riesgo de desastres
    para la comuna de Valdivia.
"""


from unittest.mock import patch

from src.models.chunk import Chunk
from src.processing.generation import generate_answer


def test_generate_answer_builds_prompt_and_returns_response():
    """
    Verifica que generate_answer construya el prompt
    y retorne la respuesta generada por el LLM.
    """

    chunk = Chunk(
        id="chunk-1",
        document_id="doc-1",
        chunk_index=0,
        content="Contenido de prueba.",
        metadata={},
    )

    with (
        patch(
            "src.processing.generation.build_prompt",
            return_value="PROMPT DE PRUEBA",
        ) as mock_build_prompt,
        patch(
            "src.processing.generation.generate_response",
            return_value="Respuesta generada.",
        ) as mock_generate_response,
    ):

        answer = generate_answer(
            question="¿Qué hacer ante una inundación?",
            context=[chunk],
        )

        mock_build_prompt.assert_called_once_with(
            question="¿Qué hacer ante una inundación?",
            context=[chunk],
        )

        mock_generate_response.assert_called_once_with(
            "PROMPT DE PRUEBA"
        )

        assert answer == "Respuesta generada."