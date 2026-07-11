import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_llm(
    query,
    context
):

    prompt = f"""

    Context:

    {context}

    Question:

    {query}

    """

    response = (
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
    )

    return (
        response
        .choices[0]
        .message.content
    )