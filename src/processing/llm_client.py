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
# Actualmente ALESSIA utiliza únicamente OpenRouter.
#
# En una versión futura este módulo implementará failover automático
# entre múltiples proveedores (OpenRouter, Hugging Face, Ollama, etc.)
# cuando se produzcan errores recuperables como Rate Limit (429).
# ------------------------------------------------------------------




import requests
from src.settings import (
    DEFAULT_PROVIDER,
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL,
    LLM_TEMPERATURE
)

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_response(prompt: str) -> str:
    """
    Genera una respuesta utilizando el proveedor configurado.

    Parámetros
    ----------
    prompt : str
        Prompt construido para el modelo de lenguaje.

    Retorna
    -------
    str
        Respuesta generada por el modelo.
    """

    match DEFAULT_PROVIDER:

        case "openrouter":
            return _generate_openrouter(prompt)
        case _:
            raise ValueError(
                f"Proveedor de LLM no soportado: {DEFAULT_PROVIDER}"
            )


def _generate_openrouter(prompt: str) -> str:
    """
    Envía un prompt a OpenRouter y retorna la respuesta generada.
    """

    if not OPENROUTER_API_KEY:
        raise ValueError(
            "No se encontró la API Key de OpenRouter."
        )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "temperature": LLM_TEMPERATURE,
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]

    except (KeyError, IndexError) as error:
        raise RuntimeError(
            "Respuesta inválida recibida desde OpenRouter."
        ) from error


def _generate_openrouter(prompt: str) -> str:
    """
    Implementación pendiente para openrouter.
    """
    raise NotImplementedError(
        "Proveedor openrouter aún no implementado."
    )


def _generate_huggerface(prompt: str) -> str:
    """
    Implementación pendiente para huggerface.
    """
    raise NotImplementedError(
        "Proveedor huggerface aún no implementado."
    )