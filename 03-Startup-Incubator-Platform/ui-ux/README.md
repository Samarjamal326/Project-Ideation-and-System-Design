# Startup Incubator Platform: UI/UX Specification

This folder documents the typography, color themes, and component structure for the Startup Incubator Platform frontend.

## 1. Style Tokens

We utilize a sleek, clean, modern dark corporate style to convey trustworthiness and security.

```css
:root {
  /* Color Palette */
  --color-primary: #0F172A;        /* Slate Blue (Dark Base) */
  --color-accent: #0284C7;         /* Sky Blue (Interaction highlights) */
  --color-success: #10B981;        /* Teal Green (KPIs Positive) */
  --color-danger: #EF4444;         /* Soft Red (Burn warning / Negative Runway) */
  --color-bg-base: #0F172A;        /* Deep Slate Dark */
  --color-bg-card: #1E293B;        /* Cool Slate Card Gray */
  --color-text-primary: #F8FAFC;   /* Crisp White */
  --color-text-muted: #94A3B8;     /* Muted Steel Gray */
  --color-border: #334155;         /* Muted Slate Border */
}
```

## 2. Typography
- **Headings & Cards:** **Inter** (Bold)
- **Financial Tables:** **JetBrains Mono** (For uniform alignment of numbers and rates)
