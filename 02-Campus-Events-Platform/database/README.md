# Campus Events Platform: Database Optimization

This directory hosts SQL schema definition files and structural optimizations for the PostgreSQL instance.

## 1. High-Concurrency Optimization

To prevent deadlock conditions and handle ticketing rushes, the following optimizations are implemented:

### 1.1. Optimistic Locking
We introduce a `version` column in the `tickets` table to prevent race conditions during updates:
```sql
ALTER TABLE tickets ADD COLUMN version INT DEFAULT 1 NOT NULL;
```
When booking, the application logic checks:
```sql
UPDATE tickets 
SET status = 'Sold', version = version + 1 
WHERE id = :ticket_id AND version = :current_version;
```
If the rows affected is `0`, another transaction has modified the ticket, and the booking transaction rolled back and retried.

### 1.2. Database Constraints
To prevent double-booking at the hardware engine layer, a unique constraint maps active tickets:
```sql
CREATE UNIQUE INDEX idx_unique_active_seat 
ON tickets(event_id, seat_number) 
WHERE (status != 'Cancelled');
```
This ensures database integrity even if the application lock logic experiences edge delays.
