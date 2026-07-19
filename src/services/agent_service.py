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

from sentence_transformers import CrossEncoder, SentenceTransformer

from chromadb.api.models.Collection import Collection


class AgentService:
    """
    Fachada del pipeline RAG.

    Esta clase coordina la ejecución del pipeline RAG,
    encapsulando los procesos de recuperación del contexto,
    reranking y generación de respuestas.

    La capa de presentación debe interactuar únicamente con
    esta clase, sin acceder directamente a los módulos internos
    del pipeline.
    """

    def __init__(
        self,
        collection: Collection,
        embedding_model: SentenceTransformer,
        reranker_model: CrossEncoder,
    ) -> None:
        """
        Inicializa el servicio con los componentes necesarios
        para ejecutar el pipeline RAG.

        Parameters
        ----------
        collection : Collection
            Colección persistente de ChromaDB.

        embedding_model : SentenceTransformer
            Modelo utilizado para generar embeddings de las consultas.

        reranker_model : CrossEncoder
            Modelo utilizado para reordenar los fragmentos recuperados.
        """

        self.collection = collection
        self.embedding_model = embedding_model
        self.reranker_model = reranker_model

    def ask(
        self,
        question: str,
    ) -> str:
        """
        Procesa una consulta utilizando el pipeline RAG.

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
        ranked_chunks = self._rerank_chunks(question, chunks)
        return self._generate_answer(question, ranked_chunks)

    def _retrieve_context(self, question: str):
        """Recupera los fragmentos más relevantes."""

        query_embedding = self.embedding_model.encode(question).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=5,
        )
        return results.get("documents", [[]])[0]

    def _rerank_chunks(self, question: str, chunks):
        """Reordena los fragmentos recuperados según su relevancia."""

        pairs = [(question, chunk) for chunk in chunks]
        scores = self.reranker_model.predict(pairs)
        ranked = sorted(zip(chunks, scores), key=lambda x: x[1], reverse=True)
        return [chunk for chunk, _ in ranked]

    def _generate_answer(self, question: str, ranked_chunks):
        """Genera una respuesta utilizando el contexto recuperado."""

        pass