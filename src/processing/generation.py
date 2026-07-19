"""
Archivo:
    generation.py

Módulo:
    Processing - Generation

Objetivo:
    Generar respuestas utilizando un modelo de lenguaje basado en el
    contexto recuperado durante el pipeline RAG.

Descripción:
    Este módulo recibe los fragmentos relevantes obtenidos durante las
    etapas de Retrieval y Reranking, construye el prompt correspondiente
    y envía la solicitud al proveedor LLM configurado.

    Trabaja directamente con objetos Chunk para mantener la trazabilidad
    del dominio y evitar dependencias con estructuras internas del
    vector store.

Proyecto:
    ALESSIA - Asistente de gestión del riesgo de desastres
    para la comuna de Valdivia.
"""


from src.models.chunk import Chunk

from src.processing.prompt_builder import build_prompt
from src.processing.llm_client import generate_response


def generate_answer(
    question: str,
    context: list[Chunk],
) -> str:
    """
    Genera una respuesta utilizando el modelo de lenguaje configurado.

    Args:
        question:
            Consulta realizada por el usuario.

        context:
            Fragmentos relevantes recuperados durante Retrieval
            y ordenados mediante Reranking.

    Returns:
        Respuesta generada por el modelo de lenguaje.
    """

    # Construye el prompt utilizando los fragmentos seleccionados.
    prompt = build_prompt(
        question=question,
        context=context,
    )

    # Envía el prompt al proveedor LLM configurado.
    answer = generate_response(
        prompt
    )

    return answer