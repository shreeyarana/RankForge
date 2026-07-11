import faiss

DIMENSION = 384

index = faiss.IndexFlatL2(
    DIMENSION
)

documents = []