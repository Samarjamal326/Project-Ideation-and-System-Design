# ML Studio: Database Schema & Migration Indexing

This directory contains the schema DDL, indexing strategies, and database configuration for ML Studio's PostgreSQL persistence layer.

## 1. Schema DDL & Optimization

```sql
-- Create Indexes for fast querying of experiment histories
CREATE INDEX idx_datasets_user_id ON datasets(user_id);
CREATE INDEX idx_experiments_dataset_id ON experiments(dataset_id);
CREATE INDEX idx_model_runs_experiment_id ON model_runs(experiment_id);
CREATE INDEX idx_model_runs_status ON model_runs(status);

-- JSONB Indexing for Schema Metadata and Metrics
CREATE INDEX idx_datasets_schema ON datasets USING gin (schema_metadata);
CREATE INDEX idx_model_runs_metrics ON model_runs USING gin (metrics);
```

## 2. Execution Query Tuning

* **JSONB Querying:** We utilize GIN (Generalized Inverted Index) on `schema_metadata` and `metrics` to enable fast filtering (e.g., finding all model runs with `accuracy > 0.90` across historical projects).
* **Cascade Deletes:** Foreign key constraints specify `ON DELETE CASCADE` so deleting an experiment automatically cleans up associated model run metadata.
