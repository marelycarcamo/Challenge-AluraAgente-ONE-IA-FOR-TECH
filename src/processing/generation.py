"""
Archivo: generation.py

Módulo:
Procesamiento (Processing)

Objetivo:
Generar respuestas utilizando un modelo de lenguaje a partir del
contexto recuperado durante la etapa de Retrieval.

Descripción:
Este módulo coordina la construcción del prompt y la comunicación
con el proveedor de lenguaje configurado.

Proyecto:
ALESSIA - Asistente Local para la gestión del riesgo de desastres.
"""


from src.models.chunk import Chunk
from src.processing.prompt_builder import build_prompt
from src.processing.llm_client import generate_response


def generate_answer(
    question: str,
    context: list[Chunk],
) -> str:
    """
    Genera una respuesta utilizando un modelo de lenguaje.

    Parámetros
    ----------
    question : str
        Pregunta realizada por el usuario.

    context : list[Chunk]
        Fragmentos recuperados durante la etapa de Retrieval.

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
    # Generar la respuesta utilizando el proveedor LLM configurado
    # --------------------------------------------------------------

    answer = generate_response(prompt)

    # --------------------------------------------------------------
    # Retornar la respuesta generada
    # --------------------------------------------------------------

    return answer