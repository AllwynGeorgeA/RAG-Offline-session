# 🧠 Hybrid RAG — FAISS + BM25 + Neo4j

A practical **Hybrid Retrieval-Augmented Generation (RAG)** application built with Streamlit.

This project combines **semantic search, keyword search, re-ranking, and Knowledge Graph retrieval** to provide more relevant and grounded answers from uploaded text documents.

---

## 🚀 Project Overview

Traditional RAG usually depends mainly on vector similarity search.

This project uses a **Hybrid RAG architecture**:

```text
                    User Question
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
        FAISS Vector Search       BM25 Search
        Semantic Retrieval       Keyword Retrieval
              │                       │
              └───────────┬───────────┘
                          ▼
                  Hybrid Retrieval
                          │
                          ▼
                      Re-Ranker
                          │
                          ▼
                   Relevant Context
                          │
                    ┌─────┴─────┐
                    ▼           ▼
                 Neo4j       Documents
              Knowledge Graph   Context
                    │           │
                    └─────┬─────┘
                          ▼
                       OpenAI
                          │
                          ▼
                  NeMo Guardrails
                          │
                          ▼
                    Final Answer
                          │
                          ▼
                       DeepEval
```

---

# 🎯 Project Goal

The goal of this project is to understand and implement a complete Hybrid RAG pipeline using:

* Semantic retrieval
* Keyword retrieval
* Hybrid retrieval
* Re-ranking
* Knowledge Graph retrieval
* LLM-based answer generation
* Guardrails
* RAG evaluation

The application is designed to answer questions using information from the provided documents while reducing unsupported or hallucinated answers.

---

# 🛠️ Tech Stack

| Technology                | Purpose                       |
| ------------------------- | ----------------------------- |
| **Streamlit**             | User interface                |
| **Python**                | Application development       |
| **Hugging Face**          | Text embeddings               |
| **FAISS**                 | Vector database               |
| **BM25**                  | Keyword-based retrieval       |
| **Sentence Transformers** | Re-ranking                    |
| **Neo4j**                 | Knowledge Graph               |
| **OpenAI**                | Answer generation             |
| **NeMo Guardrails**       | Security and response control |
| **DeepEval**              | RAG evaluation                |

---

# 📁 Project Structure

```text
hybrid-rag/
│
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   └── documents/
│       └── spotify_web_app_architecture.txt
│
├── vectorstore/
│
├── indexes/
│
├── graph/
│   ├── neo4j_graph.py
│   └── graph_retriever.py
│
├── rag/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── bm25_retriever.py
│   ├── hybrid_retriever.py
│   ├── reranker.py
│   ├── generator.py
│   └── pipeline.py
│
├── guardrails/
│   ├── config.yml
│   └── rails.co
│
└── evaluation/
    └── evaluate.py
```

---

# 🔄 How the Application Works

## 1. Document Loading

The application reads the text document from:

```text
data/documents/
```

Example:

```text
spotify_web_app_architecture.txt
```

---

## 2. Text Chunking

Large documents are divided into smaller chunks.

```text
Document
   ↓
Text
   ↓
Chunks
```

This makes retrieval more efficient.

---

## 3. Hugging Face Embeddings

Each chunk is converted into a numerical vector.

```text
Text Chunk
    ↓
Hugging Face Embedding Model
    ↓
Vector
```

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

## 4. FAISS Vector Search

The vectors are stored in FAISS.

When a user asks a question, FAISS searches for chunks with similar semantic meaning.

```text
Question
   ↓
Embedding
   ↓
FAISS
   ↓
Relevant Chunks
```

---

## 5. BM25 Keyword Search

BM25 performs keyword-based retrieval.

For example:

```text
Question:
"What database is used by the application?"
```

BM25 can identify chunks containing terms such as:

```text
database
PostgreSQL
MongoDB
storage
```

---

## 6. Hybrid Retrieval

FAISS and BM25 results are combined.

```text
FAISS
  +
BM25
  ↓
Hybrid Results
```

This gives the system both:

* Semantic understanding
* Exact keyword matching

---

# 🎯 7. Re-Ranking

The initial hybrid retrieval can return several candidate chunks.

The re-ranker scores those chunks against the user's question.

```text
Hybrid Results
      ↓
   Re-Ranker
      ↓
Most Relevant Chunks
```

The final top chunks are passed to the LLM.

---

# 🕸️ 8. Neo4j Knowledge Graph

Neo4j stores entities and relationships.

Example:

```text
Spotify
   │
   ├── uses → React
   │
   ├── uses → FastAPI
   │
   └── uses → PostgreSQL
```

This allows the application to retrieve relationship-based information.

---

# 🤖 9. OpenAI

The selected context is sent to the OpenAI model.

The model is instructed to answer only using the retrieved information.

```text
Question
   +
Retrieved Context
   ↓
OpenAI
   ↓
Answer
```

If sufficient information is not available, the system should respond:

```text
I couldn't find enough information in the provided documents.
```

---

# 🚧 10. NeMo Guardrails

NeMo Guardrails is used to add control around the AI interaction.

The purpose is to help prevent:

* Unsafe requests
* Prompt manipulation
* Unsupported responses
* Unwanted conversational behavior

---

# 📊 11. DeepEval

DeepEval is used to evaluate the RAG application.

Important evaluation areas include:

```text
Faithfulness
Answer Relevancy
Context Relevancy
```

Example:

```text
Question
   ↓
RAG Application
   ↓
Answer
   ↓
DeepEval
   ↓
Evaluation Metrics
```

---

# ⚙️ Installation

## Step 1 — Clone the repository

```cmd
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project:

```cmd
cd hybrid-rag
```

---

## Step 2 — Create virtual environment

```cmd
python -m venv venv
```

Activate it:

```cmd
venv\Scripts\activate
```

---

## Step 3 — Install dependencies

```cmd
python -m pip install --upgrade pip
```

Then:

```cmd
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_neo4j_password
```

### Important

Never upload `.env` to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
vectorstore/
indexes/
```

---

# ▶️ Run the Application

Activate the environment:

```cmd
venv\Scripts\activate
```

Run Streamlit:

```cmd
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🧪 Example Questions

After starting the application, ask questions related to the uploaded document.

Example:

```text
What technologies are used in the architecture?
```

```text
What is the role of FastAPI?
```

```text
Which database is used?
```

```text
How does the frontend communicate with the backend?
```

---

# 🛡️ Hallucination Protection

The application follows a simple rule:

```text
Retrieved Evidence
       ↓
    Enough?
    /      \
  YES       NO
   ↓         ↓
Answer    Say that the
          information
          wasn't found
```

The LLM should not invent information that is not supported by the retrieved context.

---

# 🧩 RAG Components

## Basic RAG

```text
Question
   ↓
Vector Search
   ↓
Context
   ↓
LLM
   ↓
Answer
```

## Hybrid RAG

```text
Question
   ↓
 ┌─────────────┐
 │             │
 ▼             ▼
FAISS        BM25
 │             │
 └──────┬──────┘
        ▼
 Hybrid Retrieval
        ↓
    Re-Ranker
        ↓
    Context
        ↓
      LLM
        ↓
     Answer
```

## Hybrid RAG + Knowledge Graph

```text
Question
   ↓
FAISS + BM25
   ↓
Hybrid Retrieval
   ↓
Re-Ranker
   ↓
Document Context
   +
Neo4j Relationships
   ↓
OpenAI
   ↓
Guardrails
   ↓
Final Answer
```

---

# 🧠 What I Learned

Through this project, I practiced:

* RAG architecture
* Text chunking
* Embeddings
* Vector databases
* FAISS
* BM25
* Hybrid retrieval
* Re-ranking
* Knowledge Graphs
* Neo4j
* LLM integration
* Guardrails
* RAG evaluation
* Streamlit application development

---

# 🗺️ Development Roadmap

### Phase 1 — Basic RAG

```text
TXT
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
OpenAI
```

### Phase 2 — Hybrid RAG

```text
FAISS
 +
BM25
 ↓
Hybrid Retrieval
```

### Phase 3 — Re-Ranking

```text
Hybrid Retrieval
 ↓
Re-Ranker
 ↓
Top Context
```

### Phase 4 — Knowledge Graph

```text
Neo4j
 ↓
Entity + Relationship Retrieval
```

### Phase 5 — Safety

```text
NeMo Guardrails
```

### Phase 6 — Evaluation

```text
DeepEval
```

---

# 🐛 Debugging Approach

The project is developed step by step.

```text
Build
 ↓
Run
 ↓
Error
 ↓
Debug
 ↓
Fix
 ↓
Run Again
```

If the same error appears repeatedly:

```text
Error
 ↓
Ask AI
 ↓
Try Fix
 ↓
Error Again
 ↓
Ask AI Again
 ↓
Developer life officially started 💀😂
```

---

# 🚀 Future Improvements

Possible future improvements:

* PDF document support
* Multiple document upload
* Metadata filtering
* Better hybrid scoring
* Advanced query rewriting
* Better entity extraction
* Automatic Neo4j graph construction
* Advanced NeMo Guardrails
* Automated DeepEval test datasets
* Chat history
* Source citations
* Production deployment

---

# 📌 Key Takeaway

This project demonstrates how different retrieval techniques can work together:

```text
FAISS
→ Understand meaning

BM25
→ Find exact keywords

Re-Ranker
→ Select the most relevant chunks

Neo4j
→ Understand relationships

OpenAI
→ Generate the answer

NeMo Guardrails
→ Control the interaction

DeepEval
→ Measure RAG quality
```

The main idea is:

> **Better retrieval → Better context → Better grounded answers**

---

## 👨‍💻 Project

**Hybrid RAG Application**

Built as part of my Generative AI learning journey to understand and implement advanced RAG architectures using practical tools and real-world workflows.
