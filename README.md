![Logo ALESSIA](https://raw.githubusercontent.com/marelycarcamo/Challenge-AluraAgente-ONE-IA-FOR-TECH/main/app/assets/logo/alessia_logo.png)

<p align="center">
  <a href="https://alessia.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_PROBAR_ALESSIA-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Probar ALESSIA">
  </a>
</p>

---

# Tabla de Indice

- [Tabla de Indice](#tabla-de-indice)
	- [1. ¿PorquÉ nace ALESSIA?](#1-porqué-nace-alessia)
	- [2. ¿Qué es ALESSIA?](#2-qué-es-alessia)
	- [3. Qué aporta ALESSIA?](#3-qué-aporta-alessia)
	- [4. ¿Cuál es el proyecto detrás de ALESSIA?](#4-cuál-es-el-proyecto-detrás-de-alessia)
	- [5. Ciclo de interacción con ALESSIA](#5-ciclo-de-interacción-con-alessia)
	- [](#)
	- [6. ALESSIA en acción](#6-alessia-en-acción)
	- [7. Arquitectura del sistema](#7-arquitectura-del-sistema)
		- [Capas de Arquitectura](#capas-de-arquitectura)
	- [8. Flujo del pipeline RAG](#8-flujo-del-pipeline-rag)
	- [9. Estructura del proyecto](#9-estructura-del-proyecto)
	- [10. Tecnologías utilizadas](#10-tecnologías-utilizadas)
	- [11. Características implementadas (Versión 1.0)](#11-características-implementadas-versión-10)
		- [Funcionalidades existentes](#funcionalidades-existentes)
	- [12. Instalación y ejecución](#12-instalación-y-ejecución)
		- [1. Clonar el repositorio](#1-clonar-el-repositorio)
		- [2. Crear y activar el entorno virtual](#2-crear-y-activar-el-entorno-virtual)
		- [3. Instalar dependencias](#3-instalar-dependencias)
		- [4. Configurar la API KEY](#4-configurar-la-api-key)
		- [5. Ejecutar ALESSIA](#5-ejecutar-alessia)
	- [13. Roadmap](#13-roadmap)
	- [14. Author \& Licence](#14-author--licence)



---

![ALESSIA](https://raw.githubusercontent.com/marelycarcamo/Challenge-AluraAgente-ONE-IA-FOR-TECH/fa5bcde7d6d9b214459f2a04a5aac1c49a3159ba/app/assets/images/alessia_img_2.png)


---

## 1. ¿PorquÉ nace ALESSIA?

La gestión del riesgo de desastres requiere acceso oportuno a información confiable para apoyar la preparación, prevención y respuesta ante distintos escenarios de emergencia.

Las instituciones públicas generan una gran cantidad de documentación oficial, como planes comunales de emergencia, protocolos, normativas y recomendaciones. Sin embargo, esta información suele encontrarse distribuida en múltiples documentos, almacenada en formatos poco interactivos y escrita en un lenguaje técnico que puede dificultar su consulta rápida.

Ante una situación de necesidad, encontrar una respuesta específica puede requerir revisar manualmente extensos documentos, identificar la fuente correcta e interpretar información especializada.

**ALESSIA** nace para reducir esta brecha entre las personas y el conocimiento institucional disponible, facilitando el acceso conversacional a información oficial relacionada con la gestión del riesgo de desastres.


| Antes de ALESSIA                                        | Con ALESSIA                                                |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| Buscar manualmente entre múltiples documentos oficiales | Consultar información mediante lenguaje natural            |
| Revisar extensos archivos PDF                           | Recuperar información relevante automáticamente            |
| Interpretar documentos técnicos                         | Recibir respuestas claras basadas en documentación oficial |
| Dificultad para identificar rápidamente la fuente       | Mantener trazabilidad hacia la información utilizada       |

>**ALESSIA** no reemplaza la información oficial ni la toma de decisiones de las autoridades. Su propósito es facilitar el acceso, comprensión y consulta del conocimiento institucional disponible.

---

## 2. ¿Qué es ALESSIA?

[Video de presentación de ALESSIA](https://youtu.be/UZ_mJdIBY8s)


<p align="center">
  <a href="https://www.youtube.com/watch?v=UZ_mJdIBY8s" target="_blank">
    <img src="https://img.youtube.com/vi/UZ_mJdIBY8s/0.jpg" alt="Ver video del proyecto" width="560" height="315">
  </a>
</p>

**ALESSIA** (Asistente Local de Enlace, Soluciones e Inteligencia Autónoma) es un asistente basado en Inteligencia Artificial Generativa y arquitectura RAG (Retrieval Augmented Generation), diseñado para facilitar el acceso a información oficial relacionada con la gestión del riesgo de desastres en la comuna de Valdivia.

A través de una interfaz conversacional, ALESSIA permite realizar consultas utilizando lenguaje natural y genera respuestas fundamentadas en documentación institucional previamente procesada, reduciendo la necesidad de revisar manualmente múltiples fuentes.

Su diseño prioriza:

* **Confiabilidad:** las respuestas se generan utilizando información proveniente de fuentes oficiales.
* **Trazabilidad:** el sistema mantiene relación entre las respuestas generadas y la documentación utilizada.
* **Responsabilidad:** **ALESSIA** informa y orienta, pero no reemplaza los protocolos oficiales ni la toma de decisiones de las autoridades.

---

## 3. Qué aporta ALESSIA?

**ALESSIA** facilita el acceso a información oficial relacionada con la gestión del riesgo de desastres mediante una experiencia conversacional respaldada por documentación institucional.

Sus principales aportes son:

* **Acceso simplificado a la información:** permite consultar documentos oficiales utilizando lenguaje natural, reduciendo el tiempo necesario para encontrar información relevante.
* **Respuestas fundamentadas:** genera respuestas utilizando únicamente el contexto recuperado desde documentación previamente procesada, priorizando la confiabilidad de la información entregada.
* **Mayor trazabilidad:** mantiene la relación entre las respuestas generadas y las fuentes documentales utilizadas, promoviendo la transparencia en el acceso a la información.
* **Arquitectura escalable:** su diseño modular permite incorporar nuevas capacidades, como memoria conversacional, integración con APIs oficiales y herramientas de apoyo a la gestión administrativa, sin modificar la estructura principal del sistema.

---

## 4. ¿Cuál es el proyecto detrás de ALESSIA?

**ALESSIA** es un proyecto concebido para evolucionar progresivamente desde un asistente documental basado en arquitectura RAG hacia una plataforma inteligente de apoyo a la gestión del riesgo de desastres.

La versión actual (1.0) establece las bases del sistema mediante un pipeline completo de recuperación y generación de información utilizando documentación oficial. Sobre esta arquitectura se proyecta la incorporación de nuevas capacidades orientadas a mejorar la experiencia de los usuarios, fortalecer la trazabilidad de la información y facilitar la gestión del conocimiento institucional.

Su diseño modular permite incorporar futuras funcionalidades sin modificar la arquitectura principal del sistema, favoreciendo su evolución de manera gradual y mantenible.

| Versión | Enfoque                                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| **1.0** | Asistente documental basado en RAG.                                                                                |
| **2.0** | Memoria conversacional, trazabilidad visible, metadatos e integración con APIs oficiales.                          |
| **3.0** | Plataforma de apoyo a emergencias con perfiles de usuario y administrador, y motor de protocolos basado en reglas. |

> **Nota:** Las funcionalidades descritas para las versiones 2.0 y 3.0 corresponden al roadmap de evolución del proyecto y no forman parte de la implementación actual.

---

## 5. Ciclo de interacción con ALESSIA

![ciclo de funcionamiento](docs/README/diagrams/diagrams_ciclo_conversacional.png)
---

## 6. ALESSIA en acción

docs/README/screenshots/screeshot_saludo_inicial.png


Captura 2: Pregunta y respuesta.
Pendiente screenshot de conversación

---
## 7. Arquitectura del sistema

**ALESSIA** utiliza una arquitectura modular organizada en capas, donde cada componente tiene una responsabilidad específica. Esta separación permite mantener el sistema claro, facilitar las pruebas y favorecer su evolución futura.


### Capas de Arquitectura

![Capas de Arquitectura](docs/README/diagrams/diagrama_capas_de_arquitectura.png)


---
## 8. Flujo del pipeline RAG

![Flujo de Procesamiento RAG](docs/README/diagrams/diagrama_flujo_de_procesamiento_RAG.png)


---

## 9. Estructura del proyecto

La estructura del proyecto sigue una separación de responsabilidades que permite mantener el código modular, facilitar las pruebas y favorecer la evolución futura de ALESSIA.
```
ALESSIA/
├── app/
│   ├── assets/
│   │   ├── avatars/
│   │   ├── images/
│   │   └── logo/
│   │       
│   ├── components/
│   │   └── chat.py
│   ├── bootstrap.py
│   ├── config.py
│   └── streamlit_app.py
├── data/
│   ├── processed/
│   │   └── Plan-Comunal-de-Emergencia-2025-2.json
│   ├── raw/
│   │   ├── muni_valdivia/
│   │   │   └── planes/
│   │   │       └── Plan-Comunal-de-Emergencia-2025-2.pdf
│   │   └── test/
│   │       └── test_plan_comunal.pdf
│   └── vector_store/
│       ├── 059c90cb-9bcf-4cc3-815b-206ba132aef2/
│       │   ├── data_level0.bin
│       │   ├── header.bin
│       │   ├── length.bin
│       │   └── link_lists.bin
│       └── chroma.sqlite3
├── docs/
│   └── README/
│       ├── diagrams/
│       ├── infographics/
│       ├── logo/
│       └── screenshots/
│          
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_embeddings_vector_store.ipynb
│   ├── 03_retrieval.ipynb
│   ├── 04_reranking.ipynb
│   ├── 05_generation_validation.ipynb
│   └── 06_streamlit_app.ipynb
├── src/
│   ├── ingestion/
│   │   ├── loaders.py
│   │   └── scraper.py
│   ├── models/
│   │   ├── _init_.py
│   │   ├── chunk.py
│   │   └── document.py
│   ├── processing/
│   │   ├── chunker.py
│   │   ├── cleaner.py
│   │   ├── embedder.py
│   │   ├── generation.py
│   │   ├── llm_client.py
│   │   ├── prompt_builder.py
│   │   ├── reranker.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── agent_service.py
│   └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_agent_service.py
│   ├── test_bootstrap.py
│   ├── test_chat.py
│   ├── test_chunk.py
│   ├── test_cleaner.py
│   ├── test_embedder.py
│   ├── test_generation_integration.py
│   ├── test_generation.py
│   ├── test_loaders.py
│   ├── test_prompt_builder.py
│   ├── test_reranker.py
│   ├── test_retriever.py
│   └── test_vector_store.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```
---
## 10. Tecnologías utilizadas

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)[![Sentence Transformers](https://img.shields.io/badge/Sentence_Transformers-Embeddings-orange)](https://www.sbert.net/)[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Database-purple)](https://www.trychroma.com/)[![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM_API-black)](https://openrouter.ai/)[![Pytest](https://img.shields.io/badge/Pytest-Testing-green?logo=pytest)](https://docs.pytest.org/)




| Tecnología            | Uso en ALESSIA               |
| --------------------- | ---------------------------- |
| Python                | Lenguaje principal           |
| Streamlit             | Interfaz conversacional      |
| Sentence Transformers | Embeddings y reranking       |
| ChromaDB              | Almacenamiento vectorial     |
| OpenRouter            | Acceso al modelo de lenguaje |
| Pytest                | Pruebas automatizadas        |


---
## 11. Características implementadas (Versión 1.0)

### Funcionalidades existentes
ALESSIA cuenta actualmente con una versión 1.0 funcional que implementa un pipeline RAG completo para responder consultas utilizando información proveniente de documentos institucionales oficiales.

![Diagrama de Funcionalidades Implementadass 1.0](docs/README/diagrams/diagrama_funciones_implementadas.png)

---

## 12. Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/marelycarcamo/Challenge-AluraAgente-ONE-IA-FOR-TECH.git
cd Challenge-AluraAgente-ONE-IA-FOR-TECH
```
### 2. Crear y activar el entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En MacOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la API KEY

Crear un archivo .env en la raíz del proyecto, tomando como referencia .env.example:
```env
OPENROUTER_API_KEY=tu_api_key
```

### 5. Ejecutar ALESSIA

```bash
streamlit run app/streamlit_app.py
```

---

## 13. Roadmap

ALESSIA está diseñada para evolucionar progresivamente desde un asistente documental basado en RAG hacia una plataforma inteligente de apoyo a la gestión del riesgo de desastres.

![Roadmap](docs/README/diagrams/diagrama_roadmap.png)

---


## 14. Author & Licence

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Marely_Cárcamo-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marely/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
