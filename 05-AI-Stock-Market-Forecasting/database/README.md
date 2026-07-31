# AlphaForecast AI: Time-Series Database Schema & Indexing

This directory contains DDL scripts, TimescaleDB hypertable setups, and indexing strategies for financial market data storage.

## 1. Schema DDL & TimescaleDB Optimization

```sql
-- Enable TimescaleDB Extension if available
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Create Hypertable on price_timestamp
SELECT create_hypertable('stock_prices', 'price_timestamp', if_not_exists => TRUE);

-- Create Indexes for ticker lookup and temporal range queries
CREATE INDEX idx_stock_prices_ticker_time ON stock_prices (stock_id, price_timestamp DESC);
CREATE INDEX idx_predictions_stock_target ON predictions (stock_id, target_date DESC);
CREATE INDEX idx_predictions_model ON predictions (model_name);

-- Composite Index for Fast Signal & Confidence Queries
CREATE INDEX idx_predictions_signal ON predictions (stock_id, signal, confidence_score DESC);
```

## 2. Retention Policies & Aggregations

* **Downsampling:** Raw 1-minute intraday prices older than 90 days are automatically downsampled into 1-hour and 1-day OHLC candles to preserve disk storage.
* **Continuous Aggregates:** TimescaleDB continuous aggregates compute daily moving averages (SMA_50, SMA_200) automatically in background views.
