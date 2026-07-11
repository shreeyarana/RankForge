import numpy as np

from .embeddings import embed
from .faiss_store import (
    index,
    documents
)

from .document_builder import (
    generate_documents
)


def build_index():

    docs = generate_documents()

    vectors = []

    documents.clear()

    for doc in docs:

        vector = embed(
            doc["content"]
        )

        vectors.append(vector)

        documents.append(doc)

    index.add(
        np.array(
            vectors,
            dtype=np.float32
        )
    )