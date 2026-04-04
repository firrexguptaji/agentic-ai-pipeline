# 🚀 Agentic AI Pipeline (Microservices + RAG)

## 📌 Overview

This project implements a scalable **agentic AI pipeline** using a microservices architecture. It integrates LLMs, embeddings, and a vector database to enable **semantic search** and **Retrieval-Augmented Generation (RAG)**.

The system is designed with a strong focus on **modularity, scalability, and real-world engineering practices**, evolving incrementally from core pipeline to intelligent systems.

---

## 🧠 Architecture Flow

### 🔄 End-to-End Request Flow

```text
Client Request
     ↓
API Gateway (FastAPI)
     ↓
Agent Service
     ↓
[Step 1] Generate Embedding (Gemini)
     ↓
[Step 2] Query Vector DB (Qdrant)
     ↓
[Step 3 - Upcoming] Retrieve Context (Top-K Results)
     ↓
[Step 4 - Upcoming] Inject Context into LLM Prompt
     ↓
LLM (Gemini)
     ↓
Response → API Gateway → Client
```

---

### 🧩 Service Interaction

```text
services/api_gateway
    ↓
services/agent_service
    ├── core/llm.py
    ├── core/embedding/
    └── core/vector_db/

shared/config/settings.py (used across services)
```

---

### 📦 Data Flow

#### Current

```text
Query → Embedding → Store/Search → Results
```

#### After RAG

```text
Query → Embedding → Vector Search → Context → LLM → Response
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **LLM Provider:** Google Gemini
* **Embeddings:** Gemini Embedding API (`gemini-embedding-001`)
* **Vector Database:** Qdrant
* **Architecture:** Microservices
* **Config Management:** `.env` + centralized settings

---

## ✅ Features Implemented

* API Gateway with request routing
* Agent Service with LLM integration
* Embedding generation pipeline
* Vector storage and semantic search (Qdrant)
* Centralized configuration system
* Issue-driven development with Kanban tracking
* Decision logging (`docs/decision.md`)

---

## 🧪 API Endpoints

### 🔹 Query (Gateway)

```http
POST /query
```

### 🔹 Generate Embedding

```http
POST /embed
```

### 🔹 Store Data

```http
POST /store
```

### 🔹 Search Data

```http
POST /search
```

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone [<repo-url>](https://github.com/firrexguptaji/agentic-ai-pipeline/)
cd agentic-ai-pipeline
```

---

### 2. Setup Environment

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key
VECTOR_SIZE=3072

QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=documents
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start Qdrant

```bash
docker-compose up -d
```

---

### 5. Run Services

#### API Gateway

```bash
uvicorn services.api_gateway.main:app --reload --port 8000
```

#### Agent Service

```bash
uvicorn services.agent_service.main:app --reload --port 8001
```

---

## 📁 Project Structure

```text
.
├── services/
│   ├── api_gateway/
│   ├── agent_service/
│   │   ├── core/
│   │   │   ├── llm.py
│   │   │   ├── embedding/
│   │   │   └── vector_db/
│   └── rag_service/ (planned)
│
├── shared/
│   ├── config/
│   ├── schemas/
│   └── utils/
│
├── docs/
│   └── decision.md
│
├── tests/
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📊 Current Status

* ✅ Embedding pipeline complete
* ✅ Vector DB integration complete
* ✅ Semantic search working
* 🔄 RAG integration in progress

---

## 🧠 Key Design Decisions

* Centralized configuration for scalability
* Qdrant for efficient vector similarity search
* Gemini embeddings for unified ecosystem
* Modular service abstraction
* Incremental system evolution (build → validate → extend)

---

## 🔮 Future Improvements

* Full RAG pipeline (context injection + prompt structuring)
* Tool calling (multi-agent capabilities)
* Memory layer (conversation context)
* Observability (tracing, logging, metrics)
* Autoscaling strategies
* Document ingestion pipeline (PDF → embeddings)

---

## 🧠 Learning Focus

This project demonstrates:

* AI system design (LLM + RAG)
* Microservices architecture
* Vector databases and semantic search
* Real-world engineering workflows (Kanban, issue tracking)
* Incremental and scalable system development

---

## 📌 Author

Built as part of continuous learning and exploration in **AI system design and engineering**.
