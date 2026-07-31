# ML Studio: User Interface & Experience Design Specifications

This folder documents screen navigation flows, wireframe specs, interactive dashboard layouts, and Plotly visualization designs for ML Studio.

## 1. Primary User Flow

```
[ Dashboard Home ]
       │
       ▼
[ 1. Dataset Upload & Schema Inspection ] (Drag & drop file, preview tabular rows, check NaNs)
       │
       ▼
[ 2. Data Cleaning & Pipeline Wizard ]    (Configure missing imputation, scaling, select target column)
       │
       ▼
[ 3. Model Benchmark Config ]            (Select ML task type & toggle model algorithms: Random Forest, XGBoost, etc.)
       │
       ▼
[ 4. Live Training Progress Screen ]     (Progress bar, real-time logs via SSE, execution ETA)
       │
       ▼
[ 5. Model Evaluation & Comparison ]     (Side-by-side metric tables, ROC curves, Confusion Matrix, SHAP charts)
       │
       ▼
[ 6. Interactive Prediction & Export ]   (Single/Batch prediction form, export PDF report, download .pkl file)
```

## 2. Key Screen Wireframe Specifications

1. **Schema Inspector Modal:** Highlights inferred datatypes with color-coded badges (Blue = Numeric, Green = Categorical, Yellow = Datetime). Displays warnings for missing values > 20%.
2. **Model Comparison Grid:** Interactive Plotly graphs displaying ROC-AUC curves for multiple models overlaid on the same canvas for visual benchmarking.
3. **SHAP Feature Importance Visualizer:** Waterfall plot displaying positive/negative impact of each input feature on final predictions.
