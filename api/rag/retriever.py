import numpy as np

from .embeddings import embed

from .faiss_store import (
    index,
    documents
)


def retrieve(
    query,
    k=5
):

    query_vector = np.array(
        [embed(query)],
        dtype=np.float32
    )

    distances, indices = (
        index.search(
            query_vector,
            k
        )
    )

    results = []

    for idx in indices[0]:

        if idx < len(documents):

            results.append(
                documents[idx]
            )

    return results