from dataclasses import dataclass, field
from typing import Any


@dataclass
class Chunk:
    """
    Modelo de dominio que representa un fragmento de un documento.

    Cada chunk conserva parte del contenido del documento original y la
    información necesaria para mantener la trazabilidad durante el
    pipeline RAG.
    """

    id: str
    document_id: str
    chunk_index: int
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    embedding: list[float] = field(default_factory=list)