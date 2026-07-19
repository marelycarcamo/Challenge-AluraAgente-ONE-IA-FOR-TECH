from unittest.mock import MagicMock

import numpy as np

from src.models.chunk import Chunk
from src.processing.vector_store import index_chunks


def test_index_chunks():
    """Verifica que los chunks sean almacenados correctamente."""

    chunk = Chunk(
        id="chunk-1",
        document_id="doc-1",
        chunk_index=0,
        content="Contenido de prueba.",
        metadata={"page": 1},
        embedding=np.array([0.1, 0.2, 0.3]),
    )

    collection = MagicMock()

    index_chunks(
        chunks=[chunk],
        collection=collection,
    )

    collection.add.assert_called_once_with(
        ids=["chunk-1"],
        embeddings=[[0.1, 0.2, 0.3]],
        documents=["Contenido de prueba."],
        metadatas=[{"page": 1}],
    )