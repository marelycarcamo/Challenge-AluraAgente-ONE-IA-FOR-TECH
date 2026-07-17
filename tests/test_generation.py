from unittest.mock import MagicMock, patch

from src.models.chunk import Chunk
from src.processing.generation import generate_answer


def test_generate_answer_calls_llm_and_returns_response():
    """Verifica que generate_answer construya el prompt y devuelva la respuesta del LLM."""

    chunk = Chunk(
        id="chunk-1",
        document_id="doc-1",
        chunk_index=0,
        content="Contenido de prueba.",
        metadata={},
    )

    llm_client = MagicMock()
    llm_client.generate.return_value = "Respuesta generada."

    with patch(
        "src.processing.generation.build_prompt",
        return_value="PROMPT DE PRUEBA",
    ) as mock_build_prompt:

        answer = generate_answer(
            question="¿Qué hacer ante una inundación?",
            context=[chunk],
            llm_client=llm_client,
        )

        mock_build_prompt.assert_called_once_with(
            question="¿Qué hacer ante una inundación?",
            context=[chunk],
        )

        llm_client.generate.assert_called_once_with(
            "PROMPT DE PRUEBA"
        )

    assert answer == "Respuesta generada."