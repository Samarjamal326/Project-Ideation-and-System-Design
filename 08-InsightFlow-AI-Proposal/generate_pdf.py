"""
PDF Generator for InsightFlow AI - No-Code Predictive Analytics Platform Project Proposal
Uses ReportLab to produce a professionally formatted, color-branded PDF document.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

OUTPUT_PATH = r"C:\Users\Prakash Gusain Ji\.gemini\antigravity-ide\scratch\Project-Ideation-and-System-Design\08-InsightFlow-AI-Proposal\Project-Proposal-InsightFlow-AI.pdf"

# ─────────────────────────────────────────────
# BRAND COLORS  (Deep Indigo + Violet accent)
# ─────────────────────────────────────────────
PRIMARY   = colors.HexColor("#2D1B69")   # Deep indigo
ACCENT    = colors.HexColor("#7C3AED")   # Violet
ACCENT2   = colors.HexColor("#10B981")   # Emerald green (highlights)
LIGHT_BG  = colors.HexColor("#F5F3FF")   # Soft lavender
WHITE     = colors.white
DARK_TEXT = colors.HexColor("#1A1A2E")
MID_TEXT  = colors.HexColor("#4B5563")
TBL_HDR   = colors.HexColor("#2D1B69")
TBL_R1    = colors.HexColor("#EDE9FE")
TBL_R2    = colors.white
RULE_CLR  = colors.HexColor("#7C3AED")

W_FULL = A4[0] - 4 * cm   # usable page width

# ─────────────────────────────────────────────
# PARAGRAPH STYLES
# ─────────────────────────────────────────────
def make_styles():
    s = {}
    s['H1'] = ParagraphStyle('H1', fontSize=15, textColor=WHITE,
                              fontName='Helvetica-Bold', alignment=TA_LEFT,
                              leading=22, spaceBefore=18, spaceAfter=8,
                              backColor=PRIMARY, borderPad=8)
    s['H2'] = ParagraphStyle('H2', fontSize=11, textColor=PRIMARY,
                              fontName='Helvetica-Bold', alignment=TA_LEFT,
                              leading=17, spaceBefore=12, spaceAfter=4)
    s['H3'] = ParagraphStyle('H3', fontSize=9.5, textColor=ACCENT,
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
    s['Code'] = ParagraphStyle('Code', fontSize=8, textColor=DARK_TEXT,
                                fontName='Courier', alignment=TA_LEFT,
                                leading=12, spaceBefore=4, spaceAfter=4,
                                leftIndent=16, backColor=LIGHT_BG, borderPad=6)
    s['TOC'] = ParagraphStyle('TOC', fontSize=10, textColor=DARK_TEXT,
                               fontName='Helvetica', alignment=TA_LEFT,
                               leading=18, leftIndent=8)
    return s

S = make_styles()


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def h1(text): return Paragraph(f"&nbsp;&nbsp;{text}", S['H1'])
def h2(text): return Paragraph(text, S['H2'])
def h3(text): return Paragraph(text, S['H3'])
def body(text): return Paragraph(text, S['Body'])
def bullet(text): return Paragraph(f"• &nbsp;{text}", S['Bullet'])
def note(text): return Paragraph(text, S['Note'])
def sp(n=6): return Spacer(1, n)
def rule(): return HRFlowable(width="100%", thickness=1,
                               color=RULE_CLR, spaceAfter=6, spaceBefore=6)

def make_table(rows, col_widths=None, header=True):
    if col_widths is None:
        col_widths = [W_FULL / len(rows[0])] * len(rows[0])
    t = Table(rows, colWidths=col_widths, repeatRows=1 if header else 0)
    t.setStyle(TableStyle([
        ('FONTNAME',  (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE',  (0, 0), (-1, 0), 9),
        ('BACKGROUND',(0, 0), (-1, 0), TBL_HDR),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME',  (0, 1), (-1,-1), 'Helvetica'),
        ('FONTSIZE',  (0, 1), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0, 1), (-1,-1), [TBL_R1, TBL_R2]),
        ('GRID',      (0, 0), (-1,-1), 0.4, colors.HexColor("#C4B5FD")),
        ('ALIGN',     (0, 0), (-1,-1), 'LEFT'),
        ('VALIGN',    (0, 0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0, 0), (-1,-1), 5),
        ('BOTTOMPADDING', (0, 0), (-1,-1), 5),
        ('LEFTPADDING',   (0, 0), (-1,-1), 8),
        ('RIGHTPADDING',  (0, 0), (-1,-1), 8),
    ]))
    return t


# ─────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────
def cover_page(elems):
    # Main title banner
    title_row = [[Paragraph(
        "<b>InsightFlow AI</b>",
        ParagraphStyle('T1', fontSize=32, textColor=WHITE, fontName='Helvetica-Bold',
                       alignment=TA_CENTER, leading=40)
    )]]
    title_tbl = Table(title_row, colWidths=[W_FULL])
    title_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 36),
        ('BOTTOMPADDING', (0,0),(-1,-1), 8),
        ('ALIGN',         (0,0),(-1,-1), 'CENTER'),
    ]))
    elems.append(title_tbl)

    sub_row = [[Paragraph(
        "No-Code Predictive Analytics Platform",
        ParagraphStyle('T2', fontSize=16, textColor=colors.HexColor("#C4B5FD"),
                       fontName='Helvetica', alignment=TA_CENTER, leading=22)
    )]]
    sub_tbl = Table(sub_row, colWidths=[W_FULL])
    sub_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), PRIMARY),
        ('TOPPADDING',    (0,0),(-1,-1), 4),
        ('BOTTOMPADDING', (0,0),(-1,-1), 36),
        ('ALIGN',         (0,0),(-1,-1), 'CENTER'),
    ]))
    elems.append(sub_tbl)
    elems.append(sp(14))

    # Tagline badge
    badge_row = [[Paragraph(
        "<b>Final Year Project Proposal &nbsp;|&nbsp; B.E. / B.Tech Computer Science / AI &amp; ML</b>",
        ParagraphStyle('B1', fontSize=10, textColor=WHITE, fontName='Helvetica-Bold',
                       alignment=TA_CENTER, leading=16)
    )]]
    badge_tbl = Table(badge_row, colWidths=[W_FULL])
    badge_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), ACCENT),
        ('TOPPADDING',    (0,0),(-1,-1), 10),
        ('BOTTOMPADDING', (0,0),(-1,-1), 10),
        ('ALIGN',         (0,0),(-1,-1), 'CENTER'),
    ]))
    elems.append(badge_tbl)
    elems.append(sp(36))

    # Metadata
    meta = [
        ("Submitted By", "[Your Name]"),
        ("Department", "[Your Department]"),
        ("Institution", "[Your College Name]"),
        ("Academic Year", "2025 – 2026"),
        ("Project Guide / Mentor", "[Mentor Name]"),
        ("Date", "July 2026"),
    ]
    meta_rows = [
        [Paragraph(f"<b>{k}</b>", ParagraphStyle('MK', fontSize=10, fontName='Helvetica-Bold',
                                                   textColor=PRIMARY, leading=16)),
         Paragraph(v, ParagraphStyle('MV', fontSize=10, fontName='Helvetica',
                                      textColor=DARK_TEXT, leading=16))]
        for k, v in meta
    ]
    mt = Table(meta_rows, colWidths=[6*cm, 10*cm])
    mt.setStyle(TableStyle([
        ('ALIGN',  (0,0),(-1,-1), 'LEFT'),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),(-1,-1), 6),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('LINEBELOW', (0,0),(-1,-2), 0.3, colors.HexColor("#D1D5DB")),
    ]))
    elems.append(mt)
    elems.append(PageBreak())


# ─────────────────────────────────────────────
# TABLE OF CONTENTS
# ─────────────────────────────────────────────
def toc_page(elems):
    elems.append(h1("Table of Contents"))
    elems.append(sp(10))
    toc = [
        ("1.", "Executive Summary"),
        ("2.", "Problem Statement"),
        ("3.", "Proposed Solution"),
        ("4.", "Supported Machine Learning Tasks"),
        ("5.", "Supported Models"),
        ("6.", "User Workflow"),
        ("7.", "User Roles & Responsibilities"),
        ("8.", "Platform Features"),
        ("9.", "AI & Intelligence Features"),
        ("10.", "Implementation Plan"),
        ("11.", "Technology Stack"),
        ("12.", "System Architecture"),
        ("13.", "Research Potential"),
        ("14.", "Facts & Industry Figures"),
        ("15.", "Why This Is a Major Project"),
        ("16.", "Future Scope"),
        ("17.", "Conclusion"),
    ]
    toc_rows = [
        [Paragraph(f"<b>{n}</b>", ParagraphStyle('TN', fontSize=9.5, fontName='Helvetica-Bold',
                                                   textColor=ACCENT, leading=15)),
         Paragraph(t, ParagraphStyle('TT', fontSize=9.5, fontName='Helvetica',
                                      textColor=DARK_TEXT, leading=15))]
        for n, t in toc
    ]
    tt = Table(toc_rows, colWidths=[1.2*cm, 14*cm])
    tt.setStyle(TableStyle([
        ('ALIGN',  (0,0),(-1,-1), 'LEFT'),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('ROWBACKGROUNDS', (0,0),(-1,-1), [LIGHT_BG, WHITE]),
    ]))
    elems.append(tt)
    elems.append(PageBreak())


# ─────────────────────────────────────────────
# MAIN CONTENT
# ─────────────────────────────────────────────
def build_content(elems):

    # ── 1. EXECUTIVE SUMMARY ────────────────
    elems.append(h1("1. Executive Summary"))
    elems.append(sp())
    elems.append(body(
        "Every organization today generates data. Banks track transactions. Hospitals record patient "
        "histories. Retailers log sales. Schools monitor student grades. Yet, for most of these "
        "organizations, this data sits unused — because turning raw data into predictions requires "
        "programming skills, machine learning expertise, and expensive infrastructure that most "
        "businesses simply do not have."
    ))
    elems.append(body(
        "<b>InsightFlow AI</b> is a No-Code Predictive Analytics Platform that changes this entirely. "
        "Instead of writing Python code or hiring a team of data scientists, business users simply "
        "upload their dataset, select their business problem, and the platform automatically cleans "
        "the data, selects the best machine learning models, trains them, evaluates performance, "
        "generates visual analytics, and produces a downloadable report — all through a simple, "
        "intuitive web interface."
    ))
    elems.append(body(
        "This is a complete, production-ready final-year project that brings together full-stack "
        "engineering, machine learning pipelines, cloud deployment, and applied AI into a single, "
        "powerful platform."
    ))
    elems.append(sp(10))

    # ── 2. PROBLEM STATEMENT ────────────────
    elems.append(h1("2. Problem Statement"))
    elems.append(sp())
    elems.append(h2("2.1  Data Without Intelligence"))
    elems.append(body(
        "Organizations across every industry are sitting on valuable data but lack the tools "
        "and expertise to extract predictions from it:"
    ))
    t1 = [
        ["Industry", "Data They Collect", "Predictions They Need"],
        ["Banking", "Transactions, loan history, credit scores", "Loan approval, fraud detection, churn"],
        ["Healthcare", "Patient records, lab reports, diagnostics", "Disease risk, readmission prediction"],
        ["Retail", "Sales logs, purchase history", "Demand forecasting, product recommendations"],
        ["Insurance", "Policy data, claim history, demographics", "Claim prediction, risk scoring"],
        ["Education", "Grades, attendance, behavior", "Performance prediction, dropout risk"],
        ["E-Commerce", "Browse history, cart data, reviews", "Segmentation, sentiment analysis"],
    ]
    elems.append(make_table(t1, col_widths=[3*cm, 6*cm, 7.5*cm]))
    elems.append(sp(8))

    elems.append(h2("2.2  Why Organizations Cannot Use Machine Learning Today"))
    barriers = [
        ("<b>Barrier 1 — It Requires Programming:</b>",
         "Machine learning requires writing Python code using libraries like Pandas, Scikit-Learn, "
         "TensorFlow, and PyTorch. Most business users — managers, analysts, doctors, teachers — "
         "are not programmers."),
        ("<b>Barrier 2 — It Is Expensive:</b>",
         "Hiring a professional data scientist costs between Rs.8–25 lakhs per year. "
         "For small and medium organizations, this is simply unaffordable."),
        ("<b>Barrier 3 — It Is Slow:</b>",
         "Building a custom ML model — from data cleaning to deployment — typically takes 4–12 weeks. "
         "Business decisions cannot wait that long."),
        ("<b>Barrier 4 — Existing Platforms Are Inaccessible:</b>",
         "Enterprise ML platforms like DataRobot or Google AutoML require cloud configuration, "
         "IT knowledge, and significant setup overhead, making them unsuitable for non-technical users."),
    ]
    for title, desc in barriers:
        elems.append(Paragraph(title, S['Body']))
        elems.append(body(desc))
        elems.append(sp(4))

    elems.append(h2("2.3  The Gap"))
    elems.append(body(
        "There is a clear and growing gap: organizations have data, but they lack the AI expertise "
        "and tools to make predictions from it. <b>InsightFlow AI fills this gap.</b>"
    ))
    elems.append(sp(10))

    # ── 3. PROPOSED SOLUTION ────────────────
    elems.append(h1("3. Proposed Solution"))
    elems.append(sp())
    elems.append(body(
        "InsightFlow AI is a web-based No-Code Machine Learning platform. Users interact with a "
        "guided, step-by-step interface — no programming required at any stage."
    ))
    elems.append(sp(6))
    workflow = [
        ["Step", "What Happens", "Automated?"],
        ["1. Upload Dataset", "User drags and drops a CSV or Excel file", "User action"],
        ["2. Data Profiling", "Platform detects column types, missing values, distributions", "Fully Automated"],
        ["3. Select Problem", "User describes goal: e.g., 'Predict customer churn'", "User action"],
        ["4. Model Recommendation", "Platform suggests the 3 best ML models for the task", "AI-Powered"],
        ["5. Preprocessing", "Missing values, encoding, normalization — applied automatically", "Fully Automated"],
        ["6. Model Training", "Background training — progress bar shown on screen", "Fully Automated"],
        ["7. Evaluation", "Accuracy, F1, ROC curves, Confusion Matrix generated", "Fully Automated"],
        ["8. Predictions", "Platform generates predictions on new data", "Fully Automated"],
        ["9. Visualization", "Interactive Plotly charts and SHAP feature importance", "Fully Automated"],
        ["10. Export Report", "PDF executive report + CSV predictions downloaded in one click", "Fully Automated"],
    ]
    elems.append(make_table(workflow, col_widths=[4*cm, 8.5*cm, 4*cm]))
    elems.append(sp(10))

    # ── 4. ML TASKS ────────────────
    elems.append(h1("4. Supported Machine Learning Tasks"))
    elems.append(sp())
    tasks = [
        ["ML Task", "What It Does", "Business Example"],
        ["Classification", "Predicts which category a record belongs to", "Will this customer churn? (Yes / No)"],
        ["Regression", "Predicts a continuous numerical value", "What will the house price be next month?"],
        ["Clustering", "Groups similar records together automatically", "Segment customers by spending behavior"],
        ["Time Series Forecasting", "Predicts future values based on past trends", "Forecast next quarter's sales revenue"],
        ["Recommendation Systems", "Suggests items based on preference history", "Recommend products to a user"],
        ["Anomaly Detection", "Identifies unusual or suspicious records", "Flag fraudulent bank transactions"],
        ["Natural Language Processing", "Analyzes and understands text data", "Analyze customer review sentiment"],
    ]
    elems.append(make_table(tasks, col_widths=[4.5*cm, 5.5*cm, 6.5*cm]))
    elems.append(sp(10))

    # ── 5. MODELS ────────────────
    elems.append(h1("5. Supported Models"))
    elems.append(sp())

    model_groups = [
        ("Classification Models", [
            ("Logistic Regression", "Fast, reliable baseline for binary Yes/No outcomes"),
            ("Decision Tree", "Visual tree of decisions — easy to explain and interpret"),
            ("Random Forest", "Combines hundreds of trees for high accuracy"),
            ("XGBoost", "Industry-standard gradient boosting — top performer on tabular data"),
            ("SVM", "Excellent on smaller datasets with clear decision boundaries"),
            ("Naive Bayes", "Fast probabilistic model — ideal for text classification"),
        ]),
        ("Regression Models", [
            ("Linear Regression", "Baseline model for predicting continuous numeric values"),
            ("Ridge Regression", "Adds penalty to prevent model overfitting"),
            ("Lasso Regression", "Automatically eliminates irrelevant features during training"),
            ("Random Forest Regressor", "Ensemble-based accurate numeric predictor"),
            ("XGBoost Regressor", "High-performance regression on tabular business data"),
        ]),
        ("Clustering Models", [
            ("KMeans", "Groups data into K user-defined clusters — fast and scalable"),
            ("DBSCAN", "Discovers clusters of any shape — handles noisy data well"),
            ("Hierarchical Clustering", "Builds a tree of clusters — useful for exploring structure"),
        ]),
        ("Time Series Models", [
            ("Prophet", "Developed by Meta — handles seasonality and holidays automatically"),
            ("ARIMA", "Classical statistical forecasting — reliable for stable time series"),
            ("LSTM (Deep Learning)", "Neural network for complex multi-variable time series"),
        ]),
        ("Recommendation Models", [
            ("Collaborative Filtering", "Recommends based on what similar users liked"),
            ("Content-Based Recommendation", "Recommends based on item attributes and user profile"),
        ]),
        ("NLP Models", [
            ("TF-IDF + Classifier", "Fast keyword-based text classification"),
            ("BERT Transformer", "State-of-the-art contextual language understanding"),
            ("Sentiment Analysis", "Classifies text as Positive, Neutral, or Negative"),
        ]),
    ]

    for group_name, models in model_groups:
        elems.append(h2(group_name))
        rows = [["Model", "Description"]] + [[m, d] for m, d in models]
        elems.append(make_table(rows, col_widths=[4.5*cm, 12*cm]))
        elems.append(sp(6))
    elems.append(sp(6))

    # ── 6. USER WORKFLOW ────────────────
    elems.append(h1("6. User Workflow"))
    elems.append(sp())
    elems.append(body(
        "The platform guides every user through a simple eight-step process. "
        "No technical knowledge is required at any stage."
    ))
    uw = [
        ["Step", "What Happens", "User Effort"],
        ["1. Upload Dataset", "Drag-and-drop a CSV or Excel file", "Minimal — just upload"],
        ["2. Choose Industry", "Select: Banking / Healthcare / Retail / Other", "One click"],
        ["3. Select Problem Type", "Describe the goal (e.g., 'Predict loan approval')", "One click"],
        ["4. Platform Analyzes Data", "Schema detection, data quality report, missing value summary", "Automated"],
        ["5. Configure Parameters", "Choose target column and train/test split ratio", "Simple dropdowns"],
        ["6. Run Model", "Background training with live progress bar", "One click"],
        ["7. View Results", "Accuracy, Confusion Matrix, SHAP charts, predictions", "Interactive view"],
        ["8. Download Report", "Full PDF report + CSV predictions", "One click"],
    ]
    elems.append(make_table(uw, col_widths=[4.5*cm, 7.5*cm, 4.5*cm]))
    elems.append(sp(10))

    # ── 7. USER ROLES ────────────────
    elems.append(h1("7. User Roles & Responsibilities"))
    elems.append(sp())
    roles = [
        ["Role", "Who They Are", "What They Can Do"],
        ["Business User", "Analyst, manager, domain expert", "Upload data, run predictions, export results"],
        ["ML Administrator", "Data science lead / internal tech team", "Configure models, manage compute, set quotas"],
        ["Platform Administrator", "IT or SaaS admin", "Manage users, monitor system health, configure settings"],
        ["Enterprise Customer", "Company-level account", "Dedicated workspace, team projects, API integration"],
    ]
    elems.append(make_table(roles, col_widths=[4*cm, 5*cm, 7.5*cm]))
    elems.append(sp(10))

    # ── 8. PLATFORM FEATURES ────────────────
    elems.append(h1("8. Platform Features"))
    elems.append(sp())

    feature_groups = [
        ("Data Management", [
            ("Dataset Upload", "Drag-and-drop CSV/Excel upload with file validation and column preview"),
            ("Automatic Data Profiling", "Instantly summarize each column — type, missing %, unique values, distribution"),
            ("Missing Value Handling", "Impute missing data using mean, median, mode, or smart interpolation — automatically"),
            ("Feature Encoding", "Convert categorical columns into machine-readable numbers — automatically"),
            ("Normalization / Scaling", "Scale numeric features so all models perform consistently"),
        ]),
        ("Model Intelligence", [
            ("Model Recommendation Engine", "Suggests the top 3 most suitable models based on dataset and task type"),
            ("Model Training", "Background async training — users see a live progress bar"),
            ("Model Comparison", "Train multiple models side-by-side and compare performance in one table"),
            ("Model Versioning", "Save and manage multiple model versions — track improvements over time"),
            ("Hyperparameter Tuning", "Auto-find best model settings using Optuna Bayesian search"),
        ]),
        ("Visualization & Analytics", [
            ("Performance Charts", "ROC-AUC, Confusion Matrix, Loss curves — interactive Plotly charts"),
            ("Prediction Dashboard", "Run real-time predictions on single rows or batch CSV uploads"),
            ("SHAP Feature Importance", "Visual explanation of which columns drive each prediction"),
            ("Interactive Charts", "Zoomable, filterable charts that respond to user interaction"),
        ]),
        ("Project & Export", [
            ("Project Management", "Organize datasets and experiments into named projects"),
            ("Export Reports", "Download PDF executive reports or CSV prediction files in one click"),
            ("API Access", "Auto-generated REST API endpoint for each trained model"),
        ]),
    ]

    for group_name, features in feature_groups:
        elems.append(h2(group_name))
        rows = [["Feature", "Description"]] + [[f, d] for f, d in features]
        elems.append(make_table(rows, col_widths=[5*cm, 11.5*cm]))
        elems.append(sp(6))
    elems.append(sp(6))

    # ── 9. AI FEATURES ────────────────
    elems.append(h1("9. AI & Intelligence Features"))
    elems.append(sp())
    elems.append(body(
        "These smart features go beyond standard ML training — they make the platform genuinely "
        "intelligent and helpful to non-technical users."
    ))
    ai = [
        ["AI Feature", "What It Does"],
        ["Automatic Model Recommendation", "Analyzes dataset characteristics to suggest the best model — no expertise needed"],
        ["Automatic Feature Selection", "Identifies the most informative columns and removes irrelevant ones automatically"],
        ["Explainable AI (XAI)", "Explains every prediction in plain English — not just a probability number"],
        ["SHAP Feature Importance", "Visual charts showing which input column influenced each prediction the most"],
        ["Hyperparameter Auto-Tuning", "Runs many configurations automatically using Optuna Bayesian search"],
        ["Business Insight Generator", "Generates a short plain-English paragraph summarizing key model findings"],
        ["LLM Dataset Assistant", "Users ask questions in plain English — e.g., 'What is the average salary by dept?'"],
        ["Natural Language Query", "Type queries like 'Show customers likely to churn' — platform interprets and responds"],
        ["Dataset Summary Generator", "Auto-writes a one-page summary of the dataset — distributions, anomalies, statistics"],
    ]
    elems.append(make_table(ai, col_widths=[5.5*cm, 11*cm]))
    elems.append(sp(4))
    elems.append(note(
        "Feasibility Note: LLM features use the OpenAI GPT API or a locally hosted Mistral 7B model. "
        "They are optional add-ons and do not affect core ML functionality."
    ))
    elems.append(sp(10))

    # ── 10. IMPLEMENTATION PLAN ────────────────
    elems.append(h1("10. Implementation Plan"))
    elems.append(sp())
    impl = [
        ["Phase", "Timeline", "Key Deliverables"],
        ["Phase 1 — Foundation", "Month 1",
         "Project setup, PostgreSQL schema, FastAPI backend, JWT auth, Next.js UI shell, file upload system"],
        ["Phase 2 — ML Engine Core", "Months 2–3",
         "Data profiling, preprocessing pipeline, Scikit-Learn training, evaluation metrics, Celery async queues"],
        ["Phase 3 — Visualization & AI", "Month 4",
         "Plotly dashboards, SHAP integration, model comparison, LLM dataset assistant, PDF/CSV report generator"],
        ["Phase 4 — Deployment & Polish", "Month 5",
         "Docker containerization, AWS ECS deployment, API gateway, end-to-end testing, performance optimization"],
    ]
    rows = [
        [Paragraph(f"<b>{r[0]}</b>" if i==0 else r[0],
                   ParagraphStyle('IC', fontSize=9, fontName='Helvetica-Bold' if i==0 else 'Helvetica',
                                  textColor=WHITE if i==0 else PRIMARY, leading=13)),
         Paragraph(r[1], ParagraphStyle('IT', fontSize=9,
                                         fontName='Helvetica-Bold' if i==0 else 'Helvetica',
                                         textColor=WHITE if i==0 else ACCENT, leading=13, alignment=TA_CENTER)),
         Paragraph(r[2], ParagraphStyle('ID', fontSize=9,
                                         fontName='Helvetica-Bold' if i==0 else 'Helvetica',
                                         textColor=WHITE if i==0 else DARK_TEXT, leading=13))]
        for i, r in enumerate(impl)
    ]
    it = Table(rows, colWidths=[3.8*cm, 2.5*cm, 10.2*cm])
    it.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  TBL_HDR),
        ('BACKGROUND',    (0,1),(-1,1),  colors.HexColor("#EDE9FE")),
        ('BACKGROUND',    (0,2),(-1,2),  colors.HexColor("#D1FAE5")),
        ('BACKGROUND',    (0,3),(-1,3),  colors.HexColor("#FEF3C7")),
        ('BACKGROUND',    (0,4),(-1,4),  colors.HexColor("#FCE7F3")),
        ('ALIGN',  (0,0),(-1,-1), 'LEFT'),
        ('ALIGN',  (1,0),(1,-1),  'CENTER'),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),(-1,-1), 8),
        ('BOTTOMPADDING', (0,0),(-1,-1), 8),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('GRID', (0,0),(-1,-1), 0.4, colors.HexColor("#C4B5FD")),
    ]))
    elems.append(it)
    elems.append(sp(10))

    # ── 11. TECH STACK ────────────────
    elems.append(h1("11. Technology Stack"))
    elems.append(sp())
    tech = [
        ["Layer", "Technology", "Why This Was Chosen"],
        ["Frontend", "Next.js (React)", "Fast, component-based — industry standard for web apps"],
        ["Backend API", "FastAPI (Python)", "Async, high-performance — ideal for ML workloads"],
        ["ML Core", "Scikit-Learn", "Industry-standard classical ML — wide algorithm coverage"],
        ["Deep Learning", "TensorFlow / PyTorch", "For LSTM time series and BERT NLP models"],
        ["Database", "PostgreSQL", "Robust relational DB — excellent for structured metadata"],
        ["Task Queue", "Celery + Redis", "Background model training without blocking the web server"],
        ["Visualization", "Plotly", "Interactive, web-ready charts — works natively with React"],
        ["Storage", "AWS S3", "Scalable cloud storage for datasets and trained model artifacts"],
        ["Authentication", "JWT + RBAC", "Secure, stateless tokens with fine-grained role control"],
        ["Deployment", "Docker + AWS ECS", "Containerized, portable, production-ready cloud hosting"],
        ["AI Features", "OpenAI API / Optuna", "Powers LLM assistant and automatic hyperparameter tuning"],
    ]
    elems.append(make_table(tech, col_widths=[3.5*cm, 4.5*cm, 8.5*cm]))
    elems.append(sp(10))

    # ── 12. ARCHITECTURE ────────────────
    elems.append(h1("12. System Architecture"))
    elems.append(sp())
    elems.append(body(
        "The platform follows a clean, layered architecture. The frontend communicates with the FastAPI "
        "backend via REST API. Heavy ML training is offloaded to Celery worker nodes so the web server "
        "stays responsive. Each layer is independently deployable and horizontally scalable."
    ))
    elems.append(sp(6))
    arch = [
        ["Layer", "Component", "Responsibility"],
        ["Client Layer", "Next.js Frontend", "UI, routing, real-time progress, charts"],
        ["API Layer", "FastAPI Backend", "Business logic, auth, job dispatch"],
        ["Data Layer", "PostgreSQL + Redis", "Persistent storage + session/queue caching"],
        ["Worker Layer", "Celery ML Workers", "Profiling, preprocessing, training, evaluation"],
        ["Model Layer", "Scikit-Learn / PyTorch / TF", "Algorithm execution and artifact management"],
        ["AI Layer", "OpenAI API / Optuna", "LLM assistant and hyperparameter optimization"],
        ["Storage Layer", "AWS S3", "Dataset files and trained model artifacts"],
        ["Deployment", "Docker + AWS ECS", "Containerized, auto-scaled cloud hosting"],
    ]
    elems.append(make_table(arch, col_widths=[3.5*cm, 5*cm, 8*cm]))
    elems.append(sp(8))
    elems.append(h2("Architecture Diagram"))
    elems.append(sp(4))
    arch_code = [
        "graph TD",
        "    User([Business User / Browser]) -->|HTTPS| FE[Next.js Frontend]",
        "    FE -->|REST API| API[FastAPI Backend]",
        "    API --> DB[(PostgreSQL DB)]",
        "    API --> Redis[(Redis Cache & Broker)]",
        "    API --> S3[(AWS S3 Storage)]",
        "    API --> LLM[LLM Service - OpenAI API]",
        "    subgraph ML Worker Cluster",
        "        Redis --> Profiler[Data Profiling Worker]",
        "        Redis --> Preproc[Preprocessing Worker]",
        "        Redis --> Recommender[Model Recommendation Engine]",
        "        Redis --> Trainer[Model Training Worker]",
        "        Redis --> Evaluator[Evaluation & SHAP Worker]",
        "        Redis --> Reporter[Report Generator - PDF/CSV]",
        "    end",
        "    Trainer --> S3",
        "    Evaluator --> DB",
        "    Reporter --> S3",
    ]
    for line in arch_code:
        elems.append(Paragraph(line, S['Code']))
    elems.append(note(
        "Diagram above is in Mermaid.js format — renderable in GitHub Markdown, Notion, or any Mermaid-compatible viewer."
    ))
    elems.append(sp(10))

    # ── 13. RESEARCH POTENTIAL ────────────────
    elems.append(h1("13. Research Potential"))
    elems.append(sp())
    elems.append(body(
        "InsightFlow AI opens multiple genuine research directions across active areas of AI and HCI:"
    ))
    research = [
        ["Research Area", "Description"],
        ["AutoML & Model Recommendation", "Study how to best recommend algorithms based on dataset meta-features (size, type, cardinality)"],
        ["Explainable AI (XAI)", "Research how to present SHAP/LIME explanations in ways non-technical users can understand"],
        ["AI Democratization", "Case study on how No-Code AI platforms change who can use ML in organizations"],
        ["Human-AI Interaction", "How do business users make decisions when AI gives probability scores and confidence bounds?"],
        ["Dataset Understanding", "Algorithms that automatically summarize and recommend actions for unknown datasets"],
        ["No-Code Platform Design", "UI/UX research on best interface patterns for guiding non-programmers through ML"],
        ["Benchmark Study", "Evaluate how AutoML pipelines compare to expert hand-tuned models on business datasets"],
    ]
    elems.append(make_table(research, col_widths=[5*cm, 11.5*cm]))
    elems.append(sp(10))

    # ── 14. FACTS & FIGURES ────────────────
    elems.append(h1("14. Facts & Industry Figures"))
    elems.append(sp())
    facts = [
        ["Statistic", "Source"],
        ["Global AI market expected to reach $1.81 trillion by 2030", "Grand View Research, 2024"],
        ["AutoML market valued at $1.14B in 2023 — growing at 44.6% CAGR", "MarketsandMarkets, 2023"],
        ["Global Business Intelligence market projected at $33.3B by 2025", "Fortune Business Insights"],
        ["Only 26% of organizations have successfully deployed ML models at scale", "Gartner, 2023"],
        ["87% of data science projects never reach production", "VentureBeat Research"],
        ["Low-code / no-code AI market growing at 28.1% CAGR", "IDC Research, 2023"],
        ["Demand for AI automation tools grew 65% between 2021 and 2024", "McKinsey Digital, 2024"],
    ]
    elems.append(make_table(facts, col_widths=[10*cm, 6.5*cm]))
    elems.append(sp(10))

    # ── 15. WHY MAJOR PROJECT ────────────────
    elems.append(h1("15. Why This Is a Major Project"))
    elems.append(sp())
    elems.append(body(
        "This is not a simple 'train a model and show accuracy' project. "
        "Here is a direct comparison:"
    ))
    compare = [
        ["Dimension", "Basic ML Notebook", "InsightFlow AI Platform"],
        ["User Interface", "None — Python code only", "Full Next.js web application"],
        ["ML Tasks Covered", "1 specific task", "7 complete task categories"],
        ["Models Available", "1 or 2 models", "20+ production-ready models"],
        ["Data Preprocessing", "Manual coding required", "Fully automated pipeline"],
        ["Model Recommendation", "Not available", "AI-powered recommendation engine"],
        ["Model Comparison", "Manual side-by-side", "Automated comparison dashboard"],
        ["Explainability", "Not available", "SHAP visualizations + plain text"],
        ["Async Training", "Blocking execution", "Celery worker queue"],
        ["Visualization", "Static Matplotlib plots", "Interactive Plotly dashboards"],
        ["Report Export", "Not available", "PDF executive report + CSV"],
        ["API Access", "Not available", "Auto-generated REST API per model"],
        ["LLM Assistant", "Not available", "NLP-powered dataset Q&A"],
        ["Cloud Deployment", "Not available", "Docker + AWS ECS production"],
        ["User Roles", "Not applicable", "4 distinct roles with RBAC"],
    ]
    elems.append(make_table(compare, col_widths=[5*cm, 4.5*cm, 7*cm]))
    elems.append(sp(6))
    elems.append(body(
        "This project demonstrates expertise in <b>full-stack development, machine learning "
        "engineering, cloud architecture, applied AI, and product design</b> — all integrated "
        "into a single, working product."
    ))
    elems.append(sp(10))

    # ── 16. FUTURE SCOPE ────────────────
    elems.append(h1("16. Future Scope"))
    elems.append(sp())
    future = [
        ("LLM-Powered Generative BI Reports",
         "Automatically generate a full business intelligence narrative using LLMs — "
         "explaining patterns, trends, and risks in plain English."),
        ("Voice-Based Analytics Interface",
         "Allow users to speak queries and receive spoken + visual responses."),
        ("Real-Time Streaming Analytics",
         "Support live data ingestion via Kafka for real-time prediction on streaming events."),
        ("Auto Feature Engineering",
         "Automatically create new predictive features from existing data to improve accuracy."),
        ("MLOps Integration",
         "Connect to CI/CD pipelines so models retrain automatically when new data arrives."),
        ("Enterprise Dashboard",
         "Multi-team collaboration workspace with shared datasets, models, and access controls."),
        ("Cloud AutoML",
         "Leverage Google Vertex AI or AWS SageMaker Autopilot as training backends for large datasets."),
        ("Multi-Modal AI",
         "Support image and audio datasets in addition to tabular and text data."),
    ]
    f_rows = [
        [Paragraph("Future Feature", ParagraphStyle('FH', fontSize=9, fontName='Helvetica-Bold',
                                                     textColor=WHITE, leading=13)),
         Paragraph("Description", ParagraphStyle('FH2', fontSize=9, fontName='Helvetica-Bold',
                                                  textColor=WHITE, leading=13))]
    ]
    for t, d in future:
        f_rows.append([
            Paragraph(f"<b>{t}</b>", ParagraphStyle('FT', fontSize=9, fontName='Helvetica-Bold',
                                                     textColor=PRIMARY, leading=13)),
            Paragraph(d, ParagraphStyle('FD', fontSize=9, fontName='Helvetica',
                                        textColor=DARK_TEXT, leading=13))
        ])
    ft = Table(f_rows, colWidths=[5.5*cm, 11*cm])
    ft.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0), TBL_HDR),
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [TBL_R1, TBL_R2]),
        ('ALIGN',  (0,0),(-1,-1), 'LEFT'),
        ('VALIGN', (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),(-1,-1), 6),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('LEFTPADDING',   (0,0),(-1,-1), 8),
        ('GRID', (0,0),(-1,-1), 0.4, colors.HexColor("#C4B5FD")),
    ]))
    elems.append(ft)
    elems.append(sp(10))

    # ── 17. CONCLUSION ────────────────
    elems.append(h1("17. Conclusion"))
    elems.append(sp())
    elems.append(body(
        "Organizations across every industry — banking, healthcare, retail, education, and insurance — "
        "collect enormous amounts of structured data every day. Yet, the majority of this data goes "
        "unused for predictions, because machine learning today requires expensive expertise, months "
        "of development, and deep programming knowledge."
    ))
    elems.append(body(
        "<b>InsightFlow AI solves this directly.</b> By wrapping the entire machine learning lifecycle — "
        "data upload, preprocessing, model selection, training, evaluation, visualization, and export — "
        "inside a clean, guided web interface, this platform puts the power of AI in the hands of "
        "business users who have never written a single line of code."
    ))
    elems.append(body(
        "The project is technically ambitious — spanning a full-stack web application, asynchronous ML "
        "worker pipelines, seven machine learning paradigms with 20+ models, explainable AI, an "
        "LLM-powered assistant, interactive visualizations, and cloud deployment. At the same time, "
        "it addresses a clear, real-world problem that affects millions of organizations globally."
    ))
    elems.append(body(
        "This is the kind of project that makes a strong final-year thesis, produces publishable "
        "research, and builds a portfolio that stands out to any employer in software engineering "
        "or data science."
    ))
    elems.append(sp(24))
    rule()
    elems.append(sp(8))

    sig_rows = [
        [Paragraph("Submitted By", ParagraphStyle('SL', fontSize=9, fontName='Helvetica-Bold',
                                                   textColor=PRIMARY, leading=13, alignment=TA_CENTER)),
         Paragraph("Project Guide", ParagraphStyle('SL2', fontSize=9, fontName='Helvetica-Bold',
                                                    textColor=PRIMARY, leading=13, alignment=TA_CENTER))],
        [Paragraph("[Your Name]", ParagraphStyle('SN', fontSize=9, fontName='Helvetica',
                                                  textColor=DARK_TEXT, leading=13, alignment=TA_CENTER)),
         Paragraph("[Mentor Name]", ParagraphStyle('SN2', fontSize=9, fontName='Helvetica',
                                                    textColor=DARK_TEXT, leading=13, alignment=TA_CENTER))],
        [Paragraph("[Department]", ParagraphStyle('SD', fontSize=8, fontName='Helvetica',
                                                   textColor=MID_TEXT, leading=12, alignment=TA_CENTER)),
         Paragraph("[Department]", ParagraphStyle('SD2', fontSize=8, fontName='Helvetica',
                                                    textColor=MID_TEXT, leading=12, alignment=TA_CENTER))],
    ]
    sig_tbl = Table(sig_rows, colWidths=[8*cm, 8.5*cm])
    sig_tbl.setStyle(TableStyle([
        ('ALIGN',  (0,0),(-1,-1), 'CENTER'),
        ('TOPPADDING',    (0,0),(-1,-1), 8),
        ('BOTTOMPADDING', (0,0),(-1,-1), 8),
        ('LINEABOVE', (0,0),(0,0), 1, PRIMARY),
        ('LINEABOVE', (1,0),(1,0), 1, PRIMARY),
    ]))
    elems.append(sig_tbl)


# ─────────────────────────────────────────────
# HEADER / FOOTER CALLBACK
# ─────────────────────────────────────────────
def add_page_decoration(canvas, doc):
    canvas.saveState()
    pw, ph = A4
    if doc.page > 1:
        # Header
        canvas.setFillColor(PRIMARY)
        canvas.rect(0, ph - 1.2*cm, pw, 1.2*cm, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(1.5*cm, ph - 0.75*cm, "InsightFlow AI  |  No-Code Predictive Analytics Platform")
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(pw - 1.5*cm, ph - 0.75*cm, "Final Year Project Proposal")
        # Footer
        canvas.setFillColor(LIGHT_BG)
        canvas.rect(0, 0, pw, 1.0*cm, fill=1, stroke=0)
        canvas.setFillColor(MID_TEXT)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(1.5*cm, 0.38*cm, f"Page {doc.page}")
        canvas.drawCentredString(pw / 2, 0.38*cm, "Confidential — For Academic Review Only")
        canvas.drawRightString(pw - 1.5*cm, 0.38*cm, "2025–2026")
    canvas.restoreState()


# ─────────────────────────────────────────────
# BUILD
# ─────────────────────────────────────────────
def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=1.6*cm, bottomMargin=1.5*cm,
        title="InsightFlow AI — No-Code Predictive Analytics Platform Project Proposal",
        author="Final Year Student",
        subject="Final Year Project Proposal",
    )
    elems = []
    cover_page(elems)
    toc_page(elems)
    build_content(elems)
    doc.build(elems, onFirstPage=add_page_decoration, onLaterPages=add_page_decoration)
    print(f"\n[OK] PDF Generated Successfully!\nSaved at: {OUTPUT_PATH}\n")


if __name__ == "__main__":
    build_pdf()
