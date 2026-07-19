"""
Archivo: agent_service.py

Módulo:
    src.services

Objetivo:
    Proporcionar una capa de servicio que actúe como fachada del pipeline
    RAG de ALESSIA, coordinando la recuperación del contexto, el proceso
    de reranking y la generación de respuestas.

Descripción:
    Este módulo encapsula la interacción entre la capa de presentación
    y los componentes internos del sistema, evitando que la interfaz
    conozca los detalles de implementación del pipeline RAG.

    AgentService recibe una consulta del usuario y orquesta la ejecución
    de los módulos de Retrieval, Reranking y Generation para obtener una
    respuesta fundamentada en los documentos oficiales disponibles.

Proyecto:
    ALESSIA
    Asistente basado en RAG para la gestión del riesgo de desastres
    en la comuna de Valdivia.
"""

from pathlib import Path

from chromadb.api.models.Collection import Collection
from sentence_transformers import CrossEncoder, SentenceTransformer

from src.processing.generation import generate_answer
from src.processing.reranker import rerank_chunks
from src.processing.retriever import retrieve_context
from src.processing.vector_store import get_or_create_collection


class AgentService:
    """
    Fachada del pipeline RAG.

    Esta clase coordina la ejecución del pipeline completo,
    desacoplando la interfaz de usuario de los módulos internos
    del sistema.
    """

    def __init__(
        self,
        collection: Collection,
        embedding_model: SentenceTransformer,
        reranker_model: CrossEncoder,
    ) -> None:
        """
        Inicializa el servicio con los componentes del pipeline.

        Parameters
        ----------
        collection : Collection
            Colección persistente de ChromaDB.

        embedding_model : SentenceTransformer
            Modelo utilizado para generar embeddings.

        reranker_model : CrossEncoder
            Modelo utilizado para realizar reranking.
        """

        self.collection = collection
        self.embedding_model = embedding_model
        self.reranker_model = reranker_model

    @classmethod
    def create(cls) -> "AgentService":
        """
        Crea una instancia completamente configurada de AgentService.

        Returns
        -------
        AgentService
            Servicio inicializado.
        """

        project_root = Path(__file__).parent.parent.parent

        vector_store_path = (
            project_root
            / "data"
            / "vector_store"
        )

        collection = get_or_create_collection(
            collection_name="alessia_collection",
            vector_store_path=vector_store_path,
        )

        embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        reranker_model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

        return cls(
            collection=collection,
            embedding_model=embedding_model,
            reranker_model=reranker_model,
        )

    def ask(
        self,
        question: str,
    ) -> str:
        """
        Ejecuta el pipeline RAG completo.

        Parameters
        ----------
        question : str
            Consulta realizada por el usuario.

        Returns
        -------
        str
            Respuesta generada por el modelo de lenguaje.
        """

        chunks = self._retrieve_context(question)

        ranked_chunks = self._rerank_chunks(
            question,
            chunks,
        )

        return self._generate_answer(
            question,
            ranked_chunks,
        )

    def _retrieve_context(
        self,
        question: str,
    ):
        """
        Recupera los fragmentos más relevantes para la consulta.
        """

        return retrieve_context(
            query=question,
            collection=self.collection,
            model=self.embedding_model,
            k=5,
        )

    def _rerank_chunks(
        self,
        question: str,
        chunks,
    ):
        """
        Reordena los fragmentos recuperados según su relevancia.
        """

        return rerank_chunks(
            query=question,
            chunks=chunks,
            model=self.reranker_model,
            top_k=3,
        )

    def _generate_answer(
        self,
        question: str,
        chunks,
    ) -> str:
        """
        Genera una respuesta utilizando el contexto recuperado.
        """

        return generate_answer(
            question=question,
            context=chunks,
        )