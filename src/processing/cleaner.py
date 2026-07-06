"""
Module: cleaner.py

Purpose
-------
Clean and normalize document text before chunking.

Responsibilities
----------------
- Remove unnecessary whitespace.
- Normalize line breaks.
- Return a cleaned Document.

This module DOES NOT:
- Download files.
- Read documents.
- Split text into chunks.
- Generate embeddings.
"""

import re

from src.models.document import Document


def clean_document(document: Document) -> Document:
    """
    Clean the textual content of a Document.

    Args:
        document (Document): Document to clean.

    Returns:
        Document: New Document with cleaned text.
    """

    text = document.content

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Collapse multiple blank lines into one
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Replace multiple spaces or tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove leading/trailing whitespace
    text = text.strip()

    return Document(
        title=document.title,
        source=document.source,
        file_type=document.file_type,
        content=text,
        metadata=document.metadata.copy()
    )