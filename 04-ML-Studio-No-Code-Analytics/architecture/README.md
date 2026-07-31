# ML Studio: Architecture & Compute Decoupling

This directory documents the technical architecture, execution worker decoupling, and compute resource management for ML Studio.

## 1. Architecture Overview

ML Studio splits real-time HTTP interaction from long-running, CPU/GPU intensive machine learning tasks using an asynchronous task queue architecture.

```mermaid
graph TD
    Client[Next.js Web UI] -->|HTTP REST & SSE| API[FastAPI Web Server]
    API -->|Metadata Queries| DB[(PostgreSQL Database)]
    API -->|Save Files| S3[(S3 / Local Media Store)]
    API -->|Dispatch Jobs| Redis[(Redis Broker & Task Queue)]
    
    subgraph Worker Cluster (Celery)
        Redis --> Worker1[Data Profiling Worker]
        Redis --> Worker2[Tabular ML Worker - XGBoost/SKLearn]
        Redis --> Worker3[Time-Series Worker - Prophet/ARIMA]
        Redis --> Worker4[Deep Learning Worker - PyTorch/BERT]
    end

    Worker1 --> S3
    Worker2 --> S3
    Worker3 --> S3
    Worker4 --> S3
    
    Worker1 --> API
    Worker2 --> API
    Worker3 --> API
    Worker4 --> API
```

## 2. Resource Management & Memory Limits

1. **Dataset Memory Limits:** Datasets over 500MB are chunked using Polars/Pandas streaming to prevent Out-Of-Memory (OOM) failures on worker nodes.
2. **Worker Timeouts:** Model training tasks have hard timeouts (default: 15 minutes) enforced by Celery task control to prevent rogue hyperparameter loops from locking worker CPU cores.
3. **Model Serialization:** Trained models are serialized using `joblib` or `onnxruntime` and cached in S3 with unique artifact hashes.
