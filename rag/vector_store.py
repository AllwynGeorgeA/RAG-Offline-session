from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from rag.embeddings import get_embeddings


VECTORSTORE_PATH = "vectorstore/faiss_index"


def create_vectorstore(chunks):

    embeddings = get_embeddings()

    documents = [
        Document(
            page_content=chunk,
            metadata={"source": "uploaded_document"}
        )
        for chunk in chunks
    ]

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    vectorstore.save_local(VECTORSTORE_PATH)

    return vectorstore


def load_vectorstore():

    embeddings = get_embeddings()

    return FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )