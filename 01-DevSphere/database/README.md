# DevSphere: Database Schema & Vector Indexing Specifications

This folder contains DDL scripts and optimization documents for the PostgreSQL database backend.

## 1. Vector Database Optimization

We leverage the `pgvector` extension for semantic matching. A key optimization is index tuning. For large datasets, we implement a **Hierarchical Navigable Small World (HNSW)** index rather than an Inverted File (IVFFlat) index.

### 1.1. Index Creation DDL
```sql
-- HNSW Index for Cosine Similarity searches
CREATE INDEX idx_profiles_embedding ON profiles 
USING hnsw (profile_embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

* **m = 16:** Max links per node. High values improve search recall but increase indexing time.
* **ef_construction = 64:** Size of dynamic candidate list. Improves accuracy of vector searches.

---

## 2. Table Migrations

### 2.1. Ingestion Triggers
To automatically compute composite profile strings when repositories update, we implement PostgreSQL triggers:

```sql
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_repositories_modtime
    BEFORE UPDATE ON repositories
    FOR EACH ROW
    EXECUTE PROCEDURE update_modified_column();
```
