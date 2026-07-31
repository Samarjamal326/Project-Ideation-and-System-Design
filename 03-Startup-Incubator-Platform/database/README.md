# Startup Incubator Platform: Multi-Tenant Schema Security

This folder contains DDL configurations and security settings for SQL databases.

## 1. Row-Level Security (RLS) Configuration

To implement strict multi-tenant isolation at the database layer (preventing one startup from viewing another startup's metrics), we configure PostgreSQL Row-Level Security:

### 1.1. RLS DDL Commands
```sql
-- Enable Row-Level Security on performance metrics
ALTER TABLE performance_metrics ENABLE ROW LEVEL SECURITY;

-- Create policy restricting reads based on active tenant id header
CREATE POLICY tenant_isolation_policy ON performance_metrics
    FOR ALL
    USING (startup_id IN (
        SELECT id FROM startups WHERE tenant_id = current_setting('app.current_tenant_id')::uuid
    ));
```

### 1.2. Application Handshake Flow
When a query is run from the Go backend, the database session sets the active tenant context prior to execution:
```sql
SET LOCAL app.current_tenant_id = 'c10f82c4-3329-4d62-a212-612b18acfa01';
SELECT * FROM performance_metrics WHERE startup_id = 'e98f121a-6c79-4672-a212-612b18acfa01';
```
Any attempt to access data from a different tenant raises an authorization exception, even if the query syntax is correct.
