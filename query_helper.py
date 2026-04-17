from typing import List, Optional, Dict, Any
from chromadb.api.models.Collection import Collection
import logging

logger = logging.getLogger("query_helper")


def perform_search(
    collection: Collection,
    query_texts: Optional[List[str]] = None,
    query_embeddings: Optional[List[List[float]]] = None,
    results: int = 10,
    where: Optional[Dict[str, Any]] = None,
    include: Optional[List[str]] = None,
):
    try:
        # ✅ Validate input
        if not query_texts and not query_embeddings:
            raise ValueError("Either query_texts or query_embeddings must be provided")

        if query_texts and query_embeddings:
            raise ValueError("Provide only one of query_texts or query_embeddings")

        if results <= 0:
            raise ValueError("results must be greater than 0")

        query_payload = {
            "n_results": results,
        }

        if where:
            query_payload["where"] = where

        if include:
            query_payload["include"] = include

        # ✅ Mode selection
        if query_texts:
            logger.debug(f"Searching using text queries: {len(query_texts)}")
            query_payload["query_texts"] = query_texts

        else:
            logger.debug(f"Searching using embeddings: {len(query_embeddings)}")
            query_payload["query_embeddings"] = query_embeddings

        return collection.query(**query_payload)

    except Exception as e:
        logger.exception(
            f"Search failed | texts={len(query_texts) if query_texts else 0}, "
            f"embeddings={len(query_embeddings) if query_embeddings else 0}"
        )
        raise RuntimeError("Error while performing search") from e