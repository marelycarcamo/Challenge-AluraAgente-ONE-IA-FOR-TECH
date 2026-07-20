"""
Archivo:
    test_vector_store.py

Módulo:
    Tests del almacenamiento vectorial.

Objetivo:
    Validar que los objetos Chunk sean transformados correctamente
    antes de ser almacenados en ChromaDB.

Descripción:
    Verifica que vector_store conserve embeddings, contenido y
    metadata necesaria para mantener la trazabilidad del pipeline RAG.

Proyecto:
    ALESSIA
    Asistente basado en RAG para gestión del riesgo de desastres.
"""


from unittest.mock import MagicMock

import numpy as np

from src.models.chunk import Chunk
from src.processing.vector_store import index_chunks


def test_index_chunks():
    """
    Verifica que los chunks sean almacenados correctamente
    incluyendo metadata de trazabilidad.
    """

    chunk = Chunk(
        id="chunk-1",
        document_id="doc-1",
        chunk_index=0,
        content="Contenido de prueba.",
        metadata={
            "page": 1,
        },
        embedding=np.array(
            [
                0.1,
                0.2,
                0.3,
            ]
        ),
    )

    collection = MagicMock()

    index_chunks(
        chunks=[chunk],
        collection=collection,
    )

    collection.add.assert_called_once_with(
        ids=[
            "chunk-1",
        ],
        embeddings=[
            [
                0.1,
                0.2,
                0.3,
            ]
        ],
        documents=[
            "Contenido de prueba.",
        ],
        metadatas=[
            {
                "chunk_id": "chunk-1",
                "document_id": "doc-1",
                "chunk_index": 0,
                "page": 1,
            }
        ],
    )