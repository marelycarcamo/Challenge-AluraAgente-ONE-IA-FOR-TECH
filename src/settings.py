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

# from pathlib import Path
# import os

# import streamlit as st
# from dotenv import load_dotenv


# # --------------------------------------------------------------
# # Cargar variables de entorno
# # --------------------------------------------------------------

# project_root = Path(__file__).resolve().parent.parent

# # load_dotenv(
# #     project_root / ".env"
# # )

# load_dotenv(
#     project_root / ".streamlit" / "secrets.toml"
# )
# # --------------------------------------------------------------
# # Función auxiliar de configuración
# # --------------------------------------------------------------

# def _get_setting(
#     key: str,
#     default: str | None = None,
# ) -> str | None:
#     """
#     Obtiene una configuración desde el entorno disponible.

#     Prioridad:
#     1. Variables de entorno, utilizadas durante el desarrollo local.
#     2. Secrets de Streamlit Cloud, utilizados en el despliegue.

#     Parameters
#     ----------
#     key : str
#         Nombre de la configuración.

#     default : str | None
#         Valor utilizado si la configuración no existe.

#     Returns
#     -------
#     str | None
#         Valor de la configuración.
#     """

#     value = os.getenv(
#         key
#     )

#     if value:
#         return value

#     try:
#         return st.secrets.get(
#             key,
#             default,
#         )

#     except Exception:
#         return default




# # --------------------------------------------------------------
# # Configuración del proveedor LLM
# # --------------------------------------------------------------

# DEFAULT_PROVIDER = "openrouter"


# # OPENROUTER_API_KEY = _get_setting(
# #     "OPENROUTER_API_KEY"
# # )

# OPENROUTER_API_KEY = _get_setting(
#     "OPENROUTER_API_KEY"
# )


# print(
#     "DEBUG settings.py - OPENROUTER_API_KEY:",
#     {
#         "is_none": OPENROUTER_API_KEY is None,
#         "is_empty": OPENROUTER_API_KEY == "",
#         "length": len(OPENROUTER_API_KEY)
#         if OPENROUTER_API_KEY
#         else 0,
#         "prefix": OPENROUTER_API_KEY[:7]
#         if OPENROUTER_API_KEY
#         else None,
#     },
# )

# OPENROUTER_MODEL = _get_setting(
#     "OPENROUTER_MODEL",
#     "openrouter/auto",
# )


# LLM_TEMPERATURE = float(
#     _get_setting(
#         "LLM_TEMPERATURE",
#         "0.2",
#     )
# )




# print(
#     "OPENROUTER_API_KEY en entorno:",
#     bool(os.getenv("OPENROUTER_API_KEY"))
# )

# print(
#     "OPENROUTER_API_KEY en secrets:",
#     "OPENROUTER_API_KEY" in st.secrets
# )


from pathlib import Path
import os
import streamlit as st
from dotenv import load_dotenv

# --------------------------------------------------------------
# Cargar variables de entorno (SOLO para desarrollo local)
# --------------------------------------------------------------

project_root = Path(__file__).resolve().parent

# Solo carga .env si existe (para desarrollo local)
env_path = project_root / ".env"
if env_path.exists():
    load_dotenv(env_path)

# --------------------------------------------------------------
# Función auxiliar de configuración CORREGIDA
# --------------------------------------------------------------

def _get_setting(
    key: str,
    default: str | None = None,
) -> str | None:
    """
    Obtiene una configuración con prioridad correcta:
    1. st.secrets (Streamlit Cloud)
    2. Variables de entorno (desarrollo local)
    3. Valor por defecto
    """
    
    # PRIORIDAD 1: Streamlit Secrets (producción en Streamlit Cloud)
    try:
        if hasattr(st, 'secrets') and key in st.secrets:
            value = st.secrets[key]
            if value:
                return value
    except Exception:
        pass
    
    # PRIORIDAD 2: Variables de entorno (desarrollo local)
    value = os.getenv(key)
    if value:
        return value
    
    # PRIORIDAD 3: Valor por defecto
    return default

# --------------------------------------------------------------
# Configuración del proveedor LLM
# --------------------------------------------------------------

DEFAULT_PROVIDER = "openrouter"

# Obtener la API key con la función corregida
OPENROUTER_API_KEY = _get_setting("OPENROUTER_API_KEY")

# Debugging - Útil para verificar en logs de Streamlit
if OPENROUTER_API_KEY:
    print(f"✅ OPENROUTER_API_KEY encontrada (longitud: {len(OPENROUTER_API_KEY)})")
    print(f"   Primeros 10 caracteres: {OPENROUTER_API_KEY[:10]}...")
else:
    print("❌ OPENROUTER_API_KEY NO encontrada")
    # Opcional: mostrar estado de secrets para debugging
    if hasattr(st, 'secrets'):
        print(f"   Secrets disponibles: {list(st.secrets.keys()) if st.secrets else 'None'}")

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