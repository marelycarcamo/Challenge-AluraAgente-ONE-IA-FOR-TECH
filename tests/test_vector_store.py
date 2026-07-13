import src.models.chunk
from src.processing.vector_store import index_chunks, Collection

def index_chunks(
    chunks: list[src.models.chunk.Chunk],
    collection: Collection,
    ) -> None:
    """
    Almacena una colección de Chunk dentro del índice vectorial.

    Cada Chunk aporta su identificador, contenido, embedding y metadata,
    preservando la trazabilidad entre el documento original y el índice
    utilizado durante la recuperación de información.

    Args:
        chunks: Lista de fragmentos previamente vectorizados.
        collection: Colección donde serán almacenados los embeddings.
    """

    # Se almacenan también los metadatos para mantener la trazabilidad
    # entre los resultados recuperados y el documento original.
    collection.add(
        ids=[chunk.id for chunk in chunks],
        embeddings=[
            chunk.embedding.tolist()
            if hasattr(chunk.embedding, "tolist")
            else chunk.embedding
            for chunk in chunks
        ],
        documents=[chunk.content for chunk in chunks],
        metadatas=[chunk.metadata for chunk in chunks],
    )

    return None

