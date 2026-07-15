"""
Archivo: retriever.py

Módulo:
Procesamiento (Processing)

Objetivo:
Recuperar los fragmentos de texto más relevantes para una consulta
realizada por el usuario utilizando búsqueda semántica sobre el
índice vectorial.

Descripción:
Este módulo actúa como intermediario entre la consulta del usuario y
el Vector Store. Su responsabilidad es recuperar los Chunk más
relevantes a partir de una búsqueda por similitud, proporcionando el
contexto que será utilizado posteriormente durante la generación de
respuestas del sistema RAG.

Proyecto:
SOPHIA - Sistema de Orientación para Procedimientos con enfoque
Humano e Inteligencia Artificial.
"""


from chromadb.api.models.Collection import Collection
from sentence_transformers import SentenceTransformer

from src.processing.vector_store import search_chunks


def retrieve_context(
    query: str,
    collection: Collection,
    model: SentenceTransformer,
    k: int = 5,
) -> list[str]:
    """
    Recupera los fragmentos de texto más relevantes para una consulta.

    Esta función delega la búsqueda semántica al módulo ``vector_store``
    y extrae únicamente el contenido textual de los resultados. De esta
    forma, el resto del sistema no necesita conocer la estructura interna
    de la respuesta entregada por ChromaDB.

    Args:
        query: Consulta realizada por el usuario.
        collection: Colección donde se realizará la búsqueda semántica.
        model: Modelo utilizado para generar el embedding de la consulta.
        k: Cantidad máxima de fragmentos a recuperar.

    Returns:
        Lista con los fragmentos de texto más relevantes.
    """

    # La búsqueda semántica se delega al módulo vector_store para mantener
    # encapsulada toda la interacción con ChromaDB.
    results = search_chunks(
        query=query,
        collection=collection,
        model=model,
        k=k,
    )

    # ChromaDB devuelve una lista de documentos por cada consulta realizada.
    # Como SOPHIA procesa una única consulta, se extrae el primer elemento.
    context_fragments = results["documents"][0]

    return context_fragments

