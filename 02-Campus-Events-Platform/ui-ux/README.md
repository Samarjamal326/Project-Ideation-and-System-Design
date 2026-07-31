# Campus Events Platform: UI/UX Specification

This folder documents the UI components, style tokens, and layout guidelines for the Campus Events Platform.

## 1. Style Tokens

```css
:root {
  /* Color Palette */
  --color-primary: #8B5CF6;        /* Deep Violet */
  --color-secondary: #EC4899;      /* Pink Rose (Accent) */
  --color-success: #10B981;        /* Teal Green */
  --color-bg-base: #F9FAFB;        /* Light Grey Background */
  --color-bg-card: #FFFFFF;        /* Pure White Surface */
  --color-text-primary: #111827;   /* Charcoal Black */
  --color-text-muted: #6B7280;     /* Slate Grey */
  --color-border: #E5E7EB;         /* Cool light grey */
}

/* Dark Mode Overrides */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-base: #111827;
    --color-bg-card: #1F2937;
    --color-text-primary: #F9FAFB;
    --color-text-muted: #9CA3AF;
    --color-border: #374151;
  }
}
```

## 2. Typography
- **Headings:** **Inter** (SemiBold/Bold)
- **Body Text:** **Inter** (Regular/Medium)

---

## 3. Responsive Screen Layout
- **Mobile View:** Bottom tab bar navigation. Single-column lists of events.
- **Desktop View:** Left sidebar navigation. Multi-column event grids and interactive seating layout panels.
