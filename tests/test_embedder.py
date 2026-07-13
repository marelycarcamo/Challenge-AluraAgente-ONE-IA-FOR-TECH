"""
Archivo:
    test_embedder.py

Módulo probado:
    src.processing.embedder

Objetivo:
    Validar la generación correcta de embeddings para objetos
    Chunk dentro del pipeline RAG de SOPHIA.

Descripción:
    Estos tests aseguran que la función generate_embeddings():

    - Reciba correctamente una colección de Chunk.
    - Genere una representación vectorial para cada fragmento.
    - Mantenga la cantidad original de elementos.
    - Enriquezca cada Chunk con su embedding correspondiente.

Contexto del proyecto:
    SOPHIA - Sistema de orientación sobre gestión del riesgo de desastres
    en la comuna de Valdivia.

Notas:
    Estos tests utilizan fragmentos pequeños generados en memoria para
    validar el comportamiento del módulo sin depender de documentos reales.
===============================================================================
"""


from src.models.chunk import Chunk
from src.processing.embedder import generate_embeddings



import chromadb





def test_generate_embeddings_adds_embedding():
    """
    Verifica que un Chunk individual sea enriquecido con
    su representación vectorial correspondiente.
    """
    chunks = [
        Chunk(
            id="chunk_1",
            document_id="doc_1",
            chunk_index=0,
            content="Plan comunal de emergencia de Valdivia.",
        )
    ]

    class DummyModel:
        def encode(self, texts):
            if isinstance(texts, str):
                texts = [texts]
            return [[0.1, 0.2, 0.3] for _ in texts]

    model = DummyModel()

    result = generate_embeddings(
        chunks,
        model,
    )

    assert len(result) == 1
    assert result[0].embedding is not None
    assert len(result[0].embedding) > 0


def test_generate_embeddings_processes_multiple_chunks():
    """
    Verifica que el proceso pueda generar embeddings para
    múltiples fragmentos manteniendo la correspondencia
    entre chunks de entrada y salida.
    """
    chunks = [
        Chunk(
            id="chunk_1",
            document_id="doc_1",
            chunk_index=0,
            content="Plan comunal de emergencia.",
        ),
        Chunk(
            id="chunk_2",
            document_id="doc_1",
            chunk_index=1,
            content="Medidas de evacuación ante tsunami.",
        ),
    ]

    class DummyModel:
        def encode(self, texts):
            if isinstance(texts, str):
                texts = [texts]
            return [[0.1, 0.2, 0.3] for _ in texts]

    model = DummyModel()

    result = generate_embeddings(
        chunks,
        model,
    )

    assert len(result) == 2

    for chunk in result:
        assert chunk.embedding is not None
        assert len(chunk.embedding) > 0

        