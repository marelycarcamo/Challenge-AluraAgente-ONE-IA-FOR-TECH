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

from dotenv import load_dotenv


# --------------------------------------------------------------
# Cargar variables de entorno
# --------------------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

load_dotenv(project_root / ".env")


# --------------------------------------------------------------
# Configuración del proveedor LLM
# --------------------------------------------------------------

DEFAULT_PROVIDER = "openrouter"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/auto",
)

LLM_TEMPERATURE = float(
    os.getenv("LLM_TEMPERATURE", "0.2")
)
