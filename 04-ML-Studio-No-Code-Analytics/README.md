# ML Studio: No-Code Machine Learning Prediction & Analytics Platform
## System Design, Architecture, and Product Specification Document

---

## 1. Project Overview

### 1.1. Project Name & Tagline
* **Project Name:** ML Studio (No-Code Analytics Platform)
* **Tagline:** "Democratizing Machine Learning: Turn raw datasets into trained models, interactive analytics, and actionable forecasts without writing a line of code."

### 1.2. Problem Statement
Modern organizations generate vast volumes of structured tabular data, customer interaction logs, text feedback, and time-series metrics. However, harnessing this data for predictive modeling currently requires domain expertise in Python/R, statistical analysis, data cleaning, feature engineering, and model deployment pipelines.

#### Current Problems:
1. **High Barrier to Entry:** Non-technical domain experts (business analysts, healthcare workers, marketers) understand business context but lack programming skills in Python, Scikit-Learn, PyTorch, or XGBoost.
2. **Data Preprocessing Bottlenecks:** Raw real-world datasets suffer from missing values, categorical encoding issues, skewed distributions, and inconsistent schemas, requiring hours of manual data wrangling.
3. **Model Selection & Evaluation Friction:** Selecting the correct algorithm (e.g., Random Forest vs. XGBoost vs. Prophet), tuning hyperparameters, and visualizing complex evaluation metrics (ROC curves, confusion matrices) is daunting without formal ML training.
4. **Deployment & Prediction Barriers:** Even when models are successfully trained in notebooks, turning them into usable prediction APIs or interactive dashboards requires complex DevOps infra.

#### Why Existing Solutions are Insufficient:
* **DataRobot / H2O Driverless AI:** Powerful enterprise solutions, but prohibitively expensive for small-to-medium businesses, universities, and individual researchers, featuring complex setup overhead.
* **Google Cloud AutoML:** Requires deep cloud configuration, AWS/GCP IAM permission management, and charges per node-hour of training, limiting accessibility.
* **Jupyter Notebooks / Google Colab:** Great for data scientists, but useless for non-coder business stakeholders who require zero-code GUIs.

### 1.3. Proposed Solution
ML Studio is an end-to-end web platform that enables non-technical users to upload structured datasets (CSV, Excel), automatically inspect schemas, clean and preprocess data, select prediction targets, train baseline or state-of-the-art ML models across 7 core ML tasks, compare model metrics visually, run instant inference predictions, and export analytical reports.

### 1.4. Expected Impact
* **Business Analysts:** Reduce model prototyping time from weeks to minutes.
* **Researchers & Educators:** Conduct empirical data exploration and baseline benchmarking without software engineering overhead.
* **Organizations:** Empower non-technical teams to make data-driven decisions while keeping infrastructure costs predictable.

### 1.5. Target Audience & Potential Users
* **Business Analysts & Product Managers:** Seeking predictive customer churn, revenue regression, or sentiment insights.
* **Healthcare & Academic Researchers:** Analyzing survey data, clinical trial outcomes, and statistical clustering.
* **E-Commerce & Marketing Managers:** Running recommendation systems and customer segmentation.

### 1.6. Business Value & Startup Potential
* **Freemium B2B SaaS:** Free tier for small datasets (<50MB, CPU models); Paid subscription for GPU training, large files (>1GB), and automated API deployments.
* **On-Premise Enterprise Licensing:** Offer containerized deployments for organizations with strict data privacy requirements (HIPAA, GDPR).

---

## 2. Objectives

### 2.1. Primary Objectives
1. **Automated Schema & Preprocessing Engine:** Automatically detect column data types (numeric, categorical, datetime, text), impute missing values, scale numeric ranges, and one-hot encode categoricals.
2. **Multi-Task ML Engine:** Support 7 machine learning paradigms: Classification, Regression, Clustering, Time Series Forecasting, Recommendation Systems, NLP, and Anomaly Detection.
3. **Interactive Visual Analytics:** Generate real-time performance evaluation dashboards featuring ROC curves, confusion matrices, residual plots, feature importances, and forecast charts using Plotly.

### 2.2. Secondary Objectives
1. **Explainable AI (XAI) Integration:** Provide SHAP (SHapley Additive exPlanations) visual summaries to reveal why models make specific predictions.
2. **One-Click Prediction & Export:** Enable users to run single or batch predictions on new data and export fine-tuned model artifacts (`.pkl`, `.onnx`) or downloadable PDF/HTML executive reports.

### 2.3. Long-term Vision
To become an open-source, extensible alternative to DataRobot, incorporating agentic LLM assistants that explain dataset anomalies, recommend preprocessing steps, and summarize insight reports in plain English.

---

## 3. Supported Machine Learning Paradigms & Models

ML Studio equips users with specialized algorithms across 7 distinct task categories:

| ML Task | Purpose / Use Case | Supported Algorithms & Models | Primary Metrics Generated |
| :--- | :--- | :--- | :--- |
| **Classification** | Predicting categorical outcomes (e.g., Churn vs Stay, Fraud vs Normal) | Logistic Regression, Decision Tree, Random Forest, XGBoost Classifier, SVM, Naive Bayes | Accuracy, Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix |
| **Regression** | Predicting continuous numerical values (e.g., House prices, Sales figures) | Linear Regression, Ridge, Lasso, XGBoost Regressor, Random Forest Regressor | Mean Squared Error (MSE), RMSE, Mean Absolute Error (MAE), R² Score |
| **Clustering** | Unsupervised grouping of unlabeled data (e.g., Customer segmentation) | KMeans, DBSCAN, Agglomerative Hierarchical Clustering | Silhouette Score, Davies-Bouldin Index, Inertia / Elbow Plots |
| **Time Series** | Forecasting future values based on temporal data (e.g., Demand planning) | Prophet, ARIMA / SARIMAX, LSTM Neural Networks | Mean Absolute Percentage Error (MAPE), RMSE, Multi-step Forecast Graphs |
| **Recommendation** | Recommending items to users based on preferences or history | Collaborative Filtering (SVD), Matrix Factorization, Content-Based Similarity | Mean Average Precision (MAP@K), Recall@K, Cosine Similarity Scores |
| **NLP** | Processing and predicting text sentiment or topics | TF-IDF + Classifier, Fine-tuned BERT Transformers, VADER / TextBlob Sentiment | Accuracy, F1-Score, Perplexity, Sentiment Polarity Distributions |
| **Anomaly Detection**| Identifying outliers and anomalous events | Isolation Forest, One-Class SVM, Local Outlier Factor (LOF) | Anomaly Scores, Outlier Percentage, Decision Boundary Charts |

---

## 4. Functional Requirements

### 4.1. Dataset Management & Profiling
* **Data-01: Multi-Format Upload:** Support CSV, XLSX, and JSON files up to 500MB with drag-and-drop web UI.
* **Data-02: Automated Profiling:** Infer data types (Integer, Float, String, Datetime, Boolean) and summarize missing percentage, cardinality, standard deviation, and skewness.
* **Data-03: Automated Data Cleaning:** Provide toggle options for handling missing values (Mean, Median, Mode, Drop, Interpolate) and outlier removal (IQR, Z-Score).

### 4.2. Model Training & Comparison
* **Train-01: Task Selection:** Guided 3-step wizard (Upload -> Select Task & Target Column -> Select Models).
* **Train-02: Multi-Model Benchmark:** Allow selecting up to 4 algorithms simultaneously to train in parallel and compare performance side-by-side.
* **Train-03: Asynchronous Progress:** Track training status via WebSockets/Server-Sent Events with progress bars and ETA indicators.

### 4.3. Evaluation & Visual Analytics
* **Eval-01: Interactive Metrics Dashboard:** Render dynamic charts (Plotly) for ROC-AUC curves, Confusion Matrices, Loss curves, and Feature Importance bar charts.
* **Eval-02: Explainability:** Generate SHAP summary force plots for individual predictions and global feature importance.

### 4.4. Prediction & Export
* **Pred-01: Interactive Single/Batch Inference:** Provide form inputs for quick single-row prediction or upload a test CSV for batch scoring.
* **Pred-02: Model Artifact Download:** Export trained model weights as `.pkl`, `.joblib`, or `.onnx` files.
* **Pred-03: Executive Report Generation:** Download comprehensive PDF/HTML reports summarizing dataset profile, data pipeline steps, model comparison tables, and dynamic charts.

---

## 5. User Roles & Permissions

| Role | Responsibilities | Permissions | Core Workflow |
| :--- | :--- | :--- | :--- |
| **Viewer / Guest** | Explores sample datasets, views public demo models, tests single inference forms. | Read-only access to demo workspace. | Select public dataset -> View pretrained benchmarks -> Test prediction. |
| **Data Analyst** | Uploads datasets, runs automated pipelines, trains & compares models, exports reports. | Full read/write within assigned workspace projects. | Upload CSV -> Clean Data -> Train XGBoost -> View SHAP -> Download Report. |
| **ML Engineer / Admin** | Manages cloud compute quotas, configures GPU worker nodes, manages model registries. | Workspace management, compute node configuration, user management. | Provision GPU workers -> Monitor Celery queues -> Set maximum dataset memory limits. |

---

## 6. Complete System Architecture

ML Studio is designed as an asynchronous, decoupled Web Platform:

```
[ Frontend: Next.js + React + Plotly.js + Tailwind CSS ]
                        │
                        ▼ (REST API / SSE Progress)
[ API Gateway / Reverse Proxy: Nginx ]
                        │
                        ▼
[ Backend API Service: FastAPI (Python 3.11) ]
         │              │              │
         ▼              ▼              ▼
[ PostgreSQL DB ]  [ Redis Cache ] [ Local / S3 Object Storage ]
(Metadata/Users)   (Task Queue)    (Raw CSVs & Trained .pkl Artifacts)
                        │
                        ▼
[ Asynchronous ML Workers: Celery / Redis Worker Pool ]
 ├── Worker 1: Data Cleaning & Preprocessing (Pandas/Polars)
 ├── Worker 2: Classical ML Training (Scikit-Learn/XGBoost)
 ├── Worker 3: Deep Learning & Time-Series (PyTorch/Prophet)
 └── Worker 4: Explainability & Metrics (SHAP/Plotly Generator)
```

---

## 7. Database Schema & Data Models

PostgreSQL schema capturing users, datasets, pipelines, experiments, and model artifacts:

```sql
-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Datasets Table
CREATE TABLE datasets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    file_name VARCHAR(255) NOT NULL,
    file_path VARCHAR(512) NOT NULL,
    file_size_bytes BIGINT NOT NULL,
    row_count INT,
    column_count INT,
    schema_metadata JSONB NOT NULL, -- Stores column types, missing value stats
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Experiments Table
CREATE TABLE experiments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    dataset_id UUID REFERENCES datasets(id) ON DELETE CASCADE,
    experiment_name VARCHAR(150) NOT NULL,
    ml_task VARCHAR(50) NOT NULL, -- Classification, Regression, TimeSeries, etc.
    target_column VARCHAR(100),
    preprocessing_config JSONB NOT NULL, -- Imputation strategy, encoding, scaling choices
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Model Runs Table
CREATE TABLE model_runs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    experiment_id UUID REFERENCES experiments(id) ON DELETE CASCADE,
    model_name VARCHAR(100) NOT NULL, -- XGBoost, Random Forest, Prophet, etc.
    hyperparameters JSONB NOT NULL,
    status VARCHAR(30) DEFAULT 'PENDING', -- PENDING, TRAINING, COMPLETED, FAILED
    metrics JSONB, -- Accuracy, F1, RMSE, R2, Silhouette Score
    artifact_path VARCHAR(512), -- Path to .pkl / .onnx file
    training_duration_seconds FLOAT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## 8. Key API Endpoint Specifications

### 8.1. Dataset Processing & Pipeline
* `POST /api/v1/datasets/upload`: Upload CSV/XLSX dataset. Returns `dataset_id` and schema metadata.
* `POST /api/v1/experiments/create`: Submit preprocessing & feature choices. Triggers data cleaning.

### 8.2. Model Training & Monitoring
* `POST /api/v1/train`: Launch asynchronous training task for selected models. Returns `task_id`.
* `GET /api/v1/train/status/{task_id}`: Server-Sent Events (SSE) endpoint broadcasting training percentage & live metrics.

### 8.3. Evaluation & Inference
* `GET /api/v1/models/{model_run_id}/metrics`: Returns Plotly JSON objects for ROC curves, Confusion Matrix, and SHAP feature importances.
* `POST /api/v1/predict/single`: Run real-time prediction for user-provided payload.

---

## 9. Verification & Testing Strategy

1. **Unit Testing:** PyTest suite verifying data cleaning routines (handling NaNs, categorical encoding integrity).
2. **Integration Testing:** End-to-end task execution checking that synthetic CSV uploads correctly generate trained Scikit-Learn `.pkl` files and valid JSON metric responses.
3. **Load Testing:** Locust benchmarking simulating 50 concurrent model training requests to test Celery worker auto-scaling and Redis queue queue depth management.

---

## 10. Research & Future Enhancements

* **AutoML & Dynamic Hyperparameter Tuning:** Integrate Optuna for automated Bayesian hyperparameter optimization without manual parameter input.
* **LLM Dataset Assistant:** Incorporate an LLM agent capable of answering plain-English questions about the dataset (e.g., *"What is the main driver of customer churn in this dataset?"*).
* **Explainable AI (XAI) Expansion:** Provide partial dependence plots (PDP) and counterfactual explanations alongside SHAP.
