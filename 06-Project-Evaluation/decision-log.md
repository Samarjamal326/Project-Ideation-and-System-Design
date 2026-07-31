# Architectural Decision Records (ADR) & Final Selection Decision Log

This document provides formal Architectural Decision Records (ADRs) and customized project selection recommendations tailored to different team compositions, skill sets, and career objectives.

---

## 1. Architectural Decision Records (ADR)

### ADR-01: Multi-Model Evaluation Strategy for Stock Forecasting & ML Studio
* **Status:** Approved
* **Context:** Projects 04 and 05 require comparing multiple algorithms (e.g., Random Forest vs XGBoost vs Prophet vs TFT).
* **Decision:** Implement standardized evaluation pipelines using JSON metrics payloads and Plotly dynamic overlays. For Project 05, time-series metrics must report RMSE, MAPE, and Directional Accuracy. For Project 04, classification metrics must report Accuracy, F1, ROC-AUC, and Confusion Matrix.
* **Consequences:** Ensures fair benchmarking across traditional statistical models and deep learning sequence architectures.

### ADR-02: Asynchronous Worker Architecture (Celery + Redis)
* **Status:** Approved
* **Context:** Machine learning training (Projects 04 & 05) and developer scraping (Project 01) exceed standard HTTP request timeouts (30s).
* **Decision:** Decouple FastAPI web servers from long-running execution tasks using Celery worker pools backed by Redis brokers. Progress must be broadcast to Next.js clients via Server-Sent Events (SSE) or WebSockets.
* **Consequences:** Prevents web server worker blocking and enables seamless progress bar UI feedback.

---

## 2. Selection Recommendation Guidelines by Team Profile

Select your project based on your team's core background, career aspirations, and project goals:

```
                  ┌────────────────────────────────────────────────────────┐
                  │ What is your primary project goal or career focus?     │
                  └───────────────────────────┬────────────────────────────┘
                                              │
         ┌──────────────────┬─────────────────┼──────────────────┬──────────────────┐
         ▼                  ▼                 ▼                  ▼                  ▼
  [ Deep Learning &  [ Full-Stack Web  [ Quantitative   [ Systems & High   [ Data Science &
   Developer AI ]     & Events ]        Finance & AI ]    Performance ]      No-Code ML ]
         │                  │                 │                  │                  │
         ▼                  ▼                 ▼                  ▼                  ▼
    Select 01:         Select 02:        Select 05:         Select 03:         Select 04:
    DevSphere        Campus Events    Stock Forecasting   Startup Incubator    ML Studio
```

### Profile A: AI / ML & Natural Language Processing Focus
* **Recommended Project:** **01-DevSphere** or **05-AI-Stock-Market-Forecasting**
* **Why:** Both projects maximize exposure to modern AI/ML patterns. DevSphere excels in Vector Search (`pgvector`), Embeddings (`SentenceTransformers`), and LLM Agent code reviews. Stock Forecasting excels in deep sequence architectures (Temporal Fusion Transformer, LSTM) and NLP financial news sentiment (FinBERT).

### Profile B: Quantitative Finance & Applied Analytics Focus
* **Recommended Project:** **05-AI-Stock-Market-Forecasting**
* **Why:** Combines financial engineering (TA-Lib technical indicators, Sharpe Ratio, VaR risk analytics) with deep learning sequence modeling and interactive Plotly financial candlestick charts.

### Profile C: Full-Stack Web & High-Concurrency Systems Focus
* **Recommended Project:** **02-Campus-Events-Platform**
* **Why:** Demonstrates mastery of transaction control, Redis distributed locks (Redlock), high-concurrency ticket queuing, WebSocket dynamic seating maps, and PDF certificate generation using a clean TypeScript stack (Next.js + NestJS).

### Profile D: Enterprise Microservices & B2B SaaS Focus
* **Recommended Project:** **03-Startup-Incubator-Platform**
* **Why:** Provides rare hands-on experience with Golang microservices, gRPC protocol buffers, multi-tenant database isolation, pitch deck OCR extraction, and legal document signing pipelines.

### Profile E: Data Engineering & AutoML Platforms Focus
* **Recommended Project:** **04-ML-Studio-No-Code-Analytics**
* **Why:** Covers 7 machine learning paradigms, automated data cleaning, feature engineering, worker queue isolation, explainable AI (SHAP), and model artifact exporting.

---

## 3. Master Recommendation & Conclusion

For teams seeking the **highest overall technical impact, resume value, and academic research paper novelty**, we recommend:

1. **Top Recommendation:** **05-AI-Stock-Market-Forecasting** (Score: 8.95 / 10)
2. **Runner-Up Recommendation:** **01-DevSphere** (Score: 8.85 / 10)

Both projects position students at the cutting edge of applied machine learning, system design, and modern web application development.
