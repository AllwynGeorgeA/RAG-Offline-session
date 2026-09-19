import os
import streamlit as st

from rag.pipeline import RAGPipeline


st.set_page_config(
    page_title="Hybrid RAG",
    page_icon="🧠",
    layout="wide"
)


st.title("🧠 Hybrid RAG")
st.write(
    "FAISS + BM25 + Re-Ranker + Neo4j + OpenAI"
)


file_path = "data/documents/spotify_web_app_architecture.pdf"


if not os.path.exists(file_path):

    st.error(
        f"Document not found: {file_path}"
    )

    st.stop()


@st.cache_resource
def load_pipeline():

    return RAGPipeline(file_path)


pipeline = load_pipeline()


query = st.text_input(
    "Ask a question about the document:"
)


if st.button("Ask"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching..."):

            result = pipeline.ask(query)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Retrieved Sources")

        for i, source in enumerate(
            result["sources"],
            start=1
        ):

            with st.expander(
                f"Source {i}"
            ):

                st.write(source)