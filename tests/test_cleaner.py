from src.models.document import Document
from src.processing.cleaner import clean_document


"""
===============================================================================
Archivo:
    test_cleaner.py

Módulo probado:
    src.processing.cleaner

Objetivo:
    Validar el comportamiento de la función clean_document().

Descripción:
    Estos tests verifican que el proceso de limpieza prepara correctamente
    el contenido de un documento antes de la etapa de chunking del pipeline RAG.

Casos cubiertos:
    - Eliminación de espacios múltiples.
    - Eliminación de tabulaciones.
    - Normalización de saltos de línea.
    - Conservación de la información del documento.

Proyecto:
    SOPHIA - Sistema de Orientación para Procedimientos con enfoque Humano e Inteligencia Artificial
===============================================================================
"""

from src.models.document import Document
from src.processing.cleaner import clean_document


def test_clean_document_removes_extra_spaces():
    """
    Verifica que clean_document():
    - elimina espacios múltiples
    - reemplaza tabulaciones por un solo espacio
    - reduce líneas en blanco consecutivas

    Este test asegura que el contenido queda limpio
    antes de continuar con el chunking.
    """

    document = Document(
        id="doc-001",
        title="Documento de prueba",
        source="test.pdf",
        file_type="pdf",
        content="Hola     mundo\n\n\nEsta\t\tes una prueba.",
        metadata={}
    )

    cleaned = clean_document(document)

    assert cleaned.content == "Hola mundo\n\nEsta es una prueba."





def test_clean_document_preserves_document_fields():
    """
    Verifica que la limpieza del contenido no modifica
    la información principal del documento.

    El cleaner solo debe alterar el campo 'content'.
    """
    document = Document(
        id="doc-002",
		title="Plan Comunal",
		source="plan.pdf",
		file_type="pdf",
		content="Texto",
		metadata={"pages": 10}
	)

    cleaned = clean_document(document)

    assert cleaned.title == document.title
    assert cleaned.source == document.source
    assert cleaned.file_type == document.file_type
    assert cleaned.metadata == document.metadata



"""
Ejecutar Bach: 
    pytest tests/test_cleaner.py
"""