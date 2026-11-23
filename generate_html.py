#!/usr/bin/env python3
"""
generate_html.py
Builds the standalone, anti-slop, ASD-STE100 compliant single-page case study.
Applies:
  - Theme switching: Full Dark and Light mode support with local storage persistence and system preference fallback.
  - tasteskill 2.5: Zero AI-slop gradients (no violet/lavender), quiet micro-interactions, equal edges,
    verb-object button labels, plain factual copy.
  - UI/UX Pro Max: Column sorting (asc/desc), sticky table header, Escape key modal handling,
    high information density, clean focus rings, smooth touch scrolling.
  - ASD-STE100: Simplified Technical English (short, active, unambiguous sentences under 25 words).
  - Batching controls: Shows 8-10 rows by default with dropdown (8, 10, 20, 50, All) and expander arrow.
  - Top counter badge: 'Showing X of 100' placed directly inside the top filter panel.
Output: index.html
"""

import json

def generate_html():
    with open("data/apps_100.json", "r", encoding="utf-8") as f:
        apps = json.load(f)

    with open("data/patterns_summary.json", "r", encoding="utf-8") as f:
        patterns = json.load(f)

    with open("data/verification_audit.json", "r", encoding="utf-8") as f:
        audit = json.load(f)

    apps_json_str = json.dumps(apps).replace("</script>", "<\\/script>")
    patterns_json_str = json.dumps(patterns).replace("</script>", "<\\/script>")
    audit_json_str = json.dumps(audit).replace("</script>", "<\\/script>")

    html = f"""<!DOCTYPE html>
<html lang="en" data-type="software" data-radius="sharp" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio Product Ops: 100 Application Toolkits Technical Audit</title>
  <meta name="description" content="Technical research report and verification audit for 100 software applications. Analyzes authentication methods, access limits, API surfaces, and Model Context Protocol support.">
  <meta name="page-type" content="software">
  <meta name="site-kind" content="software">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* Dark Theme (Default) */
    :root, html[data-theme="dark"] {{
      --bg-page: #0b0d11;
      --bg-surface: #12151c;
      --bg-surface-active: #181c25;
      --bg-subtle: #1c222e;
      --border-base: #232936;
      --border-strong: #323b4d;
      --text-main: #f1f3f7;
      --text-muted: #8b96a8;
      --text-dim: #5a6475;
      
      --accent-brand: #e25822; /* Composio Industrial Flame */
      --accent-blue: #2563eb;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #e11d48;
      
      --table-th-bg: #0f1218;
      --code-bg: #07090c;
    }}

    /* Light Theme (High Contrast, Clean Engineering Palette) */
    html[data-theme="light"] {{
      --bg-page: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-active: #f1f5f9;
      --bg-subtle: #f1f5f9;
      --border-base: #e2e8f0;
      --border-strong: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #64748b;
      
      --accent-brand: #c2410c; /* Deepened flame for light contrast */
      --accent-blue: #1d4ed8;
      --accent-emerald: #047857;
      --accent-amber: #b45309;
      --accent-rose: #be123c;
      
      --table-th-bg: #f1f5f9;
      --code-bg: #0f172a; /* Keep terminal high-contrast slate */
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.5;
      font-size: 14px;
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Global Layout Bounds */
    .wrap {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}

    /* Header Nav: Quiet, Factual */
    header.top-nav {{
      border-bottom: 1px solid var(--border-base);
      background: var(--bg-page);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(8px);
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .nav-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      height: 56px;
      gap: 1rem;
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--text-main);
      font-weight: 700;
      font-size: 0.95rem;
      letter-spacing: -0.01em;
    }}

    .brand-mark {{
      width: 22px;
      height: 22px;
      background: var(--accent-brand);
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      color: #fff;
      font-size: 13px;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
      list-style: none;
    }}

    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.825rem;
      font-weight: 500;
      transition: color 0.1s;
    }}

    .nav-links a:hover {{
      color: var(--text-main);
    }}

    /* Verb-Object Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      text-decoration: none;
      transition: background 0.12s, border-color 0.12s, transform 0.08s;
      user-select: none;
    }}

    .btn:active {{
      transform: translateY(1px);
    }}

    .btn-primary {{
      background: var(--text-main);
      color: var(--bg-page);
    }}

    .btn-primary:hover {{
      opacity: 0.92;
    }}

    .btn-secondary {{
      background: var(--bg-surface);
      border-color: var(--border-base);
      color: var(--text-muted);
    }}

    .btn-secondary:hover {{
      background: var(--bg-surface-active);
      color: var(--text-main);
      border-color: var(--border-strong);
    }}

    /* Theme Toggle Button */
    .theme-toggle-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      color: var(--text-muted);
      padding: 0.45rem 0.75rem;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s ease;
    }}

    .theme-toggle-btn:hover {{
      color: var(--text-main);
      border-color: var(--border-strong);
      background: var(--bg-surface-active);
    }}

    /* Main Container */
    main {{
      padding: 2.5rem 0 6rem;
    }}

    /* Section Structure */
    section.block {{
      margin-bottom: 3.5rem;
    }}

    .section-title {{
      font-size: 1.25rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      margin-bottom: 0.25rem;
    }}

    .section-desc {{
      font-size: 0.875rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      max-width: 820px;
    }}

    /* Hero / Summary Block */
    .hero-panel {{
      border: 1px solid var(--border-base);
      background: var(--bg-surface);
      border-radius: 6px;
      padding: 2rem;
      margin-bottom: 2rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .eyebrow {{
      font-family: var(--font-mono);
      font-size: 0.725rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-brand);
      font-weight: 600;
      margin-bottom: 0.75rem;
      display: block;
    }}

    h1.hero-heading {{
      font-size: 2rem;
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: -0.03em;
      color: var(--text-main);
      margin-bottom: 1rem;
      max-width: 900px;
    }}

    p.hero-text {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 840px;
    }}

    /* Stats Ribbon */
    .stats-row {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1px;
      background: var(--border-base);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      overflow: hidden;
      margin-bottom: 2.5rem;
      transition: border-color 0.2s ease;
    }}

    @media (max-width: 960px) {{
      .stats-row {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    .stat-box {{
      background: var(--bg-surface);
      padding: 1.2rem 1.25rem;
      transition: background-color 0.2s ease;
    }}

    .stat-number {{
      font-size: 1.85rem;
      font-weight: 700;
      letter-spacing: -0.03em;
      color: var(--text-main);
      line-height: 1;
      margin-bottom: 0.4rem;
      font-family: var(--font-mono);
    }}

    .stat-title {{
      font-size: 0.775rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 0.2rem;
    }}

    .stat-sub {{
      font-size: 0.75rem;
      color: var(--text-dim);
      line-height: 1.35;
    }}

    /* Patterns Grid */
    .findings-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }}

    .finding-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: border-color 0.15s, background-color 0.2s ease;
    }}

    .finding-card:hover {{
      border-color: var(--border-strong);
    }}

    .finding-tag {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      color: var(--text-muted);
      background: var(--bg-subtle);
      border: 1px solid var(--border-base);
      padding: 0.15rem 0.45rem;
      border-radius: 3px;
      margin-bottom: 0.65rem;
    }}

    .finding-card h3 {{
      font-size: 0.95rem;
      font-weight: 600;
      margin-bottom: 0.4rem;
      color: var(--text-main);
    }}

    .finding-card p {{
      font-size: 0.825rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Charts Row */
    .charts-pair {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    @media (max-width: 840px) {{
      .charts-pair {{
        grid-template-columns: 1fr;
      }}
    }}

    .chart-panel {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .chart-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-base);
    }}

    .chart-header h4 {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-main);
    }}

    .chart-header span {{
      font-size: 0.75rem;
      color: var(--text-dim);
      font-family: var(--font-mono);
    }}

    .chart-row {{
      display: flex;
      align-items: center;
      margin-bottom: 0.65rem;
      font-size: 0.8rem;
    }}

    .chart-row-label {{
      width: 150px;
      color: var(--text-muted);
      font-size: 0.775rem;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .chart-track {{
      flex: 1;
      height: 14px;
      background: var(--bg-subtle);
      border-radius: 2px;
      overflow: hidden;
      margin: 0 0.75rem;
    }}

    .chart-fill {{
      height: 100%;
      background: var(--accent-brand);
      border-radius: 2px;
    }}

    .chart-row-val {{
      width: 40px;
      text-align: right;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--text-main);
    }}

    /* Quadrant / Table of Wins vs Outreach */
    .matrix-pair {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    @media (max-width: 840px) {{
      .matrix-pair {{
        grid-template-columns: 1fr;
      }}
    }}

    .matrix-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .matrix-card.win {{
      border-left: 3px solid var(--accent-emerald);
    }}

    .matrix-card.outreach {{
      border-left: 3px solid var(--accent-rose);
    }}

    .matrix-card h4 {{
      font-size: 0.875rem;
      font-weight: 600;
      margin-bottom: 0.25rem;
      color: var(--text-main);
    }}

    .matrix-card p.lead {{
      font-size: 0.775rem;
      color: var(--text-dim);
      margin-bottom: 0.85rem;
    }}

    .matrix-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}

    .matrix-item {{
      background: var(--bg-subtle);
      padding: 0.5rem 0.75rem;
      border-radius: 4px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.775rem;
      transition: background-color 0.2s ease;
    }}

    .matrix-item .app-name {{
      font-weight: 600;
      color: var(--text-main);
    }}

    .matrix-item .app-detail {{
      color: var(--text-muted);
      font-size: 0.725rem;
      text-align: right;
    }}

    /* Interactive Table Controls */
    .controls-panel {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px 6px 0 0;
      padding: 1rem 1.25rem;
      border-bottom: none;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .controls-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .search-box {{
      flex: 1;
      min-width: 260px;
      max-width: 440px;
      position: relative;
    }}

    .search-box input {{
      width: 100%;
      background: var(--bg-subtle);
      border: 1px solid var(--border-base);
      border-radius: 4px;
      padding: 0.45rem 0.75rem 0.45rem 2rem;
      font-size: 0.8rem;
      color: var(--text-main);
      outline: none;
      font-family: inherit;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }}

    .search-box input:focus {{
      border-color: var(--accent-brand);
    }}

    .search-icon {{
      position: absolute;
      left: 0.65rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 12px;
      pointer-events: none;
    }}

    /* Top Counter Badge */
    .top-count-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-mono);
      font-size: 0.775rem;
      color: var(--text-main);
      background: var(--bg-subtle);
      padding: 0.4rem 0.75rem;
      border-radius: 4px;
      border: 1px solid var(--border-base);
      white-space: nowrap;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .controls-batching {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}

    .batch-select {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border: 1px solid var(--border-base);
      border-radius: 4px;
      padding: 0.35rem 0.6rem;
      font-size: 0.775rem;
      outline: none;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }}

    .batch-select:focus {{
      border-color: var(--accent-brand);
    }}

    .filter-pills-wrap {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      flex-wrap: wrap;
    }}

    .pill-label {{
      font-size: 0.725rem;
      color: var(--text-dim);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 0.25rem;
    }}

    .pill {{
      background: transparent;
      border: 1px solid var(--border-base);
      color: var(--text-muted);
      padding: 0.25rem 0.55rem;
      border-radius: 3px;
      font-size: 0.75rem;
      cursor: pointer;
      user-select: none;
      transition: all 0.1s;
    }}

    .pill:hover {{
      color: var(--text-main);
      border-color: var(--border-strong);
    }}

    .pill.active {{
      background: var(--bg-subtle);
      color: var(--text-main);
      border-color: var(--accent-brand);
      font-weight: 600;
    }}

    /* Table Component: Sticky Header & Sortable Columns */
    .table-frame {{
      border: 1px solid var(--border-base);
      background: var(--bg-surface);
      overflow-x: auto;
      max-height: 720px;
      -webkit-overflow-scrolling: touch;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
      text-align: left;
    }}

    table.data-table th {{
      position: sticky;
      top: 0;
      z-index: 10;
      background: var(--table-th-bg);
      padding: 0.65rem 0.85rem;
      font-size: 0.725rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-base);
      font-weight: 600;
      white-space: nowrap;
      cursor: pointer;
      user-select: none;
      transition: background-color 0.2s ease, color 0.1s ease;
    }}

    table.data-table th:hover {{
      color: var(--text-main);
    }}

    table.data-table th .sort-indicator {{
      margin-left: 0.25rem;
      font-size: 0.7rem;
      color: var(--text-dim);
    }}

    table.data-table td {{
      padding: 0.75rem 0.85rem;
      border-bottom: 1px solid var(--border-base);
      vertical-align: middle;
      transition: border-color 0.2s ease;
    }}

    table.data-table tbody tr {{
      transition: background 0.1s;
      cursor: pointer;
    }}

    table.data-table tbody tr:hover {{
      background: var(--bg-surface-active);
    }}

    table.data-table tbody tr:last-child td {{
      border-bottom: none;
    }}

    /* Status Badges */
    .tag {{
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 0.15rem 0.4rem;
      border-radius: 3px;
      white-space: nowrap;
    }}

    .tag-ready {{
      background: rgba(5, 150, 105, 0.15);
      color: var(--accent-emerald);
      border: 1px solid rgba(5, 150, 105, 0.35);
    }}

    .tag-partial {{
      background: rgba(217, 119, 6, 0.15);
      color: var(--accent-amber);
      border: 1px solid rgba(217, 119, 6, 0.35);
    }}

    .tag-friction {{
      background: rgba(225, 29, 72, 0.15);
      color: var(--accent-rose);
      border: 1px solid rgba(225, 29, 72, 0.35);
    }}

    .tag-blocked {{
      background: rgba(90, 100, 117, 0.2);
      color: var(--text-dim);
      border: 1px solid rgba(90, 100, 117, 0.4);
    }}

    .tag-selfserve {{
      background: rgba(37, 99, 235, 0.12);
      color: var(--accent-blue);
      border: 1px solid rgba(37, 99, 235, 0.3);
    }}

    .tag-gated {{
      background: rgba(225, 29, 72, 0.12);
      color: var(--accent-rose);
      border: 1px solid rgba(225, 29, 72, 0.3);
    }}

    .tag-paid {{
      background: rgba(217, 119, 6, 0.12);
      color: var(--accent-amber);
      border: 1px solid rgba(217, 119, 6, 0.3);
    }}

    .tag-mcp {{
      background: rgba(226, 88, 34, 0.15);
      color: var(--accent-brand);
      border: 1px solid rgba(226, 88, 34, 0.35);
    }}

    /* Batch Navigation Toolbar */
    .batch-toolbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.85rem 1.25rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-top: none;
      border-radius: 0 0 6px 6px;
      flex-wrap: wrap;
      gap: 0.75rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .expand-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-subtle);
      border: 1px solid var(--border-base);
      color: var(--text-main);
      padding: 0.4rem 0.85rem;
      border-radius: 4px;
      font-size: 0.775rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.15s, border-color 0.15s;
    }}

    .expand-btn:hover {{
      background: var(--bg-surface-active);
      border-color: var(--border-strong);
    }}

    .pagination-controls {{
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}

    .page-btn {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-base);
      color: var(--text-muted);
      padding: 0.3rem 0.6rem;
      border-radius: 3px;
      font-size: 0.75rem;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.12s;
    }}

    .page-btn:hover:not(:disabled) {{
      color: var(--text-main);
      border-color: var(--border-strong);
    }}

    .page-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    /* Verification Progression */
    .audit-strip {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      margin-bottom: 2rem;
    }}

    @media (max-width: 768px) {{
      .audit-strip {{
        grid-template-columns: 1fr;
      }}
    }}

    .audit-step {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .audit-step.final {{
      border-color: var(--accent-emerald);
      background: rgba(5, 150, 105, 0.04);
    }}

    .audit-step-header {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 0.5rem;
    }}

    .audit-step-title {{
      font-size: 0.825rem;
      font-weight: 600;
      color: var(--text-main);
    }}

    .audit-step-pct {{
      font-family: var(--font-mono);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .audit-step-desc {{
      font-size: 0.775rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Hit & Miss Cases */
    .cases-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    .case-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .case-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.65rem;
      padding-bottom: 0.4rem;
      border-bottom: 1px solid var(--border-base);
    }}

    .case-name {{
      font-weight: 700;
      color: var(--text-main);
      font-size: 0.9rem;
    }}

    .case-claim {{
      background: rgba(225, 29, 72, 0.08);
      border: 1px solid rgba(225, 29, 72, 0.25);
      border-radius: 4px;
      padding: 0.5rem 0.65rem;
      font-size: 0.775rem;
      color: var(--accent-rose);
      margin-bottom: 0.5rem;
    }}

    .case-truth {{
      background: rgba(5, 150, 105, 0.08);
      border: 1px solid rgba(5, 150, 105, 0.25);
      border-radius: 4px;
      padding: 0.5rem 0.65rem;
      font-size: 0.775rem;
      color: var(--accent-emerald);
      margin-bottom: 0.5rem;
    }}

    .case-lesson {{
      font-size: 0.725rem;
      color: var(--text-dim);
      line-height: 1.4;
    }}

    /* Agent vs Human Division */
    .pipeline-division {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    @media (max-width: 768px) {{
      .pipeline-division {{
        grid-template-columns: 1fr;
      }}
    }}

    .division-col {{
      background: var(--bg-surface);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .division-col h4 {{
      font-size: 0.85rem;
      font-weight: 600;
      margin-bottom: 0.75rem;
      color: var(--text-main);
    }}

    .division-col ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }}

    .division-col ul li {{
      position: relative;
      padding-left: 1rem;
      font-size: 0.775rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .division-col ul li::before {{
      content: '–';
      position: absolute;
      left: 0;
      color: var(--text-dim);
    }}

    /* Code Terminal Box */
    .code-panel {{
      background: var(--code-bg);
      border: 1px solid var(--border-base);
      border-radius: 6px;
      padding: 1.25rem;
      font-family: var(--font-mono);
      font-size: 0.775rem;
      color: #e2e8f0;
      overflow-x: auto;
      line-height: 1.6;
    }}

    .code-comment {{
      color: #64748b;
    }}

    .code-command {{
      color: #38bdf8;
      font-weight: 600;
    }}

    /* Modal Inspection */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      backdrop-filter: blur(4px);
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-dialog {{
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: 6px;
      width: 100%;
      max-width: 680px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.75rem;
      position: relative;
      box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4);
      transition: background-color 0.2s ease, border-color 0.2s ease;
    }}

    .modal-close-btn {{
      position: absolute;
      top: 1rem;
      right: 1rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.25rem;
      cursor: pointer;
      line-height: 1;
    }}

    .modal-close-btn:hover {{
      color: var(--text-main);
    }}

    .modal-grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1rem 0;
    }}

    .field-label {{
      font-size: 0.7rem;
      font-family: var(--font-mono);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      margin-bottom: 0.2rem;
    }}

    .field-value {{
      font-size: 0.85rem;
      color: var(--text-main);
    }}

    /* Footer */
    footer.page-footer {{
      border-top: 1px solid var(--border-base);
      padding: 2.5rem 0;
      color: var(--text-dim);
      font-size: 0.775rem;
    }}

    .footer-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }}
  </style>
</head>
<body>

  <!-- Top Navigation -->
  <header class="top-nav">
    <div class="wrap nav-inner">
      <a href="#" class="nav-brand">
        <div class="brand-mark">C</div>
        <span>Composio Product Ops</span>
      </a>
      <ul class="nav-links">
        <li><a href="#summary">Findings</a></li>
        <li><a href="#patterns">Rules</a></li>
        <li><a href="#matrix">100 Apps</a></li>
        <li><a href="#pipeline">Agent Architecture</a></li>
        <li><a href="#verification">Verification</a></li>
        <li><a href="#cli">Run Agent</a></li>
      </ul>
      <div style="display: flex; align-items: center; gap: 0.5rem;">
        <!-- Dark / Light Theme Toggle Button -->
        <button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()" aria-label="Toggle dark and light color theme">
          <span id="themeIcon">&#9728;</span>
          <span id="themeLabel">Light</span>
        </button>
        <button class="btn btn-secondary" onclick="exportData('csv')">Download CSV</button>
        <button class="btn btn-secondary" onclick="exportData('json')">Download JSON</button>
      </div>
    </div>
  </header>

  <main class="wrap">

    <!-- Hero / Summary Panel -->
    <section id="summary" class="block">
      <div class="hero-panel">
        <span class="eyebrow">Technical Audit &bull; 100 Applications</span>
        <h1 class="hero-heading">100 App Toolkits: Auth Methods, Gating, and MCP Readiness</h1>
        <p class="hero-text">
          An automated research agent analyzed 100 applications across 10 categories. 
          The agent verified authentication types, developer access gates, API structures, and Model Context Protocol support. 
          This report presents the findings, pattern rules, and verification results.
        </p>
      </div>

      <!-- Top Factual Metrics -->
      <div class="stats-row">
        <div class="stat-box">
          <div class="stat-number">100</div>
          <div class="stat-title">Applications</div>
          <div class="stat-sub">10 enterprise categories</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">73%</div>
          <div class="stat-title">Self-Serve</div>
          <div class="stat-sub">Instant developer keys</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">82%</div>
          <div class="stat-title">Ready Today</div>
          <div class="stat-sub">Documented write APIs</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">26%</div>
          <div class="stat-title">Native MCP</div>
          <div class="stat-sub">Official server available</div>
        </div>
        <div class="stat-box">
          <div class="stat-number" style="color: var(--accent-emerald);">+17%</div>
          <div class="stat-title">Verification Gain</div>
          <div class="stat-sub">70% Pass 1 to 87% Pass 2</div>
        </div>
      </div>
    </section>

    <!-- Macro Patterns / Rules -->
    <section id="patterns" class="block">
      <h2 class="section-title">Macro Patterns and Technical Rules</h2>
      <p class="section-desc">Six factual rules derived from clustering the 100 applications.</p>

      <div class="findings-grid">
        <div class="finding-card">
          <span class="finding-tag">Rule 1: Authentication</span>
          <h3>Bearer Tokens Dominate Infrastructure; OAuth2 Dominates Collaboration</h3>
          <p>
            59 tools use static API keys or Bearer tokens. These permit automated agent calls without user redirection. 
            33 tools require OAuth2. These are collaborative CRMs, Helpdesks, and Ad networks that require tenant scoping.
          </p>
        </div>

        <div class="finding-card">
          <span class="finding-tag">Rule 2: Access Gating</span>
          <h3>73% of Tools Provide Free Self-Serve Keys</h3>
          <p>
            73 applications permit instant registration with immediate API keys. 
            12 applications require a paid subscription. 
            15 applications require a contact-sales meeting or partner agreement.
          </p>
        </div>

        <div class="finding-card">
          <span class="finding-tag">Rule 3: Enterprise Blocks</span>
          <h3>Sales Gates and App Reviews Are the Primary Blockers</h3>
          <p>
            Technical blockers are rarely missing endpoints. 
            PitchBook, DealCloud, and Waterfall.io block access behind 5-figure enterprise contracts. 
            Meta Ads, Google Ads, and LinkedIn Ads require corporate business verification.
          </p>
        </div>

        <div class="finding-card">
          <span class="finding-tag">Rule 4: Protocol Shift</span>
          <h3>26% of Applications Already Support Model Context Protocol</h3>
          <p>
            26 applications support MCP directly. 
            This includes Devin, Consensus, TranscriptAPI, Otter, Firecrawl, Supabase, GitHub, and Sentry. 
            Developers are publishing agent-native protocols alongside standard REST APIs.
          </p>
        </div>

        <div class="finding-card">
          <span class="finding-tag">Rule 5: Local Execution</span>
          <h3>Local CLI Tools Require Container Runtimes</h3>
          <p>
            Sherlock and Mermaid CLI do not expose cloud REST APIs. 
            An agent runtime must support local container execution to run open-source command-line tools.
          </p>
        </div>

        <div class="finding-card">
          <span class="finding-tag">Rule 6: Closed Silos</span>
          <h3>Consumer AI Interfaces Often Lack Public APIs</h3>
          <p>
            Google NotebookLM has no public developer API. 
            Agents cannot call NotebookLM directly. Agents must use Google Cloud Vertex AI to access underlying models.
          </p>
        </div>
      </div>

      <!-- Charts -->
      <div class="charts-pair">
        <div class="chart-panel">
          <div class="chart-header">
            <h4>Primary Authentication Distribution</h4>
            <span>100 Tools</span>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">API Key / Bearer</div>
            <div class="chart-track"><div class="chart-fill" style="width: 59%;"></div></div>
            <div class="chart-row-val">59%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">OAuth2</div>
            <div class="chart-track"><div class="chart-fill" style="width: 33%; background: var(--accent-blue);"></div></div>
            <div class="chart-row-val">33%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">HTTP Basic</div>
            <div class="chart-track"><div class="chart-fill" style="width: 3%; background: var(--accent-amber);"></div></div>
            <div class="chart-row-val">3%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">CLI / Local / No Auth</div>
            <div class="chart-track"><div class="chart-fill" style="width: 3%; background: var(--accent-emerald);"></div></div>
            <div class="chart-row-val">3%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">Custom / HMAC</div>
            <div class="chart-track"><div class="chart-fill" style="width: 2%; background: var(--accent-rose);"></div></div>
            <div class="chart-row-val">2%</div>
          </div>
        </div>

        <div class="chart-panel">
          <div class="chart-header">
            <h4>Access Model Distribution</h4>
            <span>Gating Types</span>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">Self-Serve (Free / Trial)</div>
            <div class="chart-track"><div class="chart-fill" style="width: 73%; background: var(--accent-emerald);"></div></div>
            <div class="chart-row-val">73%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">Partner / Sales Gate</div>
            <div class="chart-track"><div class="chart-fill" style="width: 15%; background: var(--accent-rose);"></div></div>
            <div class="chart-row-val">15%</div>
          </div>
          <div class="chart-row">
            <div class="chart-row-label">Paid Plan Gate</div>
            <div class="chart-track"><div class="chart-fill" style="width: 12%; background: var(--accent-amber);"></div></div>
            <div class="chart-row-val">12%</div>
          </div>
          <div class="chart-row" style="margin-top: 1rem; padding-top: 0.5rem; border-top: 1px dashed var(--border-base);">
            <div class="chart-row-label" style="font-weight: 600; color: var(--text-main);">Agent Buildability</div>
            <div class="chart-track"><div class="chart-fill" style="width: 82%;"></div></div>
            <div class="chart-row-val">82% Ready</div>
          </div>
        </div>
      </div>

      <!-- Easy Wins vs Outreach -->
      <div class="matrix-pair">
        <div class="matrix-card win">
          <h4>Easy Wins (Build Immediately)</h4>
          <p class="lead">Instant tokens, published schemas, zero sales contact.</p>
          <ul class="matrix-list">
            <li class="matrix-item">
              <span class="app-name">GitHub</span>
              <span class="app-detail">Universal PAT &bull; Official MCP</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Firecrawl</span>
              <span class="app-detail">Free tier &bull; LLM markdown &bull; Official MCP</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Supabase</span>
              <span class="app-detail">Instant Postgres &bull; PostgREST &bull; Official MCP</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Notion</span>
              <span class="app-detail">Instant integration secret &bull; Official MCP</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Stripe</span>
              <span class="app-detail">Instant sandbox keys &bull; Official Agent Toolkit</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Consensus</span>
              <span class="app-detail">Instant API key &bull; Official MCP with OAuth PKCE</span>
            </li>
          </ul>
        </div>

        <div class="matrix-card outreach">
          <h4>Outreach Required (Enterprise Gated)</h4>
          <p class="lead">Requires sales calls, business verification, or enterprise contracts.</p>
          <ul class="matrix-list">
            <li class="matrix-item">
              <span class="app-name">PitchBook</span>
              <span class="app-detail">$20,000+/year contract &bull; No public trial</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">DealCloud</span>
              <span class="app-detail">Intapp client agreement &bull; Dedicated tenant</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Meta Ads</span>
              <span class="app-detail">App Review &bull; Legal entity verification</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Salesforce Commerce</span>
              <span class="app-detail">Account Manager contract &bull; SCAPI</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">Waterfall.io</span>
              <span class="app-detail">B2B vendor agreement &bull; Sales demo</span>
            </li>
            <li class="matrix-item">
              <span class="app-name">NotebookLM</span>
              <span class="app-detail">UI-only product &bull; Use Google Vertex AI</span>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Section: 100 App Findings Matrix -->
    <section id="matrix" class="block">
      <h2 class="section-title">100 Application Findings Matrix</h2>
      <p class="section-desc">Search, filter, and inspect technical specifications for all 100 applications. Click any column header to sort.</p>

      <!-- Filter Controls Panel -->
      <div class="controls-panel">
        <div class="controls-top">
          <!-- Search input -->
          <div class="search-box">
            <span class="search-icon">&#128269;</span>
            <input type="text" id="searchInput" placeholder="Filter by application name, category, auth, or blocker...">
          </div>

          <!-- Counter Placed Directly Beside Controls -->
          <div class="top-count-badge" id="topCountDisplay">
            Showing 1–10 of 100 applications
          </div>

          <!-- Batching Dropdown Selector -->
          <div class="controls-batching">
            <span>Show:</span>
            <select id="batchSelect" class="batch-select" onchange="handleBatchSizeChange(this.value)">
              <option value="8">8 rows</option>
              <option value="10" selected>10 rows</option>
              <option value="20">20 rows</option>
              <option value="50">50 rows</option>
              <option value="100">All 100 rows</option>
            </select>
          </div>
        </div>

        <!-- Filter Pills -->
        <div class="filter-pills-wrap">
          <span class="pill-label">Category:</span>
          <button class="pill active" onclick="setCategory('all', this)">All (100)</button>
          <button class="pill" onclick="setCategory('CRM and Sales', this)">CRM</button>
          <button class="pill" onclick="setCategory('Support and Helpdesk', this)">Helpdesk</button>
          <button class="pill" onclick="setCategory('Communications and Messaging', this)">Messaging</button>
          <button class="pill" onclick="setCategory('Marketing, Ads, Email and Social', this)">Marketing</button>
          <button class="pill" onclick="setCategory('Ecommerce', this)">Ecommerce</button>
          <button class="pill" onclick="setCategory('Data, SEO and Scraping', this)">Data / SEO</button>
          <button class="pill" onclick="setCategory('Developer, Infra and Data platforms', this)">Dev Infra</button>
          <button class="pill" onclick="setCategory('Productivity and Project Management', this)">Productivity</button>
          <button class="pill" onclick="setCategory('Finance and Fintech', this)">Fintech</button>
          <button class="pill" onclick="setCategory('AI, Research and Media-native', this)">AI / Media</button>
        </div>

        <div class="filter-pills-wrap" style="padding-top: 0.5rem; border-top: 1px solid var(--border-base);">
          <span class="pill-label">Access:</span>
          <button class="pill active" onclick="setAccess('all', this)">All</button>
          <button class="pill" onclick="setAccess('Self-Serve', this)">Self-Serve</button>
          <button class="pill" onclick="setAccess('Paid Gated', this)">Paid Gated</button>
          <button class="pill" onclick="setAccess('Partner Gated', this)">Partner Gated</button>

          <span class="pill-label" style="margin-left: 0.75rem;">Buildability:</span>
          <button class="pill active" onclick="setBuild('all', this)">All</button>
          <button class="pill" onclick="setBuild('Ready', this)">Ready</button>
          <button class="pill" onclick="setBuild('Partial', this)">Partial</button>
          <button class="pill" onclick="setBuild('High Friction', this)">High Friction</button>
          <button class="pill" onclick="setBuild('Blocked', this)">Blocked</button>

          <span class="pill-label" style="margin-left: 0.75rem;">MCP:</span>
          <button class="pill active" onclick="setMcp('all', this)">All</button>
          <button class="pill" onclick="setMcp('Official', this)">Official MCP</button>
          <button class="pill" onclick="setMcp('Composio', this)">Composio Supported</button>
        </div>
      </div>

      <!-- Data Table with Sticky Header & Column Sorting -->
      <div class="table-frame">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 50px;" onclick="handleSort('id')">
                # <span class="sort-indicator" id="sort-id">&#8645;</span>
              </th>
              <th style="width: 160px;" onclick="handleSort('name')">
                Application <span class="sort-indicator" id="sort-name">&#8645;</span>
              </th>
              <th style="width: 290px;">Description</th>
              <th style="width: 140px;" onclick="handleSort('primary_auth')">
                Primary Auth <span class="sort-indicator" id="sort-primary_auth">&#8645;</span>
              </th>
              <th style="width: 110px;" onclick="handleSort('access_model')">
                Access Gate <span class="sort-indicator" id="sort-access_model">&#8645;</span>
              </th>
              <th style="width: 120px;">API Surface</th>
              <th style="width: 100px;" onclick="handleSort('buildability')">
                Buildability <span class="sort-indicator" id="sort-buildability">&#8645;</span>
              </th>
              <th style="width: 140px;" onclick="handleSort('mcp_status')">
                MCP Status <span class="sort-indicator" id="sort-mcp_status">&#8645;</span>
              </th>
              <th style="width: 75px;">Docs</th>
            </tr>
          </thead>
          <tbody id="tableBody">
            <!-- Populated by JavaScript -->
          </tbody>
        </table>
      </div>

      <!-- Batch Toolbar: Expansion Arrow and Pagination -->
      <div class="batch-toolbar">
        <button class="expand-btn" id="expandToggleBtn" onclick="toggleExpandAll()">
          <span id="expandArrow">&#x2193;</span>
          <span id="expandBtnLabel">Show all 100 entries</span>
        </button>

        <div class="pagination-controls" id="paginationControls">
          <button class="page-btn" id="prevPageBtn" onclick="changePage(-1)">&larr; Previous</button>
          <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--text-muted); margin: 0 0.5rem;" id="pageIndicator">Page 1 of 10</span>
          <button class="page-btn" id="nextPageBtn" onclick="changePage(1)">Next &rarr;</button>
        </div>
      </div>
    </section>

    <!-- Section: Research Agent Architecture -->
    <section id="pipeline" class="block">
      <h2 class="section-title">Research Agent Architecture and Human Hand-Off</h2>
      <p class="section-desc">Division of tasks between the autonomous pipeline and human verification.</p>

      <div class="pipeline-division">
        <div class="division-col">
          <h4>Tasks Executed by the Autonomous Agent</h4>
          <ul>
            <li>Parsed developer documentation trees across 100 domains.</li>
            <li>Extracted authentication headers, token formats, and endpoints.</li>
            <li>Ingested OpenAPI and Swagger schemas to calculate API breadth.</li>
            <li>Checked public Model Context Protocol registries and repositories.</li>
            <li>Stored findings in structured JSON and CSV formats.</li>
          </ul>
        </div>

        <div class="division-col">
          <h4>Tasks Executed by Human Verification</h4>
          <ul>
            <li>Identified commercial paywalls on open documentation portals (Ahrefs, SE Ranking).</li>
            <li>Verified that NotebookLM is a UI-only product without a public API.</li>
            <li>Distinguished Salesforce Core CRM from Salesforce Commerce Cloud.</li>
            <li>Classified Sherlock and Mermaid CLI as local command-line tools.</li>
            <li>Located unlisted developer documentation on subdomains (fanbasis).</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Section: Verification Progression & Hit/Miss Audit -->
    <section id="verification" class="block">
      <h2 class="section-title">Verification Loops and Accuracy Progression</h2>
      <p class="section-desc">Measurable accuracy improvement through automated cross-validation and manual review.</p>

      <div class="audit-strip">
        <div class="audit-step">
          <div class="audit-step-header">
            <span class="audit-step-title">Pass 1: Naive Agent</span>
            <span class="audit-step-pct">70.0%</span>
          </div>
          <p class="audit-step-desc">
            Single-pass extraction. Misclassified enterprise portals as self-serve. 
            Assumed local CLI tools were cloud REST services.
          </p>
        </div>

        <div class="audit-step">
          <div class="audit-step-header">
            <span class="audit-step-title">Pass 2: Verification Loop</span>
            <span class="audit-step-pct" style="color: var(--accent-blue);">87.0%</span>
          </div>
          <p class="audit-step-desc">
            Automated cross-check. Verified HTTP status codes, tested OpenAPI endpoints, and checked MCP registries. 
            Yielded a +17.0% accuracy gain.
          </p>
        </div>

        <div class="audit-step final">
          <div class="audit-step-header">
            <span class="audit-step-title">Pass 3: Human Ground Truth</span>
            <span class="audit-step-pct" style="color: var(--accent-emerald);">100.0%</span>
          </div>
          <p class="audit-step-desc">
            Manual inspection of edge cases, payment paywalls, and unlisted subdomains.
          </p>
        </div>
      </div>

      <h3 style="font-size: 0.95rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--text-main);">
        Sample Discrepancies and Corrective Actions
      </h3>

      <div class="cases-grid">
        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">DealCloud (#10)</span>
            <span class="tag tag-friction">High Friction</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> Self-serve REST API with public portal.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> Gated behind Intapp enterprise contracts. No public sandbox exists.</div>
          <div class="case-lesson">Open Swagger portals do not imply open developer access.</div>
        </div>

        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">NotebookLM (#91)</span>
            <span class="tag tag-blocked">Blocked</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> Ready toolkit using Google Gemini API keys.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> NotebookLM has no public developer API. The product is closed UI-only.</div>
          <div class="case-lesson">Do not conflate underlying foundation models with consumer AI interfaces.</div>
        </div>

        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">Otter AI (#92)</span>
            <span class="tag tag-ready">Ready (MCP)</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> High Friction because REST API requires Enterprise plan.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> Otter operates an official MCP server (mcp.otter.ai) for agent querying.</div>
          <div class="case-lesson">Modern SaaS applications bypass REST gating by deploying native MCP servers.</div>
        </div>

        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">Threads (Meta) (#39)</span>
            <span class="tag tag-ready">Ready</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> Blocked; no public API exists.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> Threads launched a public Graph API with OAuth2 in June 2024.</div>
          <div class="case-lesson">Outdated training data must be updated through active web verification.</div>
        </div>

        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">Sherlock (#58)</span>
            <span class="tag tag-ready">Ready (CLI)</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> Cloud REST API with API token authentication.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> Open-source Python CLI utility. Runs locally without authentication.</div>
          <div class="case-lesson">CLI tools must run in local container environments rather than HTTP endpoints.</div>
        </div>

        <div class="case-item">
          <div class="case-title-row">
            <span class="case-name">fanbasis (#50)</span>
            <span class="tag tag-ready">Ready</span>
          </div>
          <div class="case-claim"><strong>Pass 1 Claim:</strong> Blocked; closed creator platform with no developer surface.</div>
          <div class="case-truth"><strong>Ground Truth:</strong> Provides checkout SDK on npm and documentation at dev-docs.fanbasis.com.</div>
          <div class="case-lesson">Rebranded software platforms often host developer portals on dedicated subdomains.</div>
        </div>
      </div>
    </section>

    <!-- Section: Runnable Agent CLI -->
    <section id="cli" class="block">
      <h2 class="section-title">Command Line Interface Commands</h2>
      <p class="section-desc">Commands to execute the agent, run the verification benchmark, and export data.</p>

      <div class="code-panel">
        <span class="code-comment"># 1. Profile specific applications</span><br>
        <span class="code-command">python3 agent/research_pipeline.py --app-id 10</span><br>
        <span class="code-command">python3 agent/research_pipeline.py --app-id 91</span><br><br>

        <span class="code-comment"># 2. Filter research pipeline by category</span><br>
        <span class="code-command">python3 agent/research_pipeline.py --category Fintech</span><br><br>

        <span class="code-comment"># 3. Run the verification benchmark</span><br>
        <span class="code-command">python3 agent/verifier.py</span><br><br>

        <span class="code-comment"># 4. Generate statistical macro patterns</span><br>
        <span class="code-command">python3 agent/analyzer.py</span>
      </div>
    </section>

  </main>

  <!-- Modal Dialog with Escape Key Listener -->
  <div id="detailModal" class="modal-overlay" onclick="closeModal(event)">
    <div class="modal-dialog" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeModal(event)" aria-label="Close dialog">&times;</button>
      <div id="modalContent"></div>
    </div>
  </div>

  <footer class="page-footer wrap">
    <div class="footer-inner">
      <span>Composio AI Product Ops Case Study &bull; Technical Research on 100 Applications</span>
      <span>ASD-STE100 Technical English Format</span>
    </div>
  </footer>

  <script>
    const rawApps = {apps_json_str};
    const patterns = {patterns_json_str};
    const audit = {audit_json_str};

    let currentCategory = 'all';
    let currentAccess = 'all';
    let currentBuild = 'all';
    let currentMcp = 'all';
    let currentSearch = '';

    // Batching & Pagination State
    let batchSize = 10;
    let currentPage = 1;
    let isExpandedAll = false;

    // Sorting State
    let sortColumn = 'id';
    let sortDirection = 'asc';

    // ----------------------------------------------------
    // Theme Switcher (Dark / Light) with Persistence
    // ----------------------------------------------------
    function initTheme() {{
      const savedTheme = localStorage.getItem('composio_theme');
      if (savedTheme) {{
        setTheme(savedTheme);
      }} else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {{
        setTheme('light');
      }} else {{
        setTheme('dark');
      }}
    }}

    function setTheme(theme) {{
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('composio_theme', theme);
      const icon = document.getElementById('themeIcon');
      const label = document.getElementById('themeLabel');
      if (theme === 'light') {{
        icon.innerHTML = '&#9790;'; // Moon symbol
        label.innerText = 'Dark';
      }} else {{
        icon.innerHTML = '&#9728;'; // Sun symbol
        label.innerText = 'Light';
      }}
    }}

    function toggleTheme() {{
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const target = (current === 'dark') ? 'light' : 'dark';
      setTheme(target);
    }}

    // ----------------------------------------------------
    // Data Table Logic
    // ----------------------------------------------------
    function getFilteredApps() {{
      let list = rawApps.filter(app => {{
        if (currentCategory !== 'all' && app.category !== currentCategory) return false;
        if (currentAccess !== 'all' && app.access_model !== currentAccess) return false;
        if (currentBuild !== 'all' && app.buildability !== currentBuild) return false;
        if (currentMcp === 'Official' && !app.mcp_status.includes('Official')) return false;
        if (currentMcp === 'Composio' && !app.mcp_status.includes('Composio')) return false;

        if (currentSearch.trim() !== '') {{
          const q = currentSearch.toLowerCase();
          const match = app.name.toLowerCase().includes(q) ||
                        app.category.toLowerCase().includes(q) ||
                        app.one_liner.toLowerCase().includes(q) ||
                        app.primary_auth.toLowerCase().includes(q) ||
                        app.main_blocker.toLowerCase().includes(q) ||
                        app.api_surface.toLowerCase().includes(q);
          if (!match) return false;
        }}
        return true;
      }});

      // Apply Sort
      list.sort((a, b) => {{
        let valA = a[sortColumn];
        let valB = b[sortColumn];
        if (typeof valA === 'string') {{
          valA = valA.toLowerCase();
          valB = valB.toLowerCase();
        }}
        if (valA < valB) return sortDirection === 'asc' ? -1 : 1;
        if (valA > valB) return sortDirection === 'asc' ? 1 : -1;
        return 0;
      }});

      return list;
    }}

    function handleSort(col) {{
      if (sortColumn === col) {{
        sortDirection = (sortDirection === 'asc') ? 'desc' : 'asc';
      }} else {{
        sortColumn = col;
        sortDirection = 'asc';
      }}
      updateSortIndicators();
      renderTable();
    }}

    function updateSortIndicators() {{
      ['id', 'name', 'primary_auth', 'access_model', 'buildability', 'mcp_status'].forEach(c => {{
        const el = document.getElementById('sort-' + c);
        if (el) {{
          if (c === sortColumn) {{
            el.innerHTML = (sortDirection === 'asc') ? '&#9650;' : '&#9660;';
            el.style.color = 'var(--text-main)';
          }} else {{
            el.innerHTML = '&#8645;';
            el.style.color = 'var(--text-dim)';
          }}
        }}
      }});
    }}

    function renderTable() {{
      const tbody = document.getElementById('tableBody');
      const filtered = getFilteredApps();
      const totalFiltered = filtered.length;

      let displayedApps = [];
      let totalPages = Math.ceil(totalFiltered / batchSize);
      if (totalPages === 0) totalPages = 1;
      if (currentPage > totalPages) currentPage = totalPages;

      if (isExpandedAll || batchSize >= totalFiltered) {{
        displayedApps = filtered;
        document.getElementById('topCountDisplay').innerText = `Showing all ${{totalFiltered}} of ${{rawApps.length}} applications`;
        document.getElementById('paginationControls').style.display = 'none';
        document.getElementById('expandArrow').innerHTML = '&#x2191;';
        document.getElementById('expandBtnLabel').innerText = 'Collapse table';
      }} else {{
        const startIndex = (currentPage - 1) * batchSize;
        const endIndex = Math.min(startIndex + batchSize, totalFiltered);
        displayedApps = filtered.slice(startIndex, endIndex);

        document.getElementById('topCountDisplay').innerText = `Showing ${{startIndex + 1}}–${{endIndex}} of ${{totalFiltered}} applications (Total: ${{rawApps.length}})`;
        document.getElementById('paginationControls').style.display = 'flex';
        document.getElementById('pageIndicator').innerText = `Page ${{currentPage}} of ${{totalPages}}`;
        document.getElementById('prevPageBtn').disabled = (currentPage === 1);
        document.getElementById('nextPageBtn').disabled = (currentPage === totalPages);
        document.getElementById('expandArrow').innerHTML = '&#x2193;';
        document.getElementById('expandBtnLabel').innerText = `Show all ${{totalFiltered}} entries`;
      }}

      if (displayedApps.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; padding: 2.5rem; color: var(--text-dim);">No applications match the selected criteria.</td></tr>`;
        return;
      }}

      tbody.innerHTML = displayedApps.map(app => {{
        let bClass = 'tag-ready';
        if (app.buildability === 'Partial') bClass = 'tag-partial';
        else if (app.buildability === 'High Friction') bClass = 'tag-friction';
        else if (app.buildability === 'Blocked') bClass = 'tag-blocked';

        let aClass = 'tag-selfserve';
        if (app.access_model === 'Paid Gated') aClass = 'tag-paid';
        else if (app.access_model === 'Partner Gated') aClass = 'tag-gated';

        let mClass = 'tag-mcp';
        let mcpLabel = app.mcp_status.split('/')[0].trim();

        return `
          <tr onclick="openModal(${{app.id}})">
            <td style="color: var(--text-dim); font-family: var(--font-mono); font-size: 0.75rem;">${{app.id}}</td>
            <td>
              <div style="font-weight: 600; color: var(--text-main);">${{app.name}}</div>
              <div style="font-size: 0.7rem; color: var(--text-dim);">${{app.category}}</div>
            </td>
            <td style="color: var(--text-muted); font-size: 0.775rem;">${{app.one_liner}}</td>
            <td><span style="font-family: var(--font-mono); font-size: 0.75rem;">${{app.primary_auth}}</span></td>
            <td><span class="tag ${{aClass}}">${{app.access_model}}</span></td>
            <td style="font-size: 0.75rem; color: var(--text-muted); font-family: var(--font-mono);">${{app.api_surface.split(',')[0]}}</td>
            <td><span class="tag ${{bClass}}">${{app.buildability}}</span></td>
            <td><span class="tag ${{mClass}}">${{mcpLabel}}</span></td>
            <td>
              <a href="${{app.docs_url}}" target="_blank" rel="noopener noreferrer" style="color: var(--accent-blue); text-decoration: none; font-size: 0.75rem; font-weight: 500;" onclick="event.stopPropagation()">
                Open &nearr;
              </a>
            </td>
          </tr>
        `;
      }}).join('');
    }}

    function handleBatchSizeChange(newSize) {{
      batchSize = parseInt(newSize, 10);
      currentPage = 1;
      isExpandedAll = (batchSize >= 100);
      renderTable();
    }}

    function toggleExpandAll() {{
      isExpandedAll = !isExpandedAll;
      renderTable();
    }}

    function changePage(delta) {{
      currentPage += delta;
      renderTable();
    }}

    function setCategory(cat, el) {{
      currentCategory = cat;
      currentPage = 1;
      el.parentNode.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      renderTable();
    }}

    function setAccess(acc, el) {{
      currentAccess = acc;
      currentPage = 1;
      el.parentNode.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      renderTable();
    }}

    function setBuild(b, el) {{
      currentBuild = b;
      currentPage = 1;
      el.parentNode.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      renderTable();
    }}

    function setMcp(m, el) {{
      currentMcp = m;
      currentPage = 1;
      el.parentNode.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      el.classList.add('active');
      renderTable();
    }}

    document.getElementById('searchInput').addEventListener('input', (e) => {{
      currentSearch = e.target.value;
      currentPage = 1;
      renderTable();
    }});

    function openModal(id) {{
      const app = rawApps.find(a => a.id === id);
      if (!app) return;

      const content = document.getElementById('modalContent');
      content.innerHTML = `
        <div style="margin-bottom: 1rem; padding-bottom: 0.75rem; border-bottom: 1px solid var(--border-base);">
          <div style="font-family: var(--font-mono); font-size: 0.725rem; color: var(--accent-brand);">APPLICATION #${{app.id}}</div>
          <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--text-main); margin: 0.2rem 0;">${{app.name}}</h3>
          <div style="font-size: 0.8rem; color: var(--text-muted);">${{app.category}} &bull; ${{app.website}}</div>
        </div>

        <p style="font-size: 0.85rem; color: var(--text-main); margin-bottom: 1.25rem; line-height: 1.5;">${{app.one_liner}}</p>

        <div class="modal-grid-2">
          <div>
            <div class="field-label">Primary Authentication</div>
            <div class="field-value font-mono">${{app.primary_auth}}</div>
          </div>
          <div>
            <div class="field-label">Access Model</div>
            <div class="field-value">${{app.access_model}}</div>
          </div>
        </div>

        <div style="margin-bottom: 1rem;">
          <div class="field-label">Access Details</div>
          <div class="field-value">${{app.access_details}}</div>
        </div>

        <div class="modal-grid-2">
          <div>
            <div class="field-label">API Surface & Breadth</div>
            <div class="field-value">${{app.api_surface}} (${{app.api_breadth}})</div>
          </div>
          <div>
            <div class="field-label">MCP Support</div>
            <div class="field-value">${{app.mcp_status}}</div>
          </div>
        </div>

        <div style="margin-bottom: 1rem;">
          <div class="field-label">Buildability & Primary Blocker</div>
          <div class="field-value"><strong>[${{app.buildability}}]</strong> &bull; ${{app.main_blocker}}</div>
        </div>

        <div style="margin-bottom: 1rem; background: var(--bg-subtle); padding: 0.75rem; border-radius: 4px; border: 1px solid var(--border-base);">
          <div class="field-label" style="color: var(--accent-brand);">Composio Integration Strategy</div>
          <div class="field-value">${{app.composio_strategy}}</div>
        </div>

        <div style="margin-bottom: 1.25rem;">
          <div class="field-label">Verification Note</div>
          <div class="field-value" style="font-size: 0.775rem; color: var(--text-muted);">${{app.verification_notes}}</div>
        </div>

        <div style="text-align: right;">
          <a href="${{app.docs_url}}" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            Open Official Documentation &nearr;
          </a>
        </div>
      `;

      document.getElementById('detailModal').classList.add('open');
    }}

    function closeModal(e) {{
      document.getElementById('detailModal').classList.remove('open');
    }}

    // Escape Key Listener for Accessibility (UI/UX Pro Max)
    window.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        closeModal();
      }}
    }});

    function exportData(format) {{
      if (format === 'json') {{
        const blob = new Blob([JSON.stringify(rawApps, null, 2)], {{ type: 'application/json' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'composio_100_apps_dataset.json';
        a.click();
      }} else if (format === 'csv') {{
        const headers = ["id", "name", "category", "one_liner", "primary_auth", "access_model", "buildability", "mcp_status", "docs_url"];
        let csv = headers.join(",") + "\\n";
        rawApps.forEach(a => {{
          const row = [
            a.id,
            `"${{a.name.replace(/"/g, '""')}}"`,
            `"${{a.category.replace(/"/g, '""')}}"`,
            `"${{a.one_liner.replace(/"/g, '""')}}"`,
            `"${{a.primary_auth.replace(/"/g, '""')}}"`,
            `"${{a.access_model.replace(/"/g, '""')}}"`,
            `"${{a.buildability.replace(/"/g, '""')}}"`,
            `"${{a.mcp_status.replace(/"/g, '""')}}"`,
            `"${{a.docs_url.replace(/"/g, '""')}}"`
          ];
          csv += row.join(",") + "\\n";
        }});
        const blob = new Blob([csv], {{ type: 'text/csv' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'composio_100_apps_dataset.csv';
        a.click();
      }}
    }}

    // Initializations
    initTheme();
    updateSortIndicators();
    renderTable();
  </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote index.html with dark and light mode toggle, local persistence, and high contrast styling.")

if __name__ == "__main__":
    generate_html()
