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

    with patch(
        "src.processing.generation.build_prompt",
        return_value="PROMPT DE PRUEBA",
    ) as mock_build_prompt, patch(
        "src.processing.generation.generate_response",
        return_value="Respuesta generada.",
    ) as mock_generate_response:

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