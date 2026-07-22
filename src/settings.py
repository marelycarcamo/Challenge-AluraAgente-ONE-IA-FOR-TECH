"""
Archivo: config.py

Módulo:
Configuración (Configuration)

Objetivo:
Centralizar la configuración del proyecto ALESSIA mediante
variables de entorno.

Descripción:
Este módulo carga las variables definidas en el archivo .env
y las pone a disposición del resto del sistema. De esta forma,
la configuración permanece desacoplada del código fuente y
permite modificar parámetros sin necesidad de realizar cambios
en la implementación.

Proyecto:
ALESSIA
"""

from pathlib import Path
import os

import streamlit as st
from dotenv import load_dotenv


# --------------------------------------------------------------
# Cargar variables de entorno
# --------------------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

# load_dotenv(
#     project_root / ".env"
# )

load_dotenv(
    project_root / ".streamlit" / "secrets.toml"
)
# --------------------------------------------------------------
# Función auxiliar de configuración
# --------------------------------------------------------------

def _get_setting(
    key: str,
    default: str | None = None,
) -> str | None:
    """
    Obtiene una configuración desde el entorno disponible.

    Prioridad:
    1. Variables de entorno, utilizadas durante el desarrollo local.
    2. Secrets de Streamlit Cloud, utilizados en el despliegue.

    Parameters
    ----------
    key : str
        Nombre de la configuración.

    default : str | None
        Valor utilizado si la configuración no existe.

    Returns
    -------
    str | None
        Valor de la configuración.
    """

    value = os.getenv(
        key
    )

    if value:
        return value

    try:
        return st.secrets.get(
            key,
            default,
        )

    except Exception:
        return default


# --------------------------------------------------------------
# Configuración del proveedor LLM
# --------------------------------------------------------------

DEFAULT_PROVIDER = "openrouter"


OPENROUTER_API_KEY = _get_setting(
    "OPENROUTER_API_KEY"
)


OPENROUTER_MODEL = _get_setting(
    "OPENROUTER_MODEL",
    "openrouter/auto",
)


LLM_TEMPERATURE = float(
    _get_setting(
        "LLM_TEMPERATURE",
        "0.2",
    )
)




print(
    "OPENROUTER_API_KEY en entorno:",
    bool(os.getenv("OPENROUTER_API_KEY"))
)

print(
    "OPENROUTER_API_KEY en secrets:",
    "OPENROUTER_API_KEY" in st.secrets
)