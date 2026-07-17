from unittest.mock import MagicMock, patch

from src.processing.retriever import retrieve_context


def test_retrieve_context_returns_documents():
    """Verifica que retrieve_context devuelva los fragmentos recuperados."""

    fake_results = {
        "documents": [[
            "Primer fragmento.",
            "Segundo fragmento.",
            "Tercer fragmento.",
        ]]
    }

    collection = MagicMock()
    model = MagicMock()

    with patch(
        "src.processing.retriever.search_chunks",
        return_value=fake_results,
    ) as mock_search:

        context = retrieve_context(
            query="consulta de prueba",
            collection=collection,
            model=model,
            k=3,
        )

        mock_search.assert_called_once_with(
            query="consulta de prueba",
            collection=collection,
            model=model,
            k=3,
        )

    assert context == [
        "Primer fragmento.",
        "Segundo fragmento.",
        "Tercer fragmento.",
    ]