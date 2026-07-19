"""
Archivo:
    config.py

Módulo:
    app

Objetivo:
    Centralizar la configuración general de la aplicación Streamlit.

Descripción:
    Este módulo contiene las constantes utilizadas por la interfaz
    de usuario, incluyendo identidad visual, textos principales y
    rutas hacia recursos gráficos.

    Mantener esta configuración separada permite modificar elementos
    visuales de la aplicación sin afectar la lógica de presentación
    ni el pipeline RAG.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""

from pathlib import Path


# Identidad de la aplicación

APP_NAME = "ALESSIA"

APP_DESCRIPTION = (
    "Asistente inteligente para la gestión "
    "del riesgo de desastres en Valdivia."
)


APP_ICON = "🌊"


# Rutas de recursos visuales

APP_DIR = Path(__file__).parent


ASSETS_DIR = (
    APP_DIR
    / "assets"
)


LOGO_PATH = (
    ASSETS_DIR
    / "logo"
    / "alessia_logo.png"
)


AVATAR_PATH = (
    ASSETS_DIR
    / "images"
    / "alessia_avatar.png"
)