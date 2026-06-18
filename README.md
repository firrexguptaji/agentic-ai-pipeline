# 🚀 Agentic AI Pipeline (Microservices + RAG)

## 📌 Overview

This project implements a **scalable Agentic AI system** using a **microservices architecture** with **Retrieval-Augmented Generation (RAG)**.

It integrates:

* Google Gemini (LLM)
* Gemini Embeddings
* Qdrant Vector Database
* Automated Document Ingestion Pipeline

The system enables **semantic search and context-aware responses** while emphasizing:

* Modularity
* Scalability
* Clean architecture
* Production-oriented engineering practices

---

# 🧠 Architecture

## 🔄 End-to-End Flow

```text
                        +-----------------------+
                        |      API Gateway      |
                        +-----------+-----------+
                                    |
                                    v
                        +-----------------------+
                        |    Agent Service      |
                        | LLM + Orchestration   |
                        +-----------+-----------+
                                    |
                                    v
                        +-----------------------+
                        |      RAG Service      |
                        +-----------+-----------+
                                    |
              +---------------------+----------------------+
              |                                            |
              v                                            v
      Retrieval Pipeline                          Document Ingestion
              |                                            |
              v                                            v
      Embedding Service                           Document Loader
              |                                            |
              |                                     Text Chunker
              |                                            |
              +---------------------+----------------------+
                                    |
                                    v
                            Qdrant Vector DB
                                    |
                                    v
                           Context → Gemini → Response
```

---

# 🧩 Service Breakdown

## 🔹 API Gateway

* Entry point for all requests
* Routes client requests to backend services
* Centralized request handling

## 🔹 Agent Service

* Orchestrates AI workflow
* Retrieves context from RAG Service
* Builds prompts
* Sends prompts to Gemini
* Returns generated responses

## 🔹 RAG Service

Responsible for two independent pipelines:

### Retrieval

* Generate query embeddings
* Search Qdrant
* Score filtering
* Context construction

### Document Ingestion

* Load supported documents
* Split documents into chunks
* Generate embeddings
* Store vectors with metadata

---

# 📦 Data Flow

## Retrieval

```text
Query
 ↓
Embedding
 ↓
Vector Search
 ↓
Score Filtering
 ↓
Context Builder
 ↓
LLM Prompt
 ↓
Response
```

## Document Ingestion

```text
Document
 ↓
Loader
 ↓
Chunker
 ↓
Embedding Service
 ↓
Metadata Builder
 ↓
Qdrant
```

---

# ⚙️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini (`gemini-2.5-flash`)
* **Embeddings:** Gemini (`gemini-embedding-001`)
* **Vector Database:** Qdrant
* **Architecture:** Microservices
* **Configuration:** Centralized (`.env` + settings)

---

# ✅ Features

## 🔹 Core

* API Gateway
* Agent Service
* RAG Service
* Gemini integration
* Qdrant integration

## 🔹 Retrieval

* Embedding generation
* Top-K retrieval
* Score filtering
* Context building
* Prompt construction

## 🔹 Document Ingestion

* TXT document support
* Markdown document support
* Automatic document loading
* Configurable chunking
* Metadata generation
* Embedding generation
* Vector storage in Qdrant

## 🔹 Engineering Practices

* Centralized configuration
* Structured logging
* Request ID middleware
* Decision logging (`docs/decision.md`)
* Clean service boundaries
* Dependency injection

---

# 🧪 API Endpoints

## API Gateway

```http
POST /query
```

---

## Agent Service

```http
POST /generate
```

---

## RAG Service

```http
POST /store
POST /retrieve
POST /ingest
```

### `/ingest`

Uploads a supported document and automatically:

* Extracts text
* Splits into chunks
* Generates embeddings
* Stores vectors and metadata in Qdrant

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/firrexguptaji/agentic-ai-pipeline.git
cd agentic-ai-pipeline
```

---

## 2. Configure Environment

```env
# LLM
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash

# Embeddings
EMBEDDING_MODEL=models/gemini-embedding-001

# Qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=documents
VECTOR_SIZE=3072

# Services
AGENT_SERVICE_URL=http://localhost:8001/generate
RAG_SERVICE_URL=http://localhost:8002

# Configuration
REQUEST_TIMEOUT=15

# Retrieval
RETRIEVAL_TOP_K=5
FINAL_TOP_K=2
SCORE_THRESHOLD=0.7
MAX_SOURCES=2

# Chunking
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start Qdrant

```bash
docker-compose up -d
```

---

## 5. Start Services

### API Gateway

```bash
uvicorn services.api_gateway.main:app --reload --port 8000
```

### Agent Service

```bash
uvicorn services.agent_service.main:app --reload --port 8001
```

### RAG Service

```bash
uvicorn services.rag_service.main:app --reload --port 8002
```

---

# 📁 Project Structure

```text
.
├── services/
│   ├── api_gateway/
│   ├── agent_service/
│   │   └── core/
│   │       ├── llm.py
│   │       └── rag_client.py
│   │
│   └── rag_service/
│       ├── api/
│       └── core/
│           ├── context/
│           ├── embedding/
│           ├── ingestion/
│           │   ├── loader.py
│           │   ├── chunker.py
│           │   ├── pipeline.py
│           │   └── models.py
│           ├── retrieval/
│           └── vector_db/
│
├── shared/
│   ├── config/
│   ├── logging/
│   └── middleware/
│
├── docs/
│   └── decision.md
│
└── tests/
```

---

# 📊 Current Status

* ✅ Embedding pipeline
* ✅ Vector database integration
* ✅ Retrieval pipeline
* ✅ Context builder
* ✅ Document ingestion pipeline
* ✅ File upload endpoint
* ✅ Metadata support
* ✅ Integration testing

### 🚧 Next Milestone

* LLM fallback when retrieval returns no context

---

# 🧠 Key Design Decisions

* Dedicated RAG microservice
* Separation of retrieval and reasoning
* Dedicated document ingestion pipeline
* Config-driven architecture
* Dependency injection for shared services
* Incremental feature delivery

See:

```
docs/decision.md
```

---

# 🔮 Future Improvements

* PDF ingestion
* DOCX ingestion
* Recursive chunking
* Batch vector insertion
* Hybrid search
* Metadata filtering
* Reranking
* Streaming responses
* Multi-agent orchestration
* OpenTelemetry tracing

---

# 🧠 Learning Highlights

This project demonstrates:

* AI system design
* Retrieval-Augmented Generation
* Microservices architecture
* Semantic search
* Vector databases
* Production-style backend engineering
* Incremental architecture evolution

---

# 📌 Author

Built as part of continuous exploration in:

**AI Systems Design + Backend Engineering**
