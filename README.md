
# 🚀 Agentic AI Pipeline (Microservices + RAG)

## 📌 Overview

This project implements a **scalable Agentic AI system** using a **microservices architecture** with **Retrieval-Augmented Generation (RAG)**.

It integrates:
- LLM (Google Gemini)
- Embeddings
- Vector database (Qdrant)

The system enables **semantic search + context-aware responses** and is designed with a strong focus on:

- Modularity
- Scalability
- Clean architecture
- Real-world engineering practices

---

# 🧠 Architecture

## 🔄 End-to-End Flow

```text
Client
 ↓
API Gateway
 ↓
Agent Service (LLM + Orchestration)
 ↓
RAG Service (Embedding + Retrieval)
 ↓
Vector DB (Qdrant)
 ↓
Context → LLM → Response
````

---

## 🧩 Service Breakdown

### 🔹 API Gateway

* Entry point for all requests
* Handles routing and error handling

### 🔹 Agent Service

* Calls RAG service for context
* Builds prompt
* Interacts with Gemini LLM

### 🔹 RAG Service

* Generates embeddings
* Stores and retrieves vectors (Qdrant)
* Applies filtering and ranking
* Builds context for LLM

---

# 📦 Data Flow

```text
Query
 → Embedding
 → Vector Search (Top-K)
 → Score Filtering
 → Context Building
 → LLM Prompt
 → Response
```

---

# ⚙️ Tech Stack

* **Backend:** FastAPI
* **LLM:** Google Gemini (`gemini-2.5-flash`)
* **Embeddings:** Gemini (`gemini-embedding-001`)
* **Vector DB:** Qdrant
* **Architecture:** Microservices
* **Config:** Centralized (`.env` + settings)

---

# ✅ Features

## 🔹 Core

* API Gateway routing
* Agent Service with LLM integration
* RAG Service (fully decoupled)
* Qdrant vector search
* Embedding pipeline

## 🔹 RAG Enhancements

* Top-K retrieval
* Score-based filtering
* Context builder
* Prompt injection

## 🔹 Engineering Practices

* Centralized configuration
* Decision logging (`docs/decision.md`)
* Clean service boundaries
* Config-driven tuning

---

# 🧪 API Endpoints

## 🔹 API Gateway

```http
POST /query
```

---

## 🔹 Agent Service

```http
POST /generate
```

---

## 🔹 RAG Service

```http
POST /store
POST /retrieve
```

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/firrexguptaji/agentic-ai-pipeline.git
cd agentic-ai-pipeline
```

---

## 2. Setup Environment

Create `.env` file:

```env
# LLM
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-2.5-flash

# Embedding
EMBEDDING_MODEL=models/gemini-embedding-001

# Qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=documents
VECTOR_SIZE=3072

# Services
AGENT_SERVICE_URL=http://localhost:8001/generate
RAG_SERVICE_URL=http://localhost:8002

# Config
REQUEST_TIMEOUT=15

# RAG Tuning
RETRIEVAL_TOP_K=5
FINAL_TOP_K=2
SCORE_THRESHOLD=0.7
MAX_SOURCES=2
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

## 5. Run Services

### API Gateway

```bash
uvicorn services.api_gateway.main:app --port 8000 --reload
```

### Agent Service

```bash
uvicorn services.agent_service.main:app --port 8001 --reload
```

### RAG Service

```bash
uvicorn services.rag_service.main:app --port 8002 --reload
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
│           ├── embedding/
│           ├── vector_db/
│           ├── retrieval/
│           └── context/
│
├── shared/
│   └── config/
│
├── docs/
│   └── decision.md
```

---

# 📊 Current Status

* ✅ Embedding pipeline
* ✅ Vector DB integration
* ✅ Retrieval system (Top-K + filtering)
* ✅ Context building
* ✅ RAG microservice architecture
* 🔄 Next: Document ingestion & chunking

---

# 🧠 Key Design Decisions

* Dedicated `rag_service` for retrieval logic
* Centralized configuration for tuning
* Separation of retrieval and reasoning layers
* Incremental system evolution

See: `docs/decision.md`

---

# 🔮 Future Improvements

* Document ingestion pipeline (PDF → chunks → embeddings)
* Reranking layer for improved retrieval
* Hybrid search (vector + keyword)
* Observability (logging, tracing)
* Streaming responses
* Multi-agent workflows

---

# 🧠 Learning Highlights

This project demonstrates:

* AI system design (LLM + RAG)
* Microservices architecture
* Vector databases & semantic search
* Production-style configuration
* Incremental engineering approach

---

# 📌 Author

Built as part of continuous exploration in:

**AI Systems Design + Backend Engineering**

````

---

# 🚀 What You Just Did

This README now reflects:

```text
not just code → but system design
````

---


