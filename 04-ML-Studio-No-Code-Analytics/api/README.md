# ML Studio: API Reference Specifications

This document outlines the primary REST and SSE endpoints for dataset management, model training, evaluation metrics, and inference.

## 1. Authentication Header
All protected endpoints require JWT authorization:
`Authorization: Bearer <JWT_TOKEN>`

## 2. API Endpoint Specifications

### 2.1. Upload & Dataset Analysis
#### `POST /api/v1/datasets/upload`
* **Description:** Upload a raw dataset (CSV/XLSX) for schema detection.
* **Payload:** `multipart/form-data` with `file`.
* **Response (201 Created):**
  ```json
  {
    "dataset_id": "8f3b2a1c-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
    "file_name": "customer_churn.csv",
    "row_count": 10000,
    "column_count": 12,
    "schema": {
      "customer_id": {"type": "string", "missing": 0},
      "tenure": {"type": "integer", "missing": 12},
      "monthly_charges": {"type": "float", "missing": 0},
      "churn": {"type": "boolean", "missing": 0}
    }
  }
  ```

### 2.2. Model Training Launch
#### `POST /api/v1/train`
* **Description:** Trigger multi-model background training.
* **Payload:**
  ```json
  {
    "experiment_id": "exp_998877",
    "target_column": "churn",
    "selected_models": ["LogisticRegression", "RandomForest", "XGBoost"],
    "preprocessing": {
      "imputation": "median",
      "encoding": "onehot",
      "scaling": "standard"
    }
  }
  ```
* **Response (202 Accepted):**
  ```json
  {
    "task_id": "task_train_123456",
    "status": "QUEUED",
    "sse_stream_url": "/api/v1/train/status/task_train_123456"
  }
  ```

### 2.3. Inference & Prediction
#### `POST /api/v1/predict/single`
* **Description:** Run a single-row inference against a trained model artifact.
* **Payload:**
  ```json
  {
    "model_run_id": "mr_445566",
    "features": {
      "tenure": 24,
      "monthly_charges": 65.5,
      "contract": "Month-to-month"
    }
  }
  ```
* **Response (200 OK):**
  ```json
  {
    "prediction": "Churn",
    "probability": 0.842,
    "shap_values": {
      "monthly_charges": 0.35,
      "tenure": -0.12
    }
  }
  ```
