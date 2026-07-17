"""
Archivo: reranker.py

Módulo:
Procesamiento (Processing)

Objetivo:
Reordenar los fragmentos recuperados durante la etapa de Retrieval
según su relevancia para la consulta del usuario.

Descripción:
Este módulo aplica un modelo CrossEncoder para recalcular la
relevancia de los fragmentos recuperados mediante búsqueda
semántica. El objetivo es priorizar aquellos chunks que aportan
el contexto más útil para la generación de respuestas dentro del
pipeline RAG.

Proyecto: ALESSIA

"""

from sentence_transformers import CrossEncoder


def rerank_chunks(
    query: str,
    retrieval_results: dict,
    model: CrossEncoder,
    top_k: int = 3,
) -> list[dict]:
    """
    Reordena los fragmentos recuperados durante la etapa de Retrieval
    según su relevancia para la consulta del usuario.

    Para cada fragmento recuperado se calcula un nuevo puntaje de
    relevancia utilizando un modelo CrossEncoder. Posteriormente,
    los resultados se ordenan de mayor a menor puntaje y se
    devuelven únicamente los fragmentos mejor posicionados.

    Args:
        query:
            Consulta realizada por el usuario.

        retrieval_results:
            Resultados obtenidos desde ChromaDB.

        model:
            Modelo CrossEncoder utilizado para calcular la
            relevancia entre la consulta y cada fragmento.

        top_k:
            Cantidad máxima de fragmentos a retornar.

    Returns:
        Lista de diccionarios con los fragmentos reordenados.
    """

    documents = retrieval_results["documents"][0]
    metadatas = retrieval_results["metadatas"][0]

    # Construir los pares (consulta, documento)
    sentence_pairs = [
        (query, document)
        for document in documents
    ]

    # Calcular el puntaje de relevancia
    scores = model.predict(sentence_pairs)

    # Asociar documento, metadata y score
    reranked_results = [
        {
            "document": document,
            "metadata": metadata,
            "score": float(score),
        }
        for document, metadata, score in zip(
            documents,
            metadatas,
            scores,
        )
    ]

    # Ordenar de mayor a menor relevancia
    reranked_results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    return reranked_results[:top_k]