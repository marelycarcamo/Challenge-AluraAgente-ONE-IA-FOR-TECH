"""
Archivo: llm_client.py

Módulo:
Procesamiento (Processing)

Objetivo:
Centralizar la comunicación entre ALESSIA y los distintos
proveedores de modelos de lenguaje (LLMs).

Descripción:
Este módulo encapsula las llamadas a los modelos de lenguaje,
permitiendo cambiar de proveedor sin afectar el resto del
pipeline RAG.

Proyecto: ALESSIA
"""

# ------------------------------------------------------------------
# Versión 1.0
#
# Actualmente ALESSIA utiliza OpenRouter como proveedor principal.
#
# En futuras versiones se podrán incorporar nuevos proveedores
# como Hugging Face u Ollama sin modificar el pipeline RAG.
# ------------------------------------------------------------------


from openrouter import OpenRouter

from src.settings import (
    DEFAULT_PROVIDER,
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
)


# --------------------------------------------------------------
# Proveedores disponibles
# --------------------------------------------------------------

def generate_response(prompt: str) -> str:
    """
    Genera una respuesta utilizando el proveedor LLM configurado.

    Parámetros
    ----------
    prompt : str
        Prompt construido para el modelo de lenguaje.

    Retorna
    -------
    str
        Respuesta generada por el modelo.
    """

    providers = {
        "openrouter": _generate_openrouter,
    }

    try:
        provider = providers[DEFAULT_PROVIDER]
    except KeyError as error:
        raise ValueError(
            f"Proveedor de LLM no soportado: {DEFAULT_PROVIDER}"
        ) from error

    return provider(prompt)


# --------------------------------------------------------------
# OpenRouter
# --------------------------------------------------------------

def _generate_openrouter(prompt: str) -> str:
    """
    Envía un prompt a OpenRouter utilizando el SDK oficial.
    """
    print(
        "API Key disponible en llm_client:",
        bool(OPENROUTER_API_KEY)
    )
    if not OPENROUTER_API_KEY:
        raise ValueError(
            "No se encontró la API Key de OpenRouter."
        )

    with OpenRouter(api_key=OPENROUTER_API_KEY) as client:

        response = client.chat.send(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

    return response.choices[0].message.content