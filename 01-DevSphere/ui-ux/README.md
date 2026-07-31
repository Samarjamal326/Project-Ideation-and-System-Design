# DevSphere: UI/UX Design System Specification

This directory outlines the UX structure, styling tokens, typography, and responsive design guidelines for the DevSphere frontend web application.

## 1. Design System Tokens

### 1.1. Color Palette (Vanilla CSS / Tailwind-Ready Variables)
We implement a modern "glassmorphism" look over a dark, deep-space background.

```css
:root {
  /* Core Brand Colors */
  --color-bg-base: #0B0F19;        /* Deep Space Blue/Black */
  --color-bg-surface: #151D30;     /* Surface Card Dark */
  --color-primary: #3B82F6;        /* Cobalt Blue */
  --color-secondary: #8B5CF6;      /* Electric Violet */
  --color-accent: #10B981;         /* Emerald Green (Success/AI) */
  --color-text-primary: #F3F4F6;   /* Ice White */
  --color-text-muted: #9CA3AF;     /* Cool Grey */
  --color-border: #24324F;         /* Subtle Steel */
  
  /* Glassmorphism overlays */
  --glass-bg: rgba(21, 29, 48, 0.6);
  --glass-blur: blur(12px);
}
```

### 1.2. Typography
* **Primary Font:** **Outfit** (Google Fonts) – clean geometric font for headings.
* **Secondary Font:** **Inter** (Google Fonts) – clean, highly readable font for interface cards, labels, and text contents.
* **Monospace Font:** **JetBrains Mono** – for code displays and collaborative editors.

---

## 2. Screen Grid & Responsive Layouts
- **Breakpoints:**
  - Mobile: `sm: 640px` (single column cards, mobile slide-out navigation menu).
  - Tablet: `md: 768px` (double column lists, split screen workspace panel).
  - Desktop: `lg: 1024px`, `xl: 1280px` (full dashboard views, persistent left drawer).

## 3. UI/UX Page Flow
```
[Landing Page] 
    └── [OAuth Gateway] 
            └── [Dashboard Layout]
                    ├── [Candidate Search Grid] 
                    ├── [Developer Portfolio]
                    └── [Multiplayer WS Code-Room]
```
