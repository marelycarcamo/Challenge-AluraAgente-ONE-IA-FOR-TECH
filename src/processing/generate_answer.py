from src.models import Chunk, LLMClient
from src.processing.prompt_builder import build_prompt

def generate_answer(
    question: str,
    context: list[Chunk],
    llm_client: LLMClient,
) -> str:
    """
    Genera una respuesta utilizando un modelo de lenguaje.

    Parámetros
    ----------
    question : str
        Pregunta realizada por el usuario.

    context : list[Chunk]
        Fragmentos recuperados durante la etapa de Retrieval.

    llm_client : LLMClient
        Cliente encargado de comunicarse con el modelo de lenguaje.

    Retorna
    -------
    str
        Respuesta generada por el modelo.
    """

    # --------------------------------------------------------------
    # Construir el prompt para el modelo
    # --------------------------------------------------------------

    prompt = build_prompt(
        question=question,
        context=context,
    )

    # --------------------------------------------------------------
    # Generar la respuesta utilizando el modelo de lenguaje
    # --------------------------------------------------------------

    answer = llm_client.generate(prompt)

    # --------------------------------------------------------------
    # Retornar la respuesta generada
    # --------------------------------------------------------------

    return answer