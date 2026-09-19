import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(query, context):

    if not context:
        return (
            "I couldn't find enough information "
            "in the provided documents."
        )

    context_text = "\n\n".join(context)

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question ONLY using the provided context.

If the answer cannot be found in the context,
say:

"I couldn't find enough information in the provided documents."

Do not invent facts.

CONTEXT:
{context_text}

QUESTION:
{query}

ANSWER:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content