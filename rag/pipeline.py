from rag.chunking import load_and_chunk
from rag.embeddings import get_embeddings
from rag.vector_store import create_vectorstore
from rag.hybrid_retriever import HybridRetriever
from rag.reranker import Reranker
from rag.generator import generate_answer


class RAGPipeline:

    def __init__(self, file_path):

        self.chunks = load_and_chunk(file_path)

        self.vectorstore = create_vectorstore(
            self.chunks
        )

        self.hybrid = HybridRetriever(
            self.vectorstore,
            self.chunks
        )

        self.reranker = Reranker()

    def ask(self, query):

        hybrid_results = self.hybrid.search(
            query,
            k=8
        )

        reranked_results = self.reranker.rerank(
            query,
            hybrid_results,
            top_k=4
        )

        answer = generate_answer(
            query,
            reranked_results
        )

        return {
            "answer": answer,
            "sources": reranked_results
        }