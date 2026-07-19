"""
===============================================================================
Archivo:
    test_loaders.py

Módulo probado:
    src.ingestion.loaders

Objetivo:
    Validar la correcta carga de documentos PDF y su conversión
    a objetos Document dentro del pipeline de ALESSIA.

Descripción:
    Estos tests aseguran que la función load_pdf():

    - Lea correctamente un archivo PDF válido.
    - Construya un objeto Document correctamente estructurado.
    - Extraiga contenido desde el documento.
    - Maneje correctamente errores cuando el archivo no existe.

Contexto del proyecto:
    ALESSIA - Sistema de orientación sobre gestión del riesgo de desastres
    en la comuna de Valdivia.

Notas:
    Estos tests utilizan archivos ubicados en tests/data/ para evitar
    dependencias con los documentos reales del sistema.
===============================================================================
"""

from pathlib import Path
import pytest

from src.ingestion.loaders import load_pdf
from src.models.document import Document


# Archivo de prueba controlado (fixture del sistema de tests)
PDF_TEST_FILE = Path("data/raw/test/test_plan_comunal.pdf")


def test_load_pdf_returns_document():
    """
    Caso 1:
        Verifica que load_pdf devuelve una instancia de Document.
    """
    document = load_pdf(PDF_TEST_FILE)

    assert isinstance(document, Document)


def test_load_pdf_sets_document_fields():
    """
    Caso 2:
        Verifica que los campos principales del Document
        se asignan correctamente (title, source, file_type).
    """
    document = load_pdf(PDF_TEST_FILE)

    assert document.title != ""
    assert document.source.endswith(".pdf")
    assert document.file_type == "pdf"


def test_load_pdf_extracts_content():
    """
    Caso 3:
        Verifica que el contenido del PDF fue extraído correctamente
        y no está vacío.
    """
    document = load_pdf(PDF_TEST_FILE)

    assert document.content.strip() != ""


def test_load_pdf_file_not_found():
    """
    Caso 4:
        Verifica que load_pdf lanza FileNotFoundError
        cuando el archivo no existe.
    """
    with pytest.raises(FileNotFoundError):
        load_pdf(Path("archivo_inexistente.pdf"))