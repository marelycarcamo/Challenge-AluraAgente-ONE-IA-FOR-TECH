"""
Archivo: chunker.py

Módulo:
Procesamiento (Processing)

Objetivo:
Dividir el contenido de un documento en fragmentos (Chunk)
manteniendo la trazabilidad con el documento original.

Descripción:
Este módulo transforma un objeto Document en una colección de Chunk
utilizando una estrategia de división basada en caracteres. Cada
fragmento conserva un identificador único, la referencia al documento
de origen y la metadata necesaria para las siguientes etapas del
pipeline RAG.

Proyecto: ALESSIA
"""

from uuid import uuid4

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.models.document import Document
from src.models.chunk import Chunk


def create_chunks(
    document: Document,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> list[Chunk]:
    """
    Divide un Document en múltiples Chunk utilizando
    RecursiveCharacterTextSplitter.

    Args:
        document: Documento que será dividido.
        chunk_size: Cantidad máxima de caracteres por Chunk.
        chunk_overlap: Cantidad de caracteres compartidos entre
            fragmentos consecutivos.

    Returns:
        Lista de Chunk generados a partir del documento.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    fragments = splitter.split_text(document.content)

    chunks = []

    for index, fragment in enumerate(fragments):

        chunk = Chunk(
            id=str(uuid4()),
            document_id=document.id,
            chunk_index=index,
            content=fragment,
            # Cada Chunk recibe una copia de la metadata para evitar que
            # varias instancias compartan la misma referencia en memoria.
            metadata=document.metadata.copy(),
        )

        chunks.append(chunk)

    return chunks