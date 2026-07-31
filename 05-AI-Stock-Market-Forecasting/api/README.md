# AlphaForecast AI: API Reference Specifications

This document details backend API endpoints for financial data querying, forecast signal generation, model comparison, and backtesting.

## 1. Authentication Header
All protected endpoints require Bearer JWT authorization:
`Authorization: Bearer <JWT_TOKEN>`

## 2. API Endpoint Specifications

### 2.1. Ticker Search & Historical Data
#### `GET /api/v1/stocks/search`
* **Query Parameters:** `q=AAPL`
* **Response (200 OK):**
  ```json
  [
    {
      "stock_id": "9a8b7c6d-5e4f-3a2b-1c0d-9e8f7a6b5c4d",
      "ticker": "AAPL",
      "company_name": "Apple Inc.",
      "sector": "Technology",
      "industry": "Consumer Electronics"
    }
  ]
  ```

### 2.2. Forecast & Signals
#### `GET /api/v1/forecast/AAPL`
* **Description:** Retrieve current AI forecast, buy/hold/sell signal, confidence score, and multi-horizon price target.
* **Response (200 OK):**
  ```json
  {
    "ticker": "AAPL",
    "current_price": 185.25,
    "forecast_summary": {
      "horizon_1d": {"predicted_close": 187.10, "change_pct": 1.00},
      "horizon_7d": {"predicted_close": 192.40, "change_pct": 3.86},
      "horizon_30d": {"predicted_close": 201.00, "change_pct": 8.50}
    },
    "composite_signal": "Strong Buy",
    "confidence_score": 88.4,
    "top_features": [
      {"feature": "RSI_14", "importance": 0.32},
      {"feature": "News Sentiment", "importance": 0.28},
      {"feature": "MACD Divergence", "importance": 0.21}
    ]
  }
  ```

### 2.3. Model Benchmarking Comparison
#### `GET /api/v1/forecast/AAPL/compare`
* **Description:** Compare predictions across all supported model architectures.
* **Response (200 OK):**
  ```json
  {
    "ticker": "AAPL",
    "models": {
      "TFT": {"predicted_7d": 192.40, "rmse": 1.42, "mape": 0.78},
      "LSTM": {"predicted_7d": 190.80, "rmse": 1.85, "mape": 0.95},
      "XGBoost": {"predicted_7d": 189.50, "rmse": 2.10, "mape": 1.12},
      "Prophet": {"predicted_7d": 188.00, "rmse": 2.65, "mape": 1.40}
    }
  }
  ```
