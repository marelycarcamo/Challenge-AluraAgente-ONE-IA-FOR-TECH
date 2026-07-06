"""
Module: scraper.py

Purpose
-------
Download official documents from the web and save them locally.

Responsibilities
----------------
- Download files from a URL.
- Save files into the raw data directory.
- Return the local path of the downloaded file.

This module DOES NOT:
- Read document contents.
- Extract text.
- Clean text.
- Create Document objects.
"""

from pathlib import Path

import requests


def download_pdf(url: str, output_dir: Path) -> Path:
    """
    Download a PDF file from a URL.

    Args:
        url (str): URL of the PDF.
        output_dir (Path): Directory where the file will be saved.

    Returns:
        Path: Local path of the downloaded file.

    Raises:
        ValueError: If the download fails.
    """

    output_dir.mkdir(parents=True, exist_ok=True)

    filename = url.split("/")[-1]
    destination = output_dir / filename

    headers = {
        "User-Agent": "SOPHIA-RAG/1.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        destination.write_bytes(response.content)

        return destination

    except requests.RequestException as e:
        raise ValueError(f"Error downloading PDF: {e}")