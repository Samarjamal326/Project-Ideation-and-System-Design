# AlphaForecast AI: UI/UX & Interactive Dashboard Specifications

This directory documents layout designs, candlestick interactive chart specifications, signal visual indicators, and portfolio tracking UI.

## 1. User Dashboard Layout Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ Header: Search Bar (Ticker/Company) | Watchlist (5) | Portfolio | Export PDF │
├─────────────────────────────────────┬───────────────────────────────────────┤
│ Left Column (65% Width):            │ Right Column (35% Width):             │
│ 1. Candlestick Chart (Plotly)        │ 1. Signal Card (Strong Buy - 88% Conf)│
│    - Historical Prices (OHLC)       │ 2. Horizon Forecast Table (1D/7D/30D) │
│    - Predicted Trend line (Dashed)  │ 3. Feature Importance Bar Chart       │
│    - Confidence Interval Band (Shaded)│ 4. News Sentiment Gauge (-1.0 to 1.0) │
│ 2. Technical Indicators Overlay     │ 5. Model Comparison Metrics Table     │
│    (RSI, MACD, Volume Bars)         │    (TFT vs LSTM vs XGBoost vs Prophet)│
└─────────────────────────────────────┴───────────────────────────────────────┘
```

## 2. Key Visual Component Guidelines

1. **Signal Badges:**
   - `Strong Buy`: Glowing Green (#10B981)
   - `Buy`: Emerald (#34D399)
   - `Hold`: Amber (#FBBF24)
   - `Sell`: Orange (#F97316)
   - `Strong Sell`: Deep Red (#EF4444)
2. **Interactive Candlestick Canvas:** Zoomable canvas built with Lightweight Charts / Plotly.js allowing toggle switches for technical overlays (SMA_50, SMA_200, Bollinger Bands).
3. **Sentiment Polarity Gauge:** Semi-circular gauge visualizing news sentiment polarity score extracted from recent financial media.
