from rag.bm25_retriever import BM25Retriever


class HybridRetriever:

    def __init__(self, vectorstore, chunks):
        self.vectorstore = vectorstore
        self.bm25 = BM25Retriever(chunks)

    def search(self, query, k=5):

        vector_results = self.vectorstore.similarity_search(
            query,
            k=k
        )

        vector_chunks = [
            doc.page_content
            for doc in vector_results
        ]

        bm25_chunks = self.bm25.search(
            query,
            k=k
        )

        combined = []

        for chunk in vector_chunks + bm25_chunks:

            if chunk not in combined:
                combined.append(chunk)

        return combined