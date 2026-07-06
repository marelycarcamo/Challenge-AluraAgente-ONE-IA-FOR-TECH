from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    """
    Modelo de dominio que representa un documento dentro del pipeline RAG.
    """

    title: str
    source: str
    file_type: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)