"""
Archivo: vector_store.py

Módulo:
Procesamiento (Processing)

Objetivo:
Construir y consultar el índice vectorial del sistema utilizando
ChromaDB.

Descripción:
Este módulo centraliza todas las operaciones relacionadas con el
almacenamiento y recuperación de embeddings. Su responsabilidad es
crear la colección vectorial, indexar los Chunk generados durante
el procesamiento y recuperar los fragmentos más relevantes mediante
búsqueda por similitud.

Proyecto:
SOPHIA - Sistema de Orientación para Procedimientos con enfoque
Humano e Inteligencia Artificial.
"""

import chromadb

from chromadb.api.models.Collection import Collection
from sentence_transformers import SentenceTransformer

from src.models.chunk import Chunk
from pathlib import Path


def get_or_create_collection(
    collection_name: str,
    vector_store_path: Path,
) -> Collection:
    """
    Obtiene una colección existente de ChromaDB o la crea si aún no existe.

    Args:
        collection_name:
            Nombre de la colección vectorial.

        vector_store_path:
            Ruta donde ChromaDB almacenará la persistencia del índice.
    """

    client = chromadb.PersistentClient(
        path=str(vector_store_path)
    )

    collection = client.get_or_create_collection(
        name=collection_name
    )
    return collection


def index_chunks(
    chunks: list[Chunk],
    collection: Collection,
) -> None:
    """
    Almacena una colección de Chunk dentro del índice vectorial.

    Si los chunks ya existen, se eliminan antes de volver a indexarlos
    para evitar duplicados al ejecutar nuevamente el pipeline.
    """

    ids = [chunk.id for chunk in chunks]

    # Evita duplicar registros si el notebook se ejecuta varias veces.
    collection.delete(ids=ids)

    collection.add(
        ids=ids,
        embeddings=[chunk.embedding.tolist() for chunk in chunks],
        documents=[chunk.content for chunk in chunks],
        metadatas=[chunk.metadata for chunk in chunks],
    )



def search_chunks(
    query: str,
    collection: Collection,
    model: SentenceTransformer,
    k: int = 5,
) -> dict:
    """
    Recupera los Chunk más similares a una consulta utilizando
    búsqueda por similitud vectorial.

    La consulta se transforma en un embedding mediante el modelo
    recibido como parámetro y posteriormente se utiliza para buscar
    los fragmentos más relevantes dentro de la colección.

    Args:
        query: Consulta realizada por el usuario.
        collection: Colección donde se realizará la búsqueda.
        model: Modelo utilizado para generar el embedding de la consulta.
        k: Cantidad máxima de resultados a recuperar.

    Returns:
        Diccionario con los resultados entregados por ChromaDB.
    """

    # El embedding de la consulta se genera aquí para encapsular toda la
    # lógica de búsqueda dentro del vector store.
    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k,
    )

    return results