"""
PDF Generator for MarketMind AI - AI-Powered Financial Intelligence & Forecasting Platform
Uses ReportLab to produce a professionally formatted, color-branded PDF.
Color theme: Deep Forest Green + Gold/Amber (financial / premium)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT_PATH = (
    r"C:\Users\Prakash Gusain Ji\.gemini\antigravity-ide\scratch"
    r"\Project-Ideation-and-System-Design\09-MarketMind-AI-Proposal"
    r"\Project-Proposal-MarketMind-AI.pdf"
)

# ─── BRAND COLORS (Financial Green + Gold) ──────────────────
PRIMARY   = colors.HexColor("#0D3B2E")   # Deep forest green
ACCENT    = colors.HexColor("#D4A017")   # Gold / amber
ACCENT2   = colors.HexColor("#16A34A")   # Mid-green
LIGHT_BG  = colors.HexColor("#F0FDF4")   # Pale green wash
WHITE     = colors.white
DARK_TEXT = colors.HexColor("#1A1A2E")
MID_TEXT  = colors.HexColor("#4B5563")
TBL_HDR   = colors.HexColor("#0D3B2E")
TBL_R1    = colors.HexColor("#DCFCE7")
TBL_R2    = colors.white
RULE_CLR  = colors.HexColor("#D4A017")
WARN_BG   = colors.HexColor("#FEF9C3")   # Amber note background

W_FULL = A4[0] - 4 * cm


# ─── STYLES ─────────────────────────────────────────────────
def make_styles():
    s = {}
    s['H1'] = ParagraphStyle('H1', fontSize=15, textColor=WHITE,
                              fontName='Helvetica-Bold', alignment=TA_LEFT,
                              leading=22, spaceBefore=18, spaceAfter=8,
                              backColor=PRIMARY, borderPad=8)
    s['H2'] = ParagraphStyle('H2', fontSize=11, textColor=PRIMARY,
                              fontName='Helvetica-Bold', alignment=TA_LEFT,
                              leading=17, spaceBefore=12, spaceAfter=4)
    s['H3'] = ParagraphStyle('H3', fontSize=9.5, textColor=ACCENT2,
                              fontName='Helvetica-Bold', alignment=TA_LEFT,
                              leading=15, spaceBefore=8, spaceAfter=3)
    s['Body'] = ParagraphStyle('Body', fontSize=9.5, textColor=DARK_TEXT,
                                fontName='Helvetica', alignment=TA_JUSTIFY,
                                leading=15, spaceBefore=3, spaceAfter=3)
    s['Bullet'] = ParagraphStyle('Bullet', fontSize=9.5, textColor=DARK_TEXT,
                                  fontName='Helvetica', alignment=TA_LEFT,
                                  leading=15, spaceBefore=2, spaceAfter=2,
                                  leftIndent=16, bulletIndent=4)
    s['Note'] = ParagraphStyle('Note', fontSize=8.5, textColor=MID_TEXT,
                                fontName='Helvetica-Oblique', alignment=TA_LEFT,
                                leading=13, spaceBefore=3, spaceAfter=3,
                                leftIndent=12)
    s['Warn'] = ParagraphStyle('Warn', fontSize=9, textColor=colors.HexColor("#78350F"),
                                fontName='Helvetica', alignment=TA_LEFT,
                                leading=14, spaceBefore=4, spaceAfter=4,
                                leftIndent=10, backColor=WARN_BG, borderPad=6)
    s['Code'] = ParagraphStyle('Code', fontSize=8, textColor=DARK_TEXT,
                                fontName='Courier', alignment=TA_LEFT,
                                leading=12, spaceBefore=4, spaceAfter=4,
                                leftIndent=16, backColor=LIGHT_BG, borderPad=6)
    return s

S = make_styles()


# ─── HELPERS ────────────────────────────────────────────────
def h1(t): return Paragraph(f"&nbsp;&nbsp;{t}", S['H1'])
def h2(t): return Paragraph(t, S['H2'])
def h3(t): return Paragraph(t, S['H3'])
def body(t): return Paragraph(t, S['Body'])
def bullet(t): return Paragraph(f"• &nbsp;{t}", S['Bullet'])
def note(t): return Paragraph(t, S['Note'])
def warn(t): return Paragraph(t, S['Warn'])
def sp(n=6): return Spacer(1, n)
def rule(): return HRFlowable(width="100%", thickness=1,
                               color=RULE_CLR, spaceAfter=6, spaceBefore=6)


def tbl(rows, widths=None, header=True):
    if widths is None:
        widths = [W_FULL / len(rows[0])] * len(rows[0])
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle([
        ('FONTNAME',  (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE',  (0,0), (-1,0), 9),
        ('BACKGROUND',(0,0), (-1,0), TBL_HDR),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME',  (0,1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',  (0,1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [TBL_R1, TBL_R2]),
        ('GRID',      (0,0), (-1,-1), 0.4, colors.HexColor("#86EFAC")),
        ('ALIGN',     (0,0), (-1,-1), 'LEFT'),
        ('VALIGN',    (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('RIGHTPADDING',  (0,0), (-1,-1), 8),
    ]))
    return t


# ─── COVER PAGE ─────────────────────────────────────────────
def cover_page(E):
    # Title banner
    r1 = [[Paragraph("<b>MarketMind AI</b>",
                     ParagraphStyle('T1', fontSize=34, textColor=WHITE,
                                    fontName='Helvetica-Bold', alignment=TA_CENTER, leading=42))]]
    t1 = Table(r1, colWidths=[W_FULL])
    t1.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PRIMARY),
                             ('TOPPADDING',(0,0),(-1,-1),38),
                             ('BOTTOMPADDING',(0,0),(-1,-1),6),
                             ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    E.append(t1)

    r2 = [[Paragraph("AI-Powered Financial Intelligence &amp; Forecasting Platform",
                     ParagraphStyle('T2', fontSize=14, textColor=ACCENT,
                                    fontName='Helvetica-Bold', alignment=TA_CENTER, leading=20))]]
    t2 = Table(r2, colWidths=[W_FULL])
    t2.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PRIMARY),
                             ('TOPPADDING',(0,0),(-1,-1),4),
                             ('BOTTOMPADDING',(0,0),(-1,-1),38),
                             ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    E.append(t2)
    E.append(sp(14))

    badge = [[Paragraph("<b>Final Year Project Proposal &nbsp;|&nbsp; B.E. / B.Tech Computer Science / AI &amp; Data Science</b>",
                        ParagraphStyle('B', fontSize=10, textColor=PRIMARY,
                                       fontName='Helvetica-Bold', alignment=TA_CENTER, leading=16))]]
    bt = Table(badge, colWidths=[W_FULL])
    bt.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),ACCENT),
                             ('TOPPADDING',(0,0),(-1,-1),10),
                             ('BOTTOMPADDING',(0,0),(-1,-1),10),
                             ('ALIGN',(0,0),(-1,-1),'CENTER')]))
    E.append(bt)
    E.append(sp(36))

    meta = [("Submitted By","[Your Name]"),("Department","[Your Department]"),
            ("Institution","[Your College Name]"),("Academic Year","2025 – 2026"),
            ("Project Guide / Mentor","[Mentor Name]"),("Date","July 2026")]
    mrows = [[Paragraph(f"<b>{k}</b>", ParagraphStyle('MK',fontSize=10,fontName='Helvetica-Bold',
                                                        textColor=PRIMARY,leading=16)),
              Paragraph(v, ParagraphStyle('MV',fontSize=10,fontName='Helvetica',
                                          textColor=DARK_TEXT,leading=16))]
             for k, v in meta]
    mt = Table(mrows, colWidths=[6*cm, 10*cm])
    mt.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                             ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                             ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
                             ('LEFTPADDING',(0,0),(-1,-1),8),
                             ('LINEBELOW',(0,0),(-1,-2),0.3,colors.HexColor("#D1D5DB"))]))
    E.append(mt)
    E.append(PageBreak())


# ─── TOC ────────────────────────────────────────────────────
def toc_page(E):
    E.append(h1("Table of Contents"))
    E.append(sp(10))
    items = [
        ("1.","Executive Summary"),("2.","Problem Statement"),
        ("3.","Proposed Solution"),("4.","Supported AI & Machine Learning Models"),
        ("5.","Input Features & Data Engineering"),("6.","Platform Outputs"),
        ("7.","User Workflow"),("8.","User Roles & Responsibilities"),
        ("9.","Platform Features"),("10.","AI & Intelligence Features"),
        ("11.","Implementation Plan"),("12.","Technology Stack"),
        ("13.","System Architecture"),("14.","Research Potential"),
        ("15.","Facts & Industry Figures"),("16.","Limitations & Disclaimer"),
        ("17.","Why This Is a Major Project"),("18.","Future Scope"),("19.","Conclusion"),
    ]
    rows = [[Paragraph(f"<b>{n}</b>",ParagraphStyle('TN',fontSize=9.5,fontName='Helvetica-Bold',
                                                      textColor=ACCENT,leading=15)),
             Paragraph(t,ParagraphStyle('TT',fontSize=9.5,fontName='Helvetica',
                                         textColor=DARK_TEXT,leading=15))]
            for n,t in items]
    tt = Table(rows, colWidths=[1.2*cm, 14*cm])
    tt.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'LEFT'),
                             ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                             ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
                             ('ROWBACKGROUNDS',(0,0),(-1,-1),[LIGHT_BG,WHITE])]))
    E.append(tt)
    E.append(PageBreak())


# ─── MAIN CONTENT ───────────────────────────────────────────
def build_content(E):

    # 1. EXECUTIVE SUMMARY
    E.append(h1("1. Executive Summary"))
    E.append(sp())
    E.append(body("Financial markets generate enormous amounts of data every single day — stock prices, "
                  "trading volumes, technical signals, market news, and macroeconomic indicators. Yet, "
                  "for most individual investors and small financial analysts, making sense of all this "
                  "data is extremely difficult. Professional tools are expensive. Manual chart analysis "
                  "takes hours. And no reliable, accessible AI-powered platform exists for everyday users."))
    E.append(body("<b>MarketMind AI</b> is an AI-powered Financial Intelligence and Forecasting Platform "
                  "that addresses this gap directly. Users select a stock, choose a forecast horizon, and "
                  "the platform automatically downloads historical data, engineers technical features, runs "
                  "multiple AI models, generates forecasts with confidence scores, and presents everything "
                  "in an interactive, intuitive dashboard."))
    E.append(body("This platform is designed as a <b>decision-support and educational research tool</b> — "
                  "not as a financial advisor. It demonstrates how modern machine learning and deep learning "
                  "can be applied to real-world financial time-series data."))
    E.append(warn("Important: This platform provides AI-assisted educational insights only. It does not "
                  "constitute financial advice. All forecasts are for research and academic purposes."))
    E.append(sp(10))

    # 2. PROBLEM STATEMENT
    E.append(h1("2. Problem Statement"))
    E.append(sp())
    E.append(h2("2.1  Who Struggles With Financial Markets"))
    t1 = [["User Group","Core Challenge"],
          ["Individual Investors","Difficulty reading charts, limited understanding of indicators, information overload"],
          ["Financial Analysts","Manually processing large datasets, time-consuming forecasting, no automation"],
          ["Businesses & Institutions","Need rapid market insights for investment decisions — current tools are expensive"]]
    E.append(tbl(t1, widths=[4.5*cm, 12*cm]))
    E.append(sp(8))
    E.append(h2("2.2  Why Stock Markets Are So Difficult to Predict"))
    factors = [("Historical Price Patterns","Past behavior only partially predicts future movement"),
               ("Trading Volume","Sudden volume changes often precede major price moves"),
               ("Market Sentiment","Investor psychology and media narratives drive irrational swings"),
               ("Macroeconomic Factors","Interest rates, inflation, and GDP affect entire sectors"),
               ("Global Events","Geopolitical conflicts, pandemics, or regulatory changes can instantly reverse trends"),
               ("Investor Psychology","Fear and greed cause markets to deviate from rational pricing for extended periods")]
    E.append(tbl([["Factor","Why It Complicates Prediction"]] + [[f,d] for f,d in factors],
                 widths=[4.5*cm, 12*cm]))
    E.append(sp(8))
    E.append(h2("2.3  Why Traditional Methods Are Insufficient"))
    trad = [["Traditional Method","Key Limitation"],
            ["Manual Chart Analysis","Time-consuming, subjective, depends heavily on human experience"],
            ["Simple Moving Averages","Lagging indicators — signal changes after they already happened"],
            ["Fundamental Analysis","Requires accounting knowledge and access to financial statements"],
            ["Bloomberg / Reuters Terminal","Costs $20,000+ per year — out of reach for individual users"],
            ["Excel-Based Models","Cannot handle the volume, speed, or complexity of modern market data"]]
    E.append(tbl(trad, widths=[5*cm, 11.5*cm]))
    E.append(sp(10))

    # 3. PROPOSED SOLUTION
    E.append(h1("3. Proposed Solution"))
    E.append(sp())
    E.append(body("MarketMind AI is a web-based, AI-powered platform that automates the full pipeline "
                  "from raw stock data to structured, visual forecasts and analytical insights."))
    E.append(sp(6))
    wf = [["Step","What Happens","Automated?"],
          ["1. Stock Selection","User types a ticker — platform loads company info and validates symbol","User action"],
          ["2. Horizon Selection","Choose forecast period: 7-day, 30-day, or 90-day","User action"],
          ["3. Data Download","Platform fetches historical OHLCV data via Yahoo Finance API","Fully Automated"],
          ["4. Feature Engineering","RSI, MACD, SMA, Bollinger Bands, Volatility computed via TA-Lib","Fully Automated"],
          ["5. Multi-Model Training","LSTM, GRU, XGBoost, LightGBM, Prophet, ARIMA run in parallel","Fully Automated"],
          ["6. Forecast Generation","Predicted closing prices with confidence bounds produced","Fully Automated"],
          ["7. Trend Classification","Bullish / Bearish / Sideways label assigned","AI-Powered"],
          ["8. Explainability","SHAP chart + plain-English summary generated","Fully Automated"],
          ["9. Dashboard Display","Interactive Plotly charts and model comparison table rendered","Fully Automated"],
          ["10. Export","PDF report + CSV forecast data available for download","One click"]]
    E.append(tbl(wf, widths=[4*cm, 8*cm, 4.5*cm]))
    E.append(sp(10))

    # 4. MODELS
    E.append(h1("4. Supported AI & Machine Learning Models"))
    E.append(sp())
    E.append(body("MarketMind AI runs a diverse ensemble of models capturing different patterns in financial "
                  "time series — from classical statistics to state-of-the-art deep learning."))
    E.append(sp(6))
    E.append(h2("Machine Learning Models"))
    ml_rows = [["Model","Description","Best For"],
               ["Linear Regression","Fast, interpretable baseline — fits a straight trend line","Simple trend extrapolation"],
               ["Random Forest","Combines hundreds of decision trees — handles non-linear patterns","Mid-term feature-rich forecasting"],
               ["XGBoost","Gradient-boosted trees — industry standard for tabular financial data","High-accuracy indicator-based prediction"],
               ["LightGBM","Faster version of XGBoost with lower memory footprint","High-speed large-dataset forecasting"]]
    E.append(tbl(ml_rows, widths=[3.5*cm, 7*cm, 6*cm]))
    E.append(sp(6))
    E.append(h2("Deep Learning Models"))
    dl_rows = [["Model","Description","Best For"],
               ["LSTM","Long Short-Term Memory — remembers long-range patterns in price sequences","Multi-week price trend modeling"],
               ["GRU","Gated Recurrent Unit — faster than LSTM with comparable accuracy","Shorter-horizon sequence prediction"],
               ["Transformer","Attention-based — captures complex, non-local time correlations","Volatile, high-frequency market patterns"],
               ["Temporal Fusion Transformer (TFT)","State-of-the-art interpretable forecasting with uncertainty quantification","Multi-horizon + explainable forecasting"]]
    E.append(tbl(dl_rows, widths=[4*cm, 7*cm, 5.5*cm]))
    E.append(sp(6))
    E.append(h2("Classical Time Series Models"))
    ts_rows = [["Model","Description","Best For"],
               ["ARIMA","Statistical autocorrelation model — reliable on stable price series","Linear trend baseline comparison"],
               ["Prophet","Meta's forecasting tool — handles seasonality and holidays automatically","Seasonal and annual market pattern forecasting"]]
    E.append(tbl(ts_rows, widths=[3.5*cm, 7.5*cm, 5.5*cm]))
    E.append(sp(4))
    E.append(note("Why Multiple Models? No single model performs best on all stocks in all market "
                  "conditions. By running multiple models and comparing outputs, users get a far more "
                  "robust and reliable view of forecasted trends."))
    E.append(sp(10))

    # 5. INPUT FEATURES
    E.append(h1("5. Input Features & Data Engineering"))
    E.append(sp())
    E.append(body("The quality of a forecast is determined by the quality of its input features. "
                  "MarketMind AI automatically engineers a rich set of financial features from raw price data."))
    feat = [["Feature","Description","Why It Matters"],
            ["Open, High, Low, Close (OHLC)","Daily price range — foundation of all technical analysis","Raw price signal"],
            ["Trading Volume","Number of shares traded per day","High volume often confirms price moves"],
            ["SMA (Simple Moving Average)","Average price over N days — smooths out noise","Identifies overall trend direction"],
            ["EMA (Exponential Moving Average)","Weighted average — more weight on recent prices","Faster trend signal than SMA"],
            ["RSI (Relative Strength Index)","Oscillator (0-100) measuring price momentum speed","Detects overbought / oversold conditions"],
            ["MACD","Difference between 12-day and 26-day EMA","Signals trend reversals and momentum shifts"],
            ["Bollinger Bands","Price bands drawn +/-2 standard deviations from moving average","Measures volatility and price breakouts"],
            ["Volatility (ATR)","Average True Range — measures daily price swing magnitude","Quantifies current market risk"],
            ["Market Index","S&P 500 / Nifty 50 benchmark","Context for stock's relative performance"],
            ["Sector Performance","Industry sector average performance","Industry-level momentum signal"],
            ["News Sentiment (Optional)","NLP-derived sentiment polarity from financial headlines","Captures investor psychology and market mood"]]
    E.append(tbl(feat, widths=[4.5*cm, 6.5*cm, 5.5*cm]))
    E.append(sp(4))
    E.append(note("All features computed automatically using TA-Lib, Pandas, and NumPy — no manual calculation required."))
    E.append(sp(10))

    # 6. OUTPUTS
    E.append(h1("6. Platform Outputs"))
    E.append(sp())
    out = [["Output","Description"],
           ["Predicted Closing Price","Forecasted price for each day in the selected horizon"],
           ["Trend Prediction","Bullish (upward), Bearish (downward), or Sideways direction classification"],
           ["Confidence Score","0-100% certainty score derived from model ensemble variance"],
           ["Educational Signal","Buy / Hold / Sell label — for research and learning purposes only"],
           ["Forecast Graph","Interactive Plotly chart: historical data + predicted trajectory + confidence bounds"],
           ["Historical Comparison","Overlay of previous predictions vs actual prices to evaluate model accuracy"],
           ["Feature Importance (SHAP)","Chart showing which indicators influenced the current forecast the most"],
           ["Risk Analysis","Volatility, historical drawdown, Value-at-Risk (VaR 95%), Sharpe Ratio"],
           ["Model Comparison Table","Side-by-side RMSE, MAE, MAPE, and Directional Accuracy across all models"]]
    E.append(tbl(out, widths=[5*cm, 11.5*cm]))
    E.append(sp(10))

    # 7. USER WORKFLOW
    E.append(h1("7. User Workflow"))
    E.append(sp())
    uw = [["Step","What Happens","User Action"],
          ["1. Search Stock","Type ticker (e.g., AAPL, TCS.NS) — platform validates and loads stock profile","Type ticker"],
          ["2. Select Time Horizon","Choose forecast period: 7-day, 30-day, or 90-day","One dropdown"],
          ["3. Run Forecast","Platform downloads data, engineers features, runs all models in background","Click 'Run'"],
          ["4. View Dashboard","Charts, trend label, confidence score, and feature importance displayed","Explore freely"],
          ["5. Compare Models","Side-by-side accuracy metrics and predictions across all models","Click 'Compare'"],
          ["6. Download Report","Export full PDF analytical report or raw CSV forecast data","One click"]]
    E.append(tbl(uw, widths=[4*cm, 8.5*cm, 4*cm]))
    E.append(sp(10))

    # 8. USER ROLES
    E.append(h1("8. User Roles & Responsibilities"))
    E.append(sp())
    roles = [["Role","Who They Are","What They Can Do"],
             ["Investor","Retail investor, student, individual user","Search stocks, run forecasts, view dashboards, download reports"],
             ["Financial Analyst","Professional or academic researcher","Advanced model outputs, cross-stock comparison, data export"],
             ["Researcher","ML researcher or academic","Raw metrics, custom backtests, SHAP outputs, model logs"],
             ["Administrator","Platform operator / IT admin","Manage users, monitor API usage, configure data refresh schedules"]]
    E.append(tbl(roles, widths=[3.5*cm, 5*cm, 8*cm]))
    E.append(sp(10))

    # 9. PLATFORM FEATURES
    E.append(h1("9. Platform Features"))
    E.append(sp())
    feat_groups = [
        ("Data & Discovery", [
            ("Stock Search", "Search any global ticker (NSE, BSE, NYSE, NASDAQ) — live company profile loaded"),
            ("Portfolio Watchlist", "Save multiple stocks for quick access and side-by-side monitoring"),
            ("Historical Charts", "Interactive Plotly candlestick charts — up to 10 years of price history"),
        ]),
        ("Analytics & Forecasting", [
            ("Technical Indicators Overlay", "Toggle SMA, EMA, RSI, MACD, Bollinger Bands on historical charts"),
            ("Forecast Dashboard", "Predicted price trajectory with confidence intervals and trend label"),
            ("Model Comparison", "Run all 10+ models simultaneously — compare RMSE, MAPE, Directional Accuracy"),
            ("Prediction History", "Archive of all past forecasts — track how predictions compared to actuals"),
            ("Performance Metrics", "RMSE, MAE, MAPE, R-squared, Directional Accuracy for each model"),
        ]),
        ("Risk & Intelligence", [
            ("Risk Analysis Dashboard", "Volatility, historical drawdown, Value-at-Risk, and Sharpe Ratio"),
            ("Feature Importance (SHAP)", "Visual explanation of which indicators drove each model's forecast"),
        ]),
        ("Export", [
            ("Export Reports", "One-click download of PDF executive report or raw CSV prediction data"),
        ]),
    ]
    for gname, feats in feat_groups:
        E.append(h2(gname))
        rows = [["Feature","Description"]] + [[f, d] for f, d in feats]
        E.append(tbl(rows, widths=[5*cm, 11.5*cm]))
        E.append(sp(5))
    E.append(sp(6))

    # 10. AI FEATURES
    E.append(h1("10. AI & Intelligence Features"))
    E.append(sp())
    ai = [["AI Feature","What It Does"],
          ["Multi-Model Comparison","Runs LSTM, GRU, XGBoost, Prophet, ARIMA simultaneously — shows which performs best"],
          ["Confidence Score","Quantifies forecast certainty using prediction intervals from ensemble variance"],
          ["Feature Importance (SHAP)","Visual chart showing which financial indicators drove each prediction"],
          ["Explainable AI (XAI)","Plain-English sentence explaining why the model forecasts Bullish or Bearish"],
          ["Trend Detection","Classifies trajectory using combination of ML output and momentum indicators"],
          ["Volatility Prediction","Estimates expected price range (upper/lower bounds) around the forecast"],
          ["Model Recommendation","Suggests the best-performing model for the selected stock based on historical accuracy"],
          ["Risk Scoring","Composite risk score combining volatility, trend strength, and market context"],
          ["Natural Language Summary","Generates a 2-3 sentence plain-English market summary for each forecast run"],
          ["LLM Integration (Future)","Chat interface: 'Why is Infosys trending down this month?' answered by LLM + live data"]]
    E.append(tbl(ai, widths=[5.5*cm, 11*cm]))
    E.append(sp(10))

    # 11. IMPLEMENTATION PLAN
    E.append(h1("11. Implementation Plan"))
    E.append(sp())
    impl = [
        ("Phase 1\nFoundation", "Month 1",
         "FastAPI backend, PostgreSQL schema, JWT auth, Next.js UI, Yahoo Finance data pipeline"),
        ("Phase 2\nFeature Engineering & ML Core", "Months 2-3",
         "TA-Lib indicators, Scikit-Learn / XGBoost / LightGBM / ARIMA / Prophet, Celery async queue"),
        ("Phase 3\nDeep Learning & Dashboard", "Month 4",
         "LSTM / GRU / Transformer / TFT in PyTorch, Plotly charts, SHAP integration, model comparison"),
        ("Phase 4\nDeployment & Polish", "Month 5",
         "Docker containerization, AWS ECS deployment, PDF report generator, end-to-end testing"),
    ]
    header = [Paragraph(t, ParagraphStyle('IH', fontSize=9, fontName='Helvetica-Bold',
                                           textColor=WHITE, leading=13))
              for t in ["Phase", "Timeline", "Key Deliverables"]]
    rows = [header]
    bg_map = {1: colors.HexColor("#DCFCE7"), 2: colors.HexColor("#FEF9C3"),
              3: colors.HexColor("#DBEAFE"), 4: colors.HexColor("#FCE7F3")}
    for i, (ph, tm, dl) in enumerate(impl, 1):
        rows.append([
            Paragraph(f"<b>{ph}</b>", ParagraphStyle('IP', fontSize=9, fontName='Helvetica-Bold',
                                                       textColor=PRIMARY, leading=13)),
            Paragraph(tm, ParagraphStyle('IT', fontSize=9, fontName='Helvetica',
                                          textColor=ACCENT2, leading=13, alignment=TA_CENTER)),
            Paragraph(dl, ParagraphStyle('ID', fontSize=9, fontName='Helvetica',
                                          textColor=DARK_TEXT, leading=13)),
        ])
    it = Table(rows, colWidths=[4*cm, 2.5*cm, 10*cm])
    style_cmds = [('BACKGROUND',(0,0),(-1,0),TBL_HDR),
                  ('ALIGN',(0,0),(-1,-1),'LEFT'),('ALIGN',(1,0),(1,-1),'CENTER'),
                  ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                  ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
                  ('LEFTPADDING',(0,0),(-1,-1),8),
                  ('GRID',(0,0),(-1,-1),0.4,colors.HexColor("#86EFAC"))]
    for i, bg in bg_map.items():
        style_cmds.append(('BACKGROUND',(0,i),(-1,i),bg))
    it.setStyle(TableStyle(style_cmds))
    E.append(it)
    E.append(sp(10))

    # 12. TECH STACK
    E.append(h1("12. Technology Stack"))
    E.append(sp())
    tech = [["Layer","Technology","Why This Was Chosen"],
            ["Frontend","Next.js (React)","Fast, component-based — industry standard for modern web apps"],
            ["Backend API","FastAPI (Python)","Async, high-performance — ideal for ML and data-heavy workloads"],
            ["ML & Classical Models","Scikit-Learn","Industry-standard library for regression and ensemble models"],
            ["Deep Learning","PyTorch + TensorFlow","PyTorch for LSTM/GRU/Transformer; TF for TFT model"],
            ["Financial Indicators","TA-Lib + Pandas + NumPy","Standard tools for RSI, MACD, Bollinger Bands, moving averages"],
            ["Time Series","Prophet (Meta)","Handles seasonality, trends, and holidays in stock data automatically"],
            ["Data Source","yfinance (Yahoo Finance API)","Free, reliable, global exchange coverage — OHLCV + market data"],
            ["Visualization","Plotly","Interactive financial charts — candlesticks, forecasts, SHAP plots"],
            ["Database","PostgreSQL","Reliable relational storage for users, forecasts, watchlists, model results"],
            ["Task Queue","Celery + Redis","Background model training without blocking the web server"],
            ["Authentication","JWT + RBAC","Secure stateless tokens with fine-grained role-based access"],
            ["Deployment","Docker + AWS ECS","Containerized, auto-scaled, production-ready cloud hosting"]]
    E.append(tbl(tech, widths=[3.5*cm, 4*cm, 9*cm]))
    E.append(sp(10))

    # 13. SYSTEM ARCHITECTURE
    E.append(h1("13. System Architecture"))
    E.append(sp())
    E.append(body("The platform follows a clean, layered architecture. The frontend communicates with "
                  "FastAPI via REST API. Heavy model training and inference is offloaded to Celery workers "
                  "backed by Redis, keeping the web server fully responsive. Each component is independently "
                  "deployable and horizontally scalable."))
    E.append(sp(6))
    arch_tbl = [["Layer","Component","Responsibility"],
                ["Client Layer","Next.js Frontend","UI, routing, Plotly charts, real-time progress display"],
                ["API Layer","FastAPI Backend","Business logic, authentication, forecast job dispatch"],
                ["Data Layer","PostgreSQL + Redis","Persistent storage + session / queue management"],
                ["Data Service","yfinance API Integration","Automated historical OHLCV data download"],
                ["Feature Layer","TA-Lib / Pandas Engine","RSI, MACD, SMA, Bollinger Bands computation"],
                ["ML Layer","Scikit-Learn / LightGBM","Classical ML regression and ensemble models"],
                ["DL Layer","PyTorch / TFT","LSTM, GRU, Transformer, Temporal Fusion Transformer"],
                ["TS Layer","Prophet / ARIMA","Classical time series decomposition models"],
                ["XAI Layer","SHAP Engine","Feature importance and prediction explanation"],
                ["Export Layer","Report Generator","PDF executive report and CSV data export"],
                ["Deployment","Docker + AWS ECS","Containerized, auto-scaled cloud production hosting"]]
    E.append(tbl(arch_tbl, widths=[3.5*cm, 4.5*cm, 8.5*cm]))
    E.append(sp(8))
    E.append(h2("Architecture Diagram (Mermaid.js)"))
    E.append(sp(4))
    arch_code = [
        "graph TD",
        "    User([Investor / Analyst / Researcher]) -->|HTTPS| FE[Next.js Frontend]",
        "    FE -->|REST API| API[FastAPI Backend]",
        "    API --> DB[(PostgreSQL Database)]",
        "    API --> Redis[(Redis Cache & Broker)]",
        "    subgraph ML Prediction Engine - Celery Workers",
        "        Redis --> MDS[Market Data - yfinance API]",
        "        MDS --> FEng[Feature Engineering - TA-Lib / Pandas]",
        "        FEng --> ML[Classical ML - XGBoost / LightGBM]",
        "        FEng --> DL[Deep Learning - LSTM / GRU / TFT]",
        "        FEng --> TS[Time Series - Prophet / ARIMA]",
        "        ML & DL & TS --> EVAL[Evaluation - RMSE / MAPE / Dir. Acc.]",
        "        EVAL --> SHAP[SHAP Explainability Engine]",
        "        SHAP --> DB",
        "    end",
        "    API --> RPT[Report Generator - PDF / CSV]",
        "    RPT --> User",
    ]
    for line in arch_code:
        E.append(Paragraph(line, S['Code']))
    E.append(note("Diagram above is in Mermaid.js format — renders in GitHub Markdown, Notion, or any Mermaid viewer."))
    E.append(sp(10))

    # 14. RESEARCH POTENTIAL
    E.append(h1("14. Research Potential"))
    E.append(sp())
    research = [["Research Direction","Description"],
                ["Time Series Forecasting in Finance","Compare classical (ARIMA) vs. deep learning (LSTM, TFT) on equity market data"],
                ["Deep Learning for Finance","Evaluate Transformer and TFT architectures on non-stationary financial time series"],
                ["Explainable AI in Investment","Study how SHAP explanations of model predictions influence investor decision quality"],
                ["Hybrid ML Models","Combine LSTM feature extraction with XGBoost output layer for ensemble forecasts"],
                ["Financial Decision Support Systems","Measure how AI-assisted signals affect real investor decision accuracy"],
                ["Model Comparison Studies","Systematic benchmark of 10+ models across multiple stocks, sectors, and market caps"],
                ["Forecast Uncertainty Quantification","Use conformal prediction or Bayesian methods for calibrated confidence intervals"]]
    E.append(tbl(research, widths=[5.5*cm, 11*cm]))
    E.append(sp(10))

    # 15. FACTS & FIGURES
    E.append(h1("15. Facts & Industry Figures"))
    E.append(sp())
    facts = [["Statistic","Source"],
             ["Global FinTech market expected to reach $644 billion by 2029","MarketsandMarkets, 2024"],
             ["AI in financial services market growing at 16.5% CAGR through 2030","Grand View Research, 2024"],
             ["Over 100 million retail investors in India as of 2024 — tripled since 2020","NSE India, 2024"],
             ["Algorithmic trading accounts for 60-73% of U.S. equity market volume","TABB Group / SEC Research"],
             ["Global Financial Analytics market projected at $11.4 billion by 2026","Allied Market Research"],
             ["65% of hedge funds now actively using ML for investment decisions","PwC Asset Management Report, 2023"],
             ["Retail investors spend avg. 4-6 hours per week on manual market research","Schwab Investor Survey, 2023"]]
    E.append(tbl(facts, widths=[10*cm, 6.5*cm]))
    E.append(sp(10))

    # 16. LIMITATIONS
    E.append(h1("16. Limitations & Disclaimer"))
    E.append(sp())
    E.append(body("This section demonstrates technical honesty and awareness of real-world constraints — "
                  "qualities that distinguish strong, mature academic projects from superficial ones."))
    E.append(sp(6))
    E.append(h2("What This Platform Does NOT Do"))
    for t in ["Guarantee accurate future price predictions",
              "Constitute financial advice of any kind",
              "Make real investment decisions automatically",
              "Account for unpredictable black-swan events (pandemics, geopolitical crises)"]:
        E.append(bullet(t))
    E.append(sp(6))
    E.append(h2("Why Markets Are Fundamentally Hard to Predict"))
    for t in ["Markets are influenced by unpredictable global events and human emotion",
              "Even the best AI models cannot account for sudden regulatory or political shocks",
              "All ML models are trained on historical data — past patterns do not always repeat",
              "Forecast accuracy degrades significantly beyond 30-day horizons for volatile stocks"]:
        E.append(bullet(t))
    E.append(sp(6))
    E.append(warn("Platform Disclaimer: All forecasts generated by MarketMind AI are for academic, "
                  "educational, and research purposes only. The platform is a decision-support tool. "
                  "Users should consult qualified financial advisors before making any investment decisions."))
    E.append(sp(10))

    # 17. WHY MAJOR PROJECT
    E.append(h1("17. Why This Is a Major Project"))
    E.append(sp())
    E.append(body("This is a question frequently asked: 'Is this just another stock prediction website?' "
                  "The honest answer is definitively no. Here is a direct comparison:"))
    compare = [["Dimension","Basic Stock Predictor","MarketMind AI Platform"],
               ["Models Used","1 LSTM or 1 ARIMA","10+ models: LSTM, GRU, TFT, XGBoost, LightGBM, Prophet, ARIMA, Transformer"],
               ["Data Pipeline","Manual CSV download","Automated live Yahoo Finance API integration"],
               ["Feature Engineering","None","15+ technical indicators via TA-Lib"],
               ["Explainability","None","SHAP feature importance + plain-English summary"],
               ["Visualization","Static Matplotlib plots","Interactive Plotly financial dashboards"],
               ["Model Comparison","Not available","Side-by-side RMSE / MAPE / Directional Accuracy"],
               ["Risk Analysis","Not available","VaR, volatility, Sharpe Ratio, drawdown"],
               ["Confidence Scoring","Not available","Calibrated confidence scores + uncertainty bounds"],
               ["Export","Not available","PDF executive report + CSV data export"],
               ["Multi-User System","Not available","4 roles with JWT authentication"],
               ["Cloud Deployment","Not available","Docker + AWS ECS production deployment"],
               ["Architecture","Notebook or local script","Full-stack web app with async ML workers"]]
    E.append(tbl(compare, widths=[5*cm, 4*cm, 7.5*cm]))
    E.append(sp(6))
    E.append(body("This project demonstrates expertise in <b>deep learning, financial data engineering, "
                  "full-stack development, cloud architecture, and explainable AI</b> — all in a single, "
                  "working product solving a real-world problem."))
    E.append(sp(10))

    # 18. FUTURE SCOPE
    E.append(h1("18. Future Scope"))
    E.append(sp())
    future = [("News Sentiment Analysis","Integrate live financial news via FinBERT NLP to add sentiment as a real-time prediction feature"),
              ("Reinforcement Learning Agent","Train a PPO-based RL agent to simulate buy/sell decision-making on historical data"),
              ("Portfolio Optimization","Use Modern Portfolio Theory (MPT) + AI to suggest diversified portfolio allocations"),
              ("Cryptocurrency Forecasting","Extend support to BTC, ETH, and other crypto assets — already available via yfinance"),
              ("Mutual Fund & ETF Analysis","NAV-based forecasting and sector rotation analysis for fund investors"),
              ("Real-Time Streaming","Live intraday data via WebSockets for minute-by-minute prediction updates"),
              ("AI Financial Assistant (LLM)","Chat interface: 'Why is Infosys falling this week?' answered by LLM + live data"),
              ("Mobile App","React Native companion app for portfolio watchlist and forecast push notifications")]
    frows = [[Paragraph("Future Feature", ParagraphStyle('FH',fontSize=9,fontName='Helvetica-Bold',
                                                          textColor=WHITE,leading=13)),
              Paragraph("Description", ParagraphStyle('FH2',fontSize=9,fontName='Helvetica-Bold',
                                                       textColor=WHITE,leading=13))]]
    for t, d in future:
        frows.append([Paragraph(f"<b>{t}</b>", ParagraphStyle('FT',fontSize=9,fontName='Helvetica-Bold',
                                                                textColor=PRIMARY,leading=13)),
                      Paragraph(d, ParagraphStyle('FD',fontSize=9,fontName='Helvetica',
                                                   textColor=DARK_TEXT,leading=13))])
    ft = Table(frows, colWidths=[5.5*cm, 11*cm])
    ft.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TBL_HDR),
                             ('ROWBACKGROUNDS',(0,1),(-1,-1),[TBL_R1,TBL_R2]),
                             ('ALIGN',(0,0),(-1,-1),'LEFT'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                             ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),
                             ('LEFTPADDING',(0,0),(-1,-1),8),
                             ('GRID',(0,0),(-1,-1),0.4,colors.HexColor("#86EFAC"))]))
    E.append(ft)
    E.append(sp(10))

    # 19. CONCLUSION
    E.append(h1("19. Conclusion"))
    E.append(sp())
    E.append(body("Financial markets are one of the most complex, data-rich environments on earth. Yet, "
                  "most individual investors and small analytical teams lack the tools, computing resources, "
                  "and AI expertise to extract structured intelligence from this data."))
    E.append(body("<b>MarketMind AI bridges this gap.</b> By combining multiple deep learning and machine "
                  "learning models, automated financial feature engineering, explainable AI outputs, "
                  "interactive visualizations, and a clean web interface — this platform puts sophisticated "
                  "financial forecasting capability within reach of any user, regardless of technical background."))
    E.append(body("This project is technically comprehensive — spanning a full-stack web application, "
                  "asynchronous multi-model ML pipelines, deep learning (LSTM, GRU, Temporal Fusion "
                  "Transformer), classical time-series models (Prophet, ARIMA), TA-Lib financial feature "
                  "engineering, SHAP explainability, cloud deployment, and a multi-role user system."))
    E.append(body("At the same time, it does so responsibly — by being fully transparent about its "
                  "limitations and positioning itself clearly as a research and decision-support tool, "
                  "not a financial advisor. This makes it both academically rigorous and professionally credible."))
    E.append(sp(24))
    E.append(rule())
    E.append(sp(8))
    sig = [[Paragraph("Submitted By", ParagraphStyle('SL',fontSize=9,fontName='Helvetica-Bold',
                                                      textColor=PRIMARY,leading=13,alignment=TA_CENTER)),
            Paragraph("Project Guide", ParagraphStyle('SL2',fontSize=9,fontName='Helvetica-Bold',
                                                       textColor=PRIMARY,leading=13,alignment=TA_CENTER))],
           [Paragraph("[Your Name]", ParagraphStyle('SN',fontSize=9,fontName='Helvetica',
                                                     textColor=DARK_TEXT,leading=13,alignment=TA_CENTER)),
            Paragraph("[Mentor Name]", ParagraphStyle('SN2',fontSize=9,fontName='Helvetica',
                                                       textColor=DARK_TEXT,leading=13,alignment=TA_CENTER))],
           [Paragraph("[Department]", ParagraphStyle('SD',fontSize=8,fontName='Helvetica',
                                                      textColor=MID_TEXT,leading=12,alignment=TA_CENTER)),
            Paragraph("[Department]", ParagraphStyle('SD2',fontSize=8,fontName='Helvetica',
                                                       textColor=MID_TEXT,leading=12,alignment=TA_CENTER))]]
    st = Table(sig, colWidths=[8*cm, 8.5*cm])
    st.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),
                             ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
                             ('LINEABOVE',(0,0),(0,0),1,PRIMARY),
                             ('LINEABOVE',(1,0),(1,0),1,PRIMARY)]))
    E.append(st)


# ─── HEADER / FOOTER ────────────────────────────────────────
def page_deco(canvas, doc):
    canvas.saveState()
    pw, ph = A4
    if doc.page > 1:
        canvas.setFillColor(PRIMARY)
        canvas.rect(0, ph - 1.2*cm, pw, 1.2*cm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(1.5*cm, ph - 0.75*cm, "MarketMind AI  |  AI-Powered Financial Intelligence & Forecasting Platform")
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(pw - 1.5*cm, ph - 0.75*cm, "Final Year Project Proposal")
        canvas.setFillColor(LIGHT_BG)
        canvas.rect(0, 0, pw, 1.0*cm, fill=1, stroke=0)
        canvas.setFillColor(MID_TEXT)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(1.5*cm, 0.38*cm, f"Page {doc.page}")
        canvas.drawCentredString(pw / 2, 0.38*cm, "Confidential — For Academic Review Only")
        canvas.drawRightString(pw - 1.5*cm, 0.38*cm, "2025–2026")
    canvas.restoreState()


# ─── BUILD ──────────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.6*cm, bottomMargin=1.5*cm,
        title="MarketMind AI — Financial Intelligence & Forecasting Platform Project Proposal",
        author="Final Year Student", subject="Final Year Project Proposal",
    )
    E = []
    cover_page(E)
    toc_page(E)
    build_content(E)
    doc.build(E, onFirstPage=page_deco, onLaterPages=page_deco)
    print(f"\n[OK] PDF Generated!\nSaved at: {OUTPUT_PATH}\n")


if __name__ == "__main__":
    build_pdf()
