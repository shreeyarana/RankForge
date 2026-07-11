from .retriever import retrieve
from .llm import ask_llm


def rag_query(query):

    docs = retrieve(query)

    context = "\n".join(
        d["content"]
        for d in docs
    )

    return ask_llm(
        query,
        context
    )