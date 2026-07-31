# Comprehensive Comparison Table: All 5 System Proposals

This document provides a side-by-side comparative architectural breakdown of all five candidate projects across 10 critical technical vectors.

---

## 1. Multi-Project Technical Comparison Matrix

| Technical Vector | 01-DevSphere | 02-Campus-Events | 03-Startup-Incubator | 04-ML-Studio | 05-Stock-Forecasting |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Domain** | Developer Hiring & Collaboration | High-Concurrency Ticketing | Accelerator SaaS & Matching | No-Code ML Analytics | Quant AI Stock Forecasting |
| **Frontend Stack** | Next.js 14, React, Tailwind CSS | Next.js 14, React, Tailwind CSS | Next.js 14, React, Tailwind CSS | Next.js 14, Plotly.js, React | Next.js 14, Plotly.js, Lightweight Charts |
| **Backend Framework** | FastAPI (Python 3.11) | NestJS (Node.js / TypeScript) | Go / Fiber (Golang) + gRPC | FastAPI (Python 3.11) | FastAPI (Python 3.11) |
| **Primary Database** | PostgreSQL + `pgvector` | PostgreSQL + Redis Cache | PostgreSQL + Document Store | PostgreSQL (JSONB schema) | PostgreSQL + TimescaleDB |
| **AI / ML Stack** | PyTorch, SentenceTransformers | Tesseract OCR, Recommender | LangChain, PyPDF, LLM OCR | Scikit-Learn, XGBoost, PyTorch, SHAP | PyTorch (TFT), TensorFlow (LSTM), TA-Lib |
| **Asynchronous Engine** | Celery + Redis Task Queue | BullMQ + Redis Sorted Sets | Asynchronous Go Goroutines | Celery + Redis Worker Pool | Celery + Redis Worker Pool |
| **Real-Time Protocols** | WebSockets (FastAPI WS) | WebSockets (Socket.io) | SSE / WebSockets | SSE (Training progress) | WebSockets / Live polling |
| **Key Architectural Bottleneck**| Scraper rate limits & vector search latency | Concurrency race conditions on ticket checkout | Multi-tenant tenant data isolation | RAM OOM on large file uploads (>1GB) | Data non-stationarity & API rate limits |
| **Deployment Target** | AWS ECS Fargate, RDS pgvector | AWS Lambda + API Gateway | Kubernetes (EKS) / ECS | AWS ECS / GPU Worker Nodes | AWS ECS Fargate, Timescale Cloud |
| **Primary Output** | Dev compatibility score & PR summary | Verified QR ticket & PDF Certificate | Venture Match Score & NDA Doc | Trained `.pkl` artifact & SHAP report | Price target, Signal, Confidence Score |

---

## 2. Deep-Dive Comparative Dimension Summaries

### 2.1. Language & Framework Diversity
* **Python-Heavy Stack (Projects 01, 04, 05):** Ideal for teams targeting AI, Data Science, and Machine Learning careers. Leverages FastAPI's async capabilities and Python's rich ML library ecosystem.
* **TypeScript-Unified Stack (Project 02):** Minimizes context-switching between frontend and backend. NestJS provides robust enterprise dependency injection patterns.
* **Golang High-Performance Stack (Project 03):** Delivers ultra-low latency microservices with gRPC protocol buffers, ideal for teams wanting systems engineering exposure.

### 2.2. Persistence & Storage Paradigms
* **Vector Databases (Project 01):** Utilizes `pgvector` for high-dimensional embeddings cosine similarity search.
* **Time-Series Databases (Project 05):** Utilizes TimescaleDB hypertables for temporal price and indicator downsampling.
* **Transactional & Cache Lock Systems (Project 02):** Utilizes Redis distributed locks (Redlock) for race-condition prevention during concurrent ticket claims.
* **JSONB Schema Engine (Project 04):** Utilizes PostgreSQL GIN indexes on dynamic JSONB schema metadata and model run performance metrics.
* **Multi-Tenant Relational Store (Project 03):** Utilizes schema-per-tenant isolation for strict financial security.
