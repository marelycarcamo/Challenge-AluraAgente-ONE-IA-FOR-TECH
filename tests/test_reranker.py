from unittest.mock import MagicMock

from src.processing.reranker import rerank_chunks


def test_rerank_chunks_orders_results_by_score():
    """Verifica que los fragmentos se ordenen por relevancia."""

    retrieval_results = {
        "documents": [[
            "Documento A",
            "Documento B",
            "Documento C",
        ]],
        "metadatas": [[
            {"page": 1},
            {"page": 2},
            {"page": 3},
        ]],
    }

    model = MagicMock()

    model.predict.return_value = [
        0.20,
        0.95,
        0.60,
    ]

    results = rerank_chunks(
        query="consulta",
        retrieval_results=retrieval_results,
        model=model,
        top_k=2,
    )

    model.predict.assert_called_once()

    assert len(results) == 2

    assert results[0]["document"] == "Documento B"
    assert results[0]["score"] == 0.95

    assert results[1]["document"] == "Documento C"
    assert results[1]["score"] == 0.60