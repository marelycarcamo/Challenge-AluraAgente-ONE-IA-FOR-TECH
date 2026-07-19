from unittest.mock import patch

from src.processing.generation import generate_answer


def test_generate_answer_builds_prompt_and_returns_response():
    """
    Verifica que generate_answer transforme el contexto recibido
    desde el reranker, construya el prompt y retorne la respuesta
    generada por el LLM.
    """

    context = [
        {
            "document": "Contenido de prueba.",
            "metadata": {},
            "score": 0.95,
        }
    ]

    with patch(
        "src.processing.generation.build_prompt",
        return_value="PROMPT DE PRUEBA",
    ) as mock_build_prompt, patch(
        "src.processing.generation.generate_response",
        return_value="Respuesta generada.",
    ) as mock_generate_response:

        answer = generate_answer(
            question="¿Qué hacer ante una inundación?",
            context=context,
        )

        mock_build_prompt.assert_called_once_with(
            question="¿Qué hacer ante una inundación?",
            context=[
                "Contenido de prueba.",
            ],
        )

        mock_generate_response.assert_called_once_with(
            "PROMPT DE PRUEBA"
        )

        assert answer == "Respuesta generada."