# ML Studio: Architectural Diagrams & Process Flowcharts

This directory contains Mermaid process sequence diagrams and data pipeline blueprints for ML Studio.

## 1. End-to-End Model Training Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Business Analyst
    participant FE as Next.js Frontend
    participant API as FastAPI Backend
    participant DB as PostgreSQL
    participant Redis as Redis Queue
    participant Worker as Celery ML Worker
    participant S3 as S3 Storage

    User->>FE: Upload dataset.csv & select Target Column
    FE->>API: POST /api/v1/datasets/upload
    API->>S3: Save dataset.csv
    API->>DB: Insert dataset metadata
    API-->>FE: Return dataset_id & inferred schema
    
    User->>FE: Select models (XGBoost, Random Forest) & Click "Train"
    FE->>API: POST /api/v1/train
    API->>DB: Create Experiment & ModelRun records (Status: PENDING)
    API->>Redis: Enqueue Training Job
    API-->>FE: Return task_id & SSE stream endpoint

    Redis->>Worker: Pick up training job
    Worker->>S3: Fetch dataset.csv
    Worker->>Worker: Preprocess (Impute NaNs, One-Hot Encode)
    Worker->>Worker: Train XGBoost & Random Forest models
    Worker->>Worker: Compute Evaluation Metrics & SHAP values
    Worker->>S3: Save trained model artifacts (.pkl)
    Worker->>DB: Update ModelRun records (Status: COMPLETED, Metrics: JSON)
    Worker-->>API: Notify Job Complete via Redis PubSub
    API-->>FE: Push SSE "COMPLETED" event with metrics
    FE->>User: Render Interactive Model Comparison & ROC Curves
```

## 2. Real-Time Inference Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Business Analyst
    participant FE as Next.js Frontend
    participant API as FastAPI Backend
    participant S3 as S3 Storage

    User->>FE: Fill prediction form fields & Click "Predict"
    FE->>API: POST /api/v1/predict/single
    API->>S3: Load trained model artifact (.pkl / .onnx)
    API->>API: Apply fitted scaler & encoders to input features
    API->>API: Execute model.predict() & compute SHAP values
    API-->>FE: Return Prediction result & Feature Importances
    FE->>User: Display prediction badge & SHAP force plot
```
