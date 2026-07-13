from src.models.chunk import Chunk

"""
===============================================================================
Archivo:
    test_chunk.py

Módulo probado:
    src.models.chunk

Objetivo:
    Validar el modelo de dominio Chunk.

Descripción:
    Estos tests verifican que un Chunk se instancia correctamente y conserva
    la información necesaria para mantener la trazabilidad durante el pipeline RAG.

Casos cubiertos:
    - Creación de un Chunk.
    - Almacenamiento correcto de sus atributos.

Proyecto:
    SOPHIA - Sistema de Orientación para Procedimientos con enfoque Humano e Inteligencia Artificial
===============================================================================
"""

def test_chunk_creation():
    """Verifica que un Chunk se crea correctamente."""

    chunk = Chunk(
        id="chunk-001",
        document_id="doc-001",
        chunk_index=0,
        content="Contenido del primer fragmento.",
        metadata={"pages": 10},
    )

    assert chunk.id == "chunk-001"
    assert chunk.document_id == "doc-001"
    assert chunk.chunk_index == 0
    assert chunk.content == "Contenido del primer fragmento."
    assert chunk.metadata["pages"] == 10



def test_chunk_default_metadata():
    
    """ Verifica que un Chunk se crea con metadata vacía por defecto. """
    

    chunk = Chunk(
        id="chunk-001",
        document_id="doc-001",
        chunk_index=0,
        content="Contenido del fragmento.",
    )

    assert chunk.metadata == {}



def test_chunks_have_independent_metadata():
    """Verifica que cada Chunk mantiene su metadata independiente."""

    chunk_1 = Chunk(
        id="chunk-001",
        document_id="doc-001",
        chunk_index=0,
        content="Primer fragmento.",
    )

    chunk_2 = Chunk(
        id="chunk-002",
        document_id="doc-001",
        chunk_index=1,
        content="Segundo fragmento.",
    )

    chunk_1.metadata["page"] = 1

    assert "page" not in chunk_2.metadata



def test_chunk_embedding_is_none_by_default():
    """
    Verifica que un Chunk recién creado no tenga embedding asociado.

    El embedding se genera posteriormente durante la etapa de Embeddings,
    por lo que inicialmente debe ser None.
    """
    
    chunk = Chunk(
        id="chunk-001",
        document_id="doc-001",
        chunk_index=0,
        content="Contenido del fragmento.",
    )

    assert chunk.embedding is None