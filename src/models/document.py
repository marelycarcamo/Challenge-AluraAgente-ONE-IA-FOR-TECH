from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:
    """
    Modelo de dominio que representa un documento dentro del pipeline RAG.

    El identificador (id) permite mantener la trazabilidad del documento
    durante todas las etapas del pipeline, desde la carga hasta la
    recuperación de información.
    """

    id: str 
    title: str
    source: str
    file_type: str
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)

