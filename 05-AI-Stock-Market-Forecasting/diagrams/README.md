# AlphaForecast AI: Process Sequence & Workflow Diagrams

This directory contains Mermaid workflow sequence diagrams for data ingestion, feature calculation, deep learning inference, and backtesting.

## 1. Automated Forecast & Signal Pipeline

```mermaid
sequenceDiagram
    autonumber
    actor User as Investor / Trader
    participant FE as Next.js Dashboard
    participant API as FastAPI Backend
    participant Redis as Redis Cache
    participant DB as TimescaleDB
    participant Worker as Celery AI Worker
    participant Yahoo as Yahoo Finance API

    User->>FE: Select Ticker "AAPL"
    FE->>API: GET /api/v1/forecast/AAPL
    API->>Redis: Check precomputed forecast cache
    alt Cache Hit
        Redis-->>API: Return cached forecast & signal JSON
    else Cache Miss
        API->>DB: Query latest stock_prices & predictions
        alt Predictions Stale
            API->>Redis: Trigger Priority Model Inference Worker
            Worker->>Yahoo: Fetch latest OHLCV data
            Worker->>Worker: Calculate TA-Lib indicators (RSI, MACD, SMA)
            Worker->>Worker: Run Temporal Fusion Transformer (TFT) model
            Worker->>Worker: Compute Buy/Hold/Sell signal & confidence score
            Worker->>DB: Save new predictions to DB
            Worker->>Redis: Update Cache
            Redis-->>API: Return fresh forecast JSON
        end
    end
    API-->>FE: Return Forecast, Signals, and Feature Importances
    FE->>User: Render Candlestick Chart, Confidence Bounds, and Signal Badges
```

## 2. Quantitative Backtesting Sequence

```mermaid
sequenceDiagram
    autonumber
    actor User as Quant Researcher
    participant FE as Next.js Dashboard
    participant API as FastAPI Backend
    participant Worker as Backtest Worker

    User->>FE: Configure Backtest (Strategy: TFT Signal, Period: 2 Years, Capital: $10,000)
    FE->>API: POST /api/v1/backtest
    API->>Worker: Launch historical trading simulation
    Worker->>Worker: Iterate historical price series day-by-day
    Worker->>Worker: Execute Buy/Sell signals & track equity curve
    Worker->>Worker: Compute Sharpe Ratio, Max Drawdown %, Total ROI %
    Worker-->>API: Return Simulation Results & Equity Time Series
    API-->>FE: Return Backtest Performance JSON
    FE->>User: Render Portfolio Equity Curve & Risk Metrics Table
```
