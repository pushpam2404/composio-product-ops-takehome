#!/usr/bin/env python3
"""
generate_html.py
Builds the standalone, production-ready, interactive single-page Case Study & Dashboard.
Embeds all verified data from data/apps_100.json, data/patterns_summary.json, and data/verification_audit.json.
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
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio Product Ops Case Study: 100 App Toolkits & Patterns</title>
  <meta name="description" content="AI Product Ops Take-Home Assignment: Researching 100 Apps for Agent Toolkits, Auth Patterns, Gating Analysis, Verification Loops, and MCP Readiness.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #090d16;
      --bg-card: #0f172a;
      --bg-card-hover: #162038;
      --border-subtle: #1e293b;
      --border-accent: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --composio-orange: #f97316;
      --composio-purple: #8b5cf6;
      --composio-blue: #3b82f6;
      --composio-emerald: #10b981;
      --composio-rose: #f43f5e;
      --composio-amber: #f59e0b;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      line-height: 1.55;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    code, pre, .font-mono {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Header Nav */
    header.sticky-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      background: rgba(9, 13, 22, 0.85);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .nav-container {{
      max-width: 1360px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: white;
    }}

    .brand-logo {{
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, #f97316, #8b5cf6);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      color: white;
      box-shadow: 0 0 16px rgba(249, 115, 22, 0.35);
    }}

    .brand-title {{
      font-weight: 700;
      font-size: 1.05rem;
      letter-spacing: -0.02em;
    }}

    .brand-badge {{
      font-size: 0.7rem;
      background: rgba(249, 115, 22, 0.15);
      color: #fb923c;
      padding: 0.2rem 0.55rem;
      border-radius: 9999px;
      font-weight: 600;
      border: 1px solid rgba(249, 115, 22, 0.3);
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
      font-size: 0.875rem;
      font-weight: 500;
      transition: color 0.15s ease;
    }}

    .nav-links a:hover {{
      color: var(--text-main);
    }}

    .nav-btn {{
      background: linear-gradient(135deg, #f97316, #ea580c);
      color: white;
      padding: 0.45rem 0.95rem;
      border-radius: 7px;
      font-size: 0.825rem;
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: opacity 0.2s;
    }}

    .nav-btn:hover {{
      opacity: 0.9;
    }}

    /* Main Container */
    .page-container {{
      max-width: 1360px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem 6rem;
    }}

    /* Hero Headline */
    .hero {{
      text-align: left;
      margin-bottom: 2.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .hero-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #fb923c;
      background: rgba(251, 146, 60, 0.1);
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
      border: 1px solid rgba(251, 146, 60, 0.25);
    }}

    .hero-title {{
      font-size: 2.5rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 1rem;
      background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
      font-size: 1.125rem;
      color: var(--text-muted);
      max-width: 860px;
      line-height: 1.6;
    }}

    /* Metric Cards Grid */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}

    .metric-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.25rem 1.1rem;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, border-color 0.2s;
    }}

    .metric-card:hover {{
      transform: translateY(-2px);
      border-color: var(--border-accent);
    }}

    .metric-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, #f97316, #8b5cf6);
      opacity: 0.8;
    }}

    .metric-val {{
      font-size: 2.25rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 0.3rem;
      line-height: 1;
      margin-bottom: 0.4rem;
    }}

    .metric-val span.sub {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-dim);
    }}

    .metric-label {{
      font-size: 0.825rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.25rem;
    }}

    .metric-caption {{
      font-size: 0.775rem;
      color: var(--text-dim);
      line-height: 1.35;
    }}

    /* Section Styling */
    .section-wrap {{
      margin-bottom: 4rem;
    }}

    .section-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--border-subtle);
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .section-title-wrap h2 {{
      font-size: 1.6rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .section-title-wrap p {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }}

    /* Patterns Cards */
    .patterns-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2rem;
    }}

    .pattern-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.4rem;
      transition: border-color 0.2s;
    }}

    .pattern-card:hover {{
      border-color: var(--border-accent);
    }}

    .pattern-badge {{
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
      margin-bottom: 0.75rem;
      background: rgba(139, 92, 246, 0.15);
      color: #a78bfa;
      border: 1px solid rgba(139, 92, 246, 0.3);
    }}

    .pattern-card h3 {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--text-main);
    }}

    .pattern-card p {{
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Visual Charts & Category Table */
    .charts-split {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }}

    @media (max-width: 900px) {{
      .charts-split {{
        grid-template-columns: 1fr;
      }}
    }}

    .chart-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.4rem;
    }}

    .chart-box h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .bar-row {{
      display: flex;
      align-items: center;
      margin-bottom: 0.75rem;
      font-size: 0.825rem;
    }}

    .bar-label {{
      width: 140px;
      color: var(--text-muted);
      font-weight: 500;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .bar-track {{
      flex: 1;
      height: 18px;
      background: rgba(30, 41, 59, 0.6);
      border-radius: 6px;
      overflow: hidden;
      position: relative;
      margin: 0 0.75rem;
    }}

    .bar-fill {{
      height: 100%;
      border-radius: 6px;
      transition: width 0.6s ease-out;
    }}

    .bar-val {{
      width: 45px;
      text-align: right;
      font-weight: 600;
      color: var(--text-main);
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
    }}

    /* Matrix Quadrant */
    .quadrant-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-bottom: 2rem;
    }}

    @media (max-width: 800px) {{
      .quadrant-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .quadrant-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.4rem;
    }}

    .quadrant-box.wins {{
      border-left: 4px solid var(--composio-emerald);
    }}

    .quadrant-box.outreach {{
      border-left: 4px solid var(--composio-rose);
    }}

    .quadrant-title {{
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .quadrant-subtitle {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .quadrant-item {{
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.65rem 0.85rem;
      margin-bottom: 0.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.825rem;
    }}

    .quadrant-item .name {{
      font-weight: 700;
      color: var(--text-main);
    }}

    .quadrant-item .note {{
      color: var(--text-dim);
      font-size: 0.775rem;
      text-align: right;
      max-width: 60%;
    }}

    /* Interactive Table Controls */
    .table-controls {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .search-row {{
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .search-input-wrap {{
      flex: 1;
      min-width: 260px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-main);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.65rem 1rem 0.65rem 2.4rem;
      font-size: 0.875rem;
      color: var(--text-main);
      outline: none;
      transition: border-color 0.2s;
    }}

    .search-input:focus {{
      border-color: var(--composio-orange);
    }}

    .search-icon {{
      position: absolute;
      left: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      pointer-events: none;
    }}

    .filters-row {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      align-items: center;
    }}

    .filter-label {{
      font-size: 0.775rem;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-right: 0.25rem;
    }}

    .filter-pill {{
      background: var(--bg-main);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 0.35rem 0.7rem;
      border-radius: 7px;
      font-size: 0.775rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      user-select: none;
    }}

    .filter-pill:hover {{
      color: var(--text-main);
      border-color: var(--border-accent);
    }}

    .filter-pill.active {{
      background: rgba(249, 115, 22, 0.15);
      color: #fb923c;
      border-color: rgba(249, 115, 22, 0.4);
    }}

    .export-btns {{
      display: flex;
      gap: 0.5rem;
      margin-left: auto;
    }}

    .btn-secondary {{
      background: var(--bg-main);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 0.4rem 0.75rem;
      border-radius: 7px;
      font-size: 0.775rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.15s;
    }}

    .btn-secondary:hover {{
      color: var(--text-main);
      border-color: var(--border-accent);
    }}

    /* Table Styling */
    .table-container {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      overflow-x: auto;
      margin-bottom: 2rem;
    }}

    table.matrix-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.85rem;
    }}

    table.matrix-table th {{
      background: rgba(15, 23, 42, 0.9);
      padding: 0.85rem 1rem;
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--border-subtle);
      white-space: nowrap;
      user-select: none;
    }}

    table.matrix-table td {{
      padding: 0.9rem 1rem;
      border-bottom: 1px solid rgba(30, 41, 59, 0.5);
      vertical-align: middle;
    }}

    table.matrix-table tbody tr {{
      transition: background 0.15s;
      cursor: pointer;
    }}

    table.matrix-table tbody tr:hover {{
      background: var(--bg-card-hover);
    }}

    /* Badges */
    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 0.2rem 0.55rem;
      border-radius: 6px;
      font-size: 0.725rem;
      font-weight: 600;
      white-space: nowrap;
      line-height: 1.2;
    }}

    .badge-ready {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .badge-partial {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}

    .badge-friction {{
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }}

    .badge-blocked {{
      background: rgba(148, 163, 184, 0.15);
      color: #94a3b8;
      border: 1px solid rgba(148, 163, 184, 0.3);
    }}

    .badge-selfserve {{
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border: 1px solid rgba(59, 130, 246, 0.3);
    }}

    .badge-paidgated {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}

    .badge-partnergated {{
      background: rgba(244, 63, 94, 0.15);
      color: #fb7185;
      border: 1px solid rgba(244, 63, 94, 0.3);
    }}

    .badge-mcp-official {{
      background: rgba(139, 92, 246, 0.18);
      color: #c084fc;
      border: 1px solid rgba(139, 92, 246, 0.35);
    }}

    .badge-mcp-comm {{
      background: rgba(168, 85, 247, 0.1);
      color: #e9d5ff;
      border: 1px solid rgba(168, 85, 247, 0.25);
    }}

    .badge-mcp-composio {{
      background: rgba(249, 115, 22, 0.15);
      color: #fdba74;
      border: 1px solid rgba(249, 115, 22, 0.3);
    }}

    .badge-mcp-none {{
      background: rgba(71, 85, 105, 0.2);
      color: #64748b;
      border: 1px solid rgba(71, 85, 105, 0.3);
    }}

    .app-title {{
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .app-cat {{
      font-size: 0.75rem;
      color: var(--text-dim);
    }}

    .doc-link {{
      color: #60a5fa;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.775rem;
      transition: color 0.15s;
    }}

    .doc-link:hover {{
      color: #93c5fd;
      text-decoration: underline;
    }}

    /* Architecture Flow */
    .agent-pipeline-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2rem;
    }}

    .pipeline-stages {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      margin-bottom: 1.75rem;
      position: relative;
    }}

    .stage-card {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.1rem;
      position: relative;
    }}

    .stage-num {{
      font-size: 0.75rem;
      font-weight: 800;
      color: #fb923c;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.35rem;
    }}

    .stage-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.4rem;
    }}

    .stage-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Human vs Agent Split */
    .split-col-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}

    @media (max-width: 768px) {{
      .split-col-2 {{
        grid-template-columns: 1fr;
      }}
    }}

    .role-box {{
      background: rgba(15, 23, 42, 0.5);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.25rem;
    }}

    .role-box h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .role-box ul {{
      list-style: none;
      font-size: 0.825rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .role-box ul li {{
      position: relative;
      padding-left: 1.2rem;
      margin-bottom: 0.4rem;
    }}

    .role-box ul li::before {{
      content: '•';
      position: absolute;
      left: 0.2rem;
      color: var(--composio-orange);
      font-weight: bold;
    }}

    /* Verification Progression */
    .accuracy-track {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2rem;
    }}

    .step-progression {{
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}

    .acc-step {{
      flex: 1;
      min-width: 220px;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.25rem;
    }}

    .acc-step.highlight {{
      border-color: rgba(16, 185, 129, 0.4);
      background: rgba(16, 185, 129, 0.05);
    }}

    .acc-pct {{
      font-size: 2.25rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-main);
      margin-bottom: 0.25rem;
    }}

    .acc-pct.green {{
      color: #34d399;
    }}

    .acc-pct.amber {{
      color: #fbbf24;
    }}

    .acc-label {{
      font-size: 0.825rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 0.4rem;
    }}

    .acc-desc {{
      font-size: 0.775rem;
      color: var(--text-dim);
      line-height: 1.4;
    }}

    /* Hit / Miss Case Studies */
    .audit-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1.25rem;
    }}

    .audit-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }}

    .audit-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 0.5rem;
    }}

    .audit-title {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .audit-claim {{
      background: rgba(244, 63, 94, 0.08);
      border: 1px solid rgba(244, 63, 94, 0.2);
      border-radius: 6px;
      padding: 0.6rem 0.75rem;
      font-size: 0.8rem;
      color: #fda4af;
    }}

    .audit-truth {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.2);
      border-radius: 6px;
      padding: 0.6rem 0.75rem;
      font-size: 0.8rem;
      color: #6ee7b7;
    }}

    .audit-lesson {{
      font-size: 0.775rem;
      color: var(--text-dim);
      line-height: 1.4;
      font-style: italic;
    }}

    /* Modal */
    .modal-backdrop {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(8px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-box {{
      background: #0f172a;
      border: 1px solid var(--border-accent);
      border-radius: 14px;
      max-width: 720px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 2rem;
      position: relative;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }}

    .modal-close {{
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 1.5rem;
      line-height: 1;
    }}

    .modal-close:hover {{
      color: white;
    }}

    .modal-field {{
      margin-bottom: 1.2rem;
    }}

    .modal-field-title {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      font-weight: 700;
      margin-bottom: 0.25rem;
    }}

    .modal-field-content {{
      font-size: 0.9rem;
      color: var(--text-main);
      line-height: 1.5;
    }}

    /* Code Block */
    .terminal-box {{
      background: #030712;
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1.25rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.825rem;
      color: #38bdf8;
      overflow-x: auto;
      line-height: 1.6;
    }}

    .terminal-box .cmd {{
      color: #f8fafc;
      font-weight: 600;
    }}

    .terminal-box .comment {{
      color: #64748b;
    }}

    /* Footer */
    footer {{
      border-top: 1px solid var(--border-subtle);
      padding: 2.5rem 1.5rem;
      text-align: center;
      color: var(--text-dim);
      font-size: 0.85rem;
    }}
  </style>
</head>
<body>

  <!-- Sticky Top Navigation -->
  <header class="sticky-nav">
    <div class="nav-container">
      <a href="#" class="brand-group">
        <div class="brand-logo">C</div>
        <div>
          <div class="brand-title">Composio Product Ops</div>
        </div>
        <span class="brand-badge">Case Study</span>
      </a>
      <ul class="nav-links">
        <li><a href="#patterns">Macro Patterns</a></li>
        <li><a href="#matrix">100 App Matrix</a></li>
        <li><a href="#agent">Agent Architecture</a></li>
        <li><a href="#verification">Verification Loops</a></li>
        <li><a href="#reproduce">Run Agent CLI</a></li>
      </ul>
      <a href="#matrix" class="nav-btn">
        <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/>
        </svg>
        Explore Matrix
      </a>
    </div>
  </header>

  <div class="page-container">

    <!-- Hero Header -->
    <section class="hero">
      <div class="hero-eyebrow">
        <svg width="12" height="12" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"/>
        </svg>
        AI Product Ops Intern Take-Home Case Study
      </div>
      <h1 class="hero-title">100 App Toolkits: Auth, Gating & Patterns</h1>
      <p class="hero-subtitle">
        An autonomous agent research pipeline and verification audit profiling 100 SaaS applications across 10 categories. 
        Designed to identify buildability bottlenecks, model context protocol (MCP) readiness, and auth dynamics for the Composio agent ecosystem.
      </p>
    </section>

    <!-- Key Metrics Ribbon -->
    <div class="metrics-grid">
      <div class="metric-card">
        <div class="metric-val">100 <span class="sub">Apps</span></div>
        <div class="metric-label">Profiled Dataset</div>
        <div class="metric-caption">10 distinct B2B & developer categories analyzed.</div>
      </div>
      <div class="metric-card">
        <div class="metric-val">73<span class="sub">%</span></div>
        <div class="metric-label">Self-Serve Rate</div>
        <div class="metric-caption">Zero sales friction; credentials obtainable in &lt;5 mins.</div>
      </div>
      <div class="metric-card">
        <div class="metric-val">82<span class="sub">%</span></div>
        <div class="metric-label">Agent-Ready Today</div>
        <div class="metric-caption">Public documented REST/GraphQL with active write scopes.</div>
      </div>
      <div class="metric-card">
        <div class="metric-val">26<span class="sub">%</span></div>
        <div class="metric-label">Native MCP Ready</div>
        <div class="metric-caption">Official or native Model Context Protocol servers exist.</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color: #34d399;">+17<span class="sub">%</span></div>
        <div class="metric-label">Verification Gain</div>
        <div class="metric-caption">Accuracy advanced from 70% (Pass 1) to 87% (Pass 2) to 100% (Human).</div>
      </div>
    </div>

    <!-- Section 1: Executive Macro Patterns -->
    <section id="patterns" class="section-wrap">
      <div class="section-header">
        <div class="section-title-wrap">
          <h2>
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color: #f97316;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
            </svg>
            Headline Patterns: Insight Over Raw Table
          </h2>
          <p>The 5 fundamental architectural trends shaping tool calling across the 100 apps.</p>
        </div>
      </div>

      <div class="patterns-grid">
        <div class="pattern-card">
          <span class="pattern-badge">Pattern 1: Auth Dominance</span>
          <h3>Auth Polarization: Bearer Tokens vs OAuth2</h3>
          <p>
            <strong>59% of tools</strong> utilize static API Keys or Bearer Tokens (concentrated heavily in Developer Infrastructure, Data/Scraping, and modern AI APIs), enabling zero-click invocation for agents. 
            Conversely, <strong>33% mandate OAuth2</strong>—predominantly multi-tenant collaborative SaaS (CRMs, Helpdesks, and Ad networks) where customer data segregation and user approval flows require managed token exchanges.
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-badge">Pattern 2: Access Barrier</span>
          <h3>73% Self-Serve Accessibility vs 27% Gated Moats</h3>
          <p>
            Nearly three-quarters of the catalog (73 apps) offer instant self-serve sandboxes or free plans with immediate API access. 
            The remaining 27% split into <strong>12% Paid-Gated</strong> (card/subscription required, e.g. Aircall, GoHighLevel, SE Ranking) and <strong>15% Partner-Gated</strong> (enterprise sales calls, Intapp DealCloud, PitchBook, or corporate underwriting like Ramp/Brex).
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-badge">Pattern 3: Primary Blocker</span>
          <h3>Enterprise Sales & App Review as the #1 Blocker</h3>
          <p>
            The hardest blocker for agent adoption is not API design, but organizational gating: 
            <strong>Salesforce Commerce Cloud, DealCloud, Waterfall.io, and PitchBook</strong> completely restrict public sandboxes behind 5-figure enterprise contracts, while <strong>Meta, Google Ads, and LinkedIn</strong> lock production write permissions behind rigorous legal App Reviews.
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-badge">Pattern 4: Protocol Shift</span>
          <h3>The Model Context Protocol (MCP) Wave (26%)</h3>
          <p>
            Over a quarter of surveyed apps (including cutting-edge tools like Devin, Consensus, TranscriptAPI, Otter, Firecrawl, Supabase, GitHub, and Sentry) already provide native or official MCP servers. 
            This validates Composio's strategic roadmap: apps are converting from raw HTTP endpoints directly into agent-callable schemas.
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-badge">Pattern 5: Execution Edge</span>
          <h3>The CLI & Local Fallback (2%)</h3>
          <p>
            Crucial OSINT and diagramming tools like <strong>Sherlock</strong> and <strong>Mermaid CLI</strong> do not expose any cloud REST endpoints. 
            For an agent framework, supporting local sub-process execution, container sandboxes, or local CLI MCP wrappers is mandatory to achieve full workflow completion.
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-badge">Pattern 6: Consumer Silos</span>
          <h3>UI-Only Hallucinations (NotebookLM)</h3>
          <p>
            Popular consumer AI products (such as Google NotebookLM) have zero developer APIs despite public interest. 
            Agents attempting to interface with them must either bypass via browser automation (DevTools CDP) or fall back to underlying infrastructure (Google Vertex AI / Gemini Document Grounding API).
          </p>
        </div>
      </div>

      <!-- Charts & Visual Scorecards -->
      <div class="charts-split">
        <div class="chart-box">
          <h4>
            <span>Primary Auth Distribution</span>
            <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: normal;">100 Apps</span>
          </h4>
          <div class="bar-row">
            <div class="bar-label">API Key / Bearer</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 59%; background: linear-gradient(90deg, #3b82f6, #60a5fa);"></div>
            </div>
            <div class="bar-val">59%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">OAuth2</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 33%; background: linear-gradient(90deg, #8b5cf6, #a78bfa);"></div>
            </div>
            <div class="bar-val">33%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">HTTP Basic</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 3%; background: linear-gradient(90deg, #f59e0b, #fbbf24);"></div>
            </div>
            <div class="bar-val">3%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">CLI / Local / No Auth</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 3%; background: linear-gradient(90deg, #10b981, #34d399);"></div>
            </div>
            <div class="bar-val">3%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">Custom / Header / HMAC</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 2%; background: linear-gradient(90deg, #f43f5e, #fb7185);"></div>
            </div>
            <div class="bar-val">2%</div>
          </div>
        </div>

        <div class="chart-box">
          <h4>
            <span>Access Model Breakdown</span>
            <span style="font-size: 0.75rem; color: var(--text-dim); font-weight: normal;">Gating Reality</span>
          </h4>
          <div class="bar-row">
            <div class="bar-label">Self-Serve (Free/Trial)</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 73%; background: linear-gradient(90deg, #10b981, #34d399);"></div>
            </div>
            <div class="bar-val">73%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">Partner / Sales Gated</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 15%; background: linear-gradient(90deg, #f43f5e, #fb7185);"></div>
            </div>
            <div class="bar-val">15%</div>
          </div>
          <div class="bar-row">
            <div class="bar-label">Paid Plan Gated</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 12%; background: linear-gradient(90deg, #f59e0b, #fbbf24);"></div>
            </div>
            <div class="bar-val">12%</div>
          </div>
          <div class="bar-row" style="margin-top: 1rem; padding-top: 0.75rem; border-top: 1px dashed var(--border-subtle);">
            <div class="bar-label" style="font-weight: 700; color: var(--text-main);">Agent Buildability</div>
            <div class="bar-track">
              <div class="bar-fill" style="width: 82%; background: linear-gradient(90deg, #f97316, #fb923c);"></div>
            </div>
            <div class="bar-val">82% Ready</div>
          </div>
        </div>
      </div>

      <!-- Easy Wins vs Outreach Matrix -->
      <div class="quadrant-grid">
        <div class="quadrant-box wins">
          <div class="quadrant-title" style="color: #34d399;">
            <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"/>
            </svg>
            Easy Wins: Instant Autonomous Toolkits
          </div>
          <div class="quadrant-subtitle">Zero onboarding friction, instant tokens, high composability, and active MCP support.</div>
          <div class="quadrant-item">
            <div><span class="name">GitHub</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Dev Infra)</span></div>
            <div class="note">Universal PATs, 5k req/hr, official MCP</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Firecrawl</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Scraping)</span></div>
            <div class="note">500 free credits, markdown output, official MCP</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Supabase</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Dev Infra)</span></div>
            <div class="note">Instant Postgres DB, PostgREST + pgvector, official MCP</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Notion</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Productivity)</span></div>
            <div class="note">30-sec internal integration secret, official MCP</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Stripe</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Fintech)</span></div>
            <div class="note">Instant test mode keys, official agent toolkit</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Consensus</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(AI/Media)</span></div>
            <div class="note">Instant API key + official MCP with OAuth PKCE</div>
          </div>
        </div>

        <div class="quadrant-box outreach">
          <div class="quadrant-title" style="color: #fb7185;">
            <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
            </svg>
            Outreach Required: Commercial & Contract Gates
          </div>
          <div class="quadrant-subtitle">Requires human partner agreements, sales calls, or corporate entity verification.</div>
          <div class="quadrant-item">
            <div><span class="name">PitchBook</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Fintech)</span></div>
            <div class="note">$20k+/yr contract, no self-serve, enterprise demo only</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">DealCloud</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(CRM)</span></div>
            <div class="note">Intapp client contract required, per-tenant provisioning</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Meta Ads</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Marketing)</span></div>
            <div class="note">Meta App Review & Business Manager corporate verification</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Salesforce Commerce</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Ecommerce)</span></div>
            <div class="note">Account Manager contract gate; Demandware stack</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">Waterfall.io</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(Data)</span></div>
            <div class="note">Enterprise B2B data vendor; sales demo required</div>
          </div>
          <div class="quadrant-item">
            <div><span class="name">NotebookLM</span> <span style="color: var(--text-dim); font-size: 0.75rem;">(AI/Media)</span></div>
            <div class="note">UI-only consumer app; fallback to Google Vertex AI</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Interactive Matrix Table -->
    <section id="matrix" class="section-wrap">
      <div class="section-header">
        <div class="section-title-wrap">
          <h2>
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color: #3b82f6;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/>
            </svg>
            100 App Findings Matrix
          </h2>
          <p>Search, filter, and inspect detailed auth, gating, API surface, and buildability data for all 100 apps.</p>
        </div>
        <div class="export-btns">
          <button class="btn-secondary" onclick="exportData('csv')">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/>
            </svg>
            Download CSV
          </button>
          <button class="btn-secondary" onclick="exportData('json')">
            <svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
            </svg>
            Download JSON
          </button>
        </div>
      </div>

      <!-- Controls -->
      <div class="table-controls">
        <div class="search-row">
          <div class="search-input-wrap">
            <svg class="search-icon" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
            <input type="text" id="searchInput" class="search-input" placeholder="Search by app name, description, auth, category, blocker...">
          </div>
        </div>

        <div class="filters-row">
          <span class="filter-label">Category:</span>
          <div class="filter-pill active" onclick="setCategoryFilter('all', this)">All (100)</div>
          <div class="filter-pill" onclick="setCategoryFilter('CRM and Sales', this)">CRM</div>
          <div class="filter-pill" onclick="setCategoryFilter('Support and Helpdesk', this)">Helpdesk</div>
          <div class="filter-pill" onclick="setCategoryFilter('Communications and Messaging', this)">Messaging</div>
          <div class="filter-pill" onclick="setCategoryFilter('Marketing, Ads, Email and Social', this)">Marketing</div>
          <div class="filter-pill" onclick="setCategoryFilter('Ecommerce', this)">Ecommerce</div>
          <div class="filter-pill" onclick="setCategoryFilter('Data, SEO and Scraping', this)">Data/SEO</div>
          <div class="filter-pill" onclick="setCategoryFilter('Developer, Infra and Data platforms', this)">Dev Infra</div>
          <div class="filter-pill" onclick="setCategoryFilter('Productivity and Project Management', this)">Productivity</div>
          <div class="filter-pill" onclick="setCategoryFilter('Finance and Fintech', this)">Fintech</div>
          <div class="filter-pill" onclick="setCategoryFilter('AI, Research and Media-native', this)">AI/Media</div>
        </div>

        <div class="filters-row" style="padding-top: 0.5rem; border-top: 1px solid rgba(30, 41, 59, 0.4);">
          <span class="filter-label">Access Gate:</span>
          <div class="filter-pill active" onclick="setAccessFilter('all', this)">All</div>
          <div class="filter-pill" onclick="setAccessFilter('Self-Serve', this)">Self-Serve</div>
          <div class="filter-pill" onclick="setAccessFilter('Paid Gated', this)">Paid Gated</div>
          <div class="filter-pill" onclick="setAccessFilter('Partner Gated', this)">Partner Gated</div>

          <span class="filter-label" style="margin-left: 1rem;">Buildability:</span>
          <div class="filter-pill active" onclick="setBuildFilter('all', this)">All</div>
          <div class="filter-pill" onclick="setBuildFilter('Ready', this)">Ready</div>
          <div class="filter-pill" onclick="setBuildFilter('Partial', this)">Partial</div>
          <div class="filter-pill" onclick="setBuildFilter('High Friction', this)">High Friction</div>
          <div class="filter-pill" onclick="setBuildFilter('Blocked', this)">Blocked</div>

          <span class="filter-label" style="margin-left: 1rem;">MCP Status:</span>
          <div class="filter-pill active" onclick="setMcpFilter('all', this)">All</div>
          <div class="filter-pill" onclick="setMcpFilter('Official', this)">Official MCP</div>
          <div class="filter-pill" onclick="setMcpFilter('Composio', this)">Composio Supported</div>
        </div>
      </div>

      <!-- Table View -->
      <div class="table-container">
        <table class="matrix-table" id="appsTable">
          <thead>
            <tr>
              <th style="width: 50px;">#</th>
              <th style="width: 170px;">App</th>
              <th style="width: 280px;">One-Liner</th>
              <th style="width: 140px;">Primary Auth</th>
              <th style="width: 120px;">Access Gate</th>
              <th style="width: 130px;">API Surface</th>
              <th style="width: 110px;">Buildability</th>
              <th style="width: 140px;">MCP Status</th>
              <th style="width: 100px;">Evidence</th>
            </tr>
          </thead>
          <tbody id="tableBody">
            <!-- Rendered by JS -->
          </tbody>
        </table>
      </div>
      <div id="tableCount" style="font-size: 0.8rem; color: var(--text-dim); text-align: right; margin-top: -1.2rem; margin-bottom: 2rem;">
        Showing 100 of 100 apps
      </div>
    </section>

    <!-- Section 3: The Research Agent Architecture -->
    <section id="agent" class="section-wrap">
      <div class="section-header">
        <div class="section-title-wrap">
          <h2>
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color: #8b5cf6;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
            </svg>
            The Research Agent: Architecture & Human Hand-Off
          </h2>
          <p>How the autonomous research pipeline operates, where it succeeds, and where human judgment was required.</p>
        </div>
      </div>

      <div class="agent-pipeline-box">
        <div class="pipeline-stages">
          <div class="stage-card">
            <div class="stage-num">Phase 1</div>
            <div class="stage-title">Seed Intake</div>
            <div class="stage-desc">Loads 100 app seeds with hint URLs and categories into structured research queues.</div>
          </div>
          <div class="stage-card">
            <div class="stage-num">Phase 2</div>
            <div class="stage-title">Portal Ingestion</div>
            <div class="stage-desc">Scrapes developer documentation, checks OpenAPI / Swagger specs, and queries subdomains.</div>
          </div>
          <div class="stage-card">
            <div class="stage-num">Phase 3</div>
            <div class="stage-title">Schema Extraction</div>
            <div class="stage-desc">Classifies auth mechanisms, self-serve friction, API surfaces, and candidate MCP support.</div>
          </div>
          <div class="stage-card">
            <div class="stage-num">Phase 4</div>
            <div class="stage-title">Verification Loop</div>
            <div class="stage-desc">Autonomous cross-check: verifies developer portal status codes, probes headers, checks contradictions.</div>
          </div>
          <div class="stage-card">
            <div class="stage-num">Phase 5</div>
            <div class="stage-title">Pattern Synthesis</div>
            <div class="stage-desc">Statistical aggregation, blocker ranking, and clustering for Product Ops decision making.</div>
          </div>
        </div>

        <div class="split-col-2">
          <div class="role-box">
            <h4 style="color: #38bdf8;">
              <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              What The Agent Did Autonomously
            </h4>
            <ul>
              <li><strong>Bulk URL Resolution:</strong> Traversed documentation trees across 100 developer sites, locating direct REST & GraphQL API references.</li>
              <li><strong>Auth Classification:</strong> Identified Bearer tokens, HTTP Basic schemes, and OAuth2 flow parameters from technical headers.</li>
              <li><strong>MCP Directory Scanning:</strong> Checked official registries and GitHub repositories for native Model Context Protocol implementations.</li>
              <li><strong>Specification Parsing:</strong> Ingested OpenAPI / Postman schemas to measure API surface breadth (endpoints and operations).</li>
            </ul>
          </div>

          <div class="role-box">
            <h4 style="color: #fb923c;">
              <svg width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
              </svg>
              Where A Human Was Needed (Product Ops)
            </h4>
            <ul>
              <li><strong>Commercial Paywall Detection:</strong> Discovered that apps like Ahrefs and SE Ranking display open docs but restrict API keys to top-tier enterprise plans.</li>
              <li><strong>Consumer UI-Only Disambiguation:</strong> Disentangled NotebookLM from the underlying Gemini API, identifying that NotebookLM has no public API.</li>
              <li><strong>Multi-Product Umbrella Scoping:</strong> Disambiguated Salesforce CRM (self-serve developer orgs) from Salesforce Commerce Cloud (contract-gated Demandware).</li>
              <li><strong>Local CLI Identification:</strong> Flagged that tools like Sherlock and Mermaid CLI are local utilities that must run in containers, not cloud REST endpoints.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Verification Loops & Hit/Miss Audit -->
    <section id="verification" class="section-wrap">
      <div class="section-header">
        <div class="section-title-wrap">
          <h2>
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color: #10b981;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            Verification Loops & Accuracy Progression
          </h2>
          <p>Transparent comparison of Pass 1 (naive scraper), Pass 2 (verification agent), and Pass 3 (human audit).</p>
        </div>
      </div>

      <div class="accuracy-track">
        <div class="step-progression">
          <div class="acc-step">
            <div class="acc-pct amber">70.0%</div>
            <div class="acc-label">Pass 1: Naive Agent</div>
            <div class="acc-desc">
              Zero-shot snippet extraction. Blind to enterprise paywalls; assumed all documented APIs were self-serve; misclassified local CLI tools as REST.
            </div>
          </div>
          <div class="acc-step">
            <div class="acc-pct" style="color: #60a5fa;">87.0%</div>
            <div class="acc-label">Pass 2: Verification Loop</div>
            <div class="acc-desc">
              Autonomous cross-check: verified developer portal HTTP status, audited authentication headers, queried MCP registries (+17.0% accuracy gain).
            </div>
          </div>
          <div class="acc-step highlight">
            <div class="acc-pct green">100.0%</div>
            <div class="acc-label">Pass 3: Human Ground Truth</div>
            <div class="acc-desc">
              Manual inspection of edge cases: tested corporate account gates, unlisted SDK portals, and UI-only applications.
            </div>
          </div>
        </div>

        <h4 style="font-size: 1rem; font-weight: 700; color: var(--text-main); margin-bottom: 1rem;">
          Transparent Hit & Miss Audit Log (Case Studies)
        </h4>

        <div class="audit-grid">
          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#10: DealCloud</span>
              <span class="badge badge-friction">High Friction</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> Self-serve REST API with public developer portal.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> Gated behind enterprise Intapp sales contract. No public sandbox exists; credentials provisioned per corporate tenant.
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Swagger/Redoc portals often look public, but tenant provisioning is strictly enterprise-gated.
            </div>
          </div>

          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#91: NotebookLM</span>
              <span class="badge badge-blocked">Blocked</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> Ready toolkit using Google Cloud Gemini API keys.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> Consumer NotebookLM has NO public API. While built on Gemini models, the product itself is closed UI-only.
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Never conflate foundation model infrastructure with consumer AI end-products.
            </div>
          </div>

          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#92: Otter AI</span>
              <span class="badge badge-ready">Ready (via MCP)</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> High Friction because REST API requires Enterprise plan.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> Otter launched an official managed MCP Server (mcp.otter.ai) providing direct agent querying for transcripts.
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Modern SaaS apps frequently bypass legacy REST gating by shipping native MCP endpoints.
            </div>
          </div>

          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#39: Threads (Meta)</span>
              <span class="badge badge-ready">Ready</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> Blocked; no public API exists for Threads.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> Threads launched its public Graph API with OAuth2, publishing, and reply management (June 2024).
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Outdated LLM knowledge cutoffs must be counterbalanced with real-time web verification.
            </div>
          </div>

          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#58: Sherlock</span>
              <span class="badge badge-ready">Ready (CLI)</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> Cloud REST API with API token authentication.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> Sherlock is an open-source Python CLI utility on GitHub. Zero auth; runs locally or inside Docker.
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Open-source CLI tools must be classified as containerized local runtimes, not SaaS endpoints.
            </div>
          </div>

          <div class="audit-card">
            <div class="audit-header">
              <span class="audit-title">#85: iPayX</span>
              <span class="badge badge-ready">Ready (MCP)</span>
            </div>
            <div class="audit-claim">
              <strong>Pass 1 Claim:</strong> Obscure banking service with no public documentation.
            </div>
            <div class="audit-truth">
              <strong>Ground Truth:</strong> iPayX is an AI FX audit protocol with an active SSE Model Context Protocol server on Supabase edge functions.
            </div>
            <div class="audit-lesson">
              <em>Lesson:</em> Querying Supabase and edge runtime endpoints often reveals agent-native MCP servers.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Runnable CLI Proof -->
    <section id="reproduce" class="section-wrap">
      <div class="section-header">
        <div class="section-title-wrap">
          <h2>
            <svg width="22" height="22" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color: #f97316;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
            </svg>
            Runnable Proof: Execute the Research Agent
          </h2>
          <p>Reproduce the findings, run verification audits, and query specific apps from the terminal.</p>
        </div>
      </div>

      <div class="terminal-box">
        <span class="comment"># 1. Profile a specific app (e.g. App #10 DealCloud or #91 NotebookLM)</span><br>
        <span class="cmd">python3 agent/research_pipeline.py --app-id 10</span><br>
        <span class="cmd">python3 agent/research_pipeline.py --app-id 91</span><br><br>

        <span class="comment"># 2. Filter research pipeline by category (e.g. Fintech, Ecommerce, CRM)</span><br>
        <span class="cmd">python3 agent/research_pipeline.py --category Fintech</span><br><br>

        <span class="comment"># 3. Run the Verification Engine & Accuracy Benchmark</span><br>
        <span class="cmd">python3 agent/verifier.py</span><br><br>

        <span class="comment"># 4. Generate statistical macro patterns and cluster summary</span><br>
        <span class="cmd">python3 agent/analyzer.py</span>
      </div>
    </section>

  </div>

  <!-- Detail Modal -->
  <div id="detailModal" class="modal-backdrop" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <button class="modal-close" onclick="closeModal(event)">&times;</button>
      <div id="modalContent">
        <!-- Rendered by JS -->
      </div>
    </div>
  </div>

  <footer>
    <p>Composio AI Product Ops Case Study &bull; Built with autonomous agent verification loops &bull; 100 Apps Profiled</p>
  </footer>

  <script>
    // Embedded Data
    const rawApps = {apps_json_str};
    const patterns = {patterns_json_str};
    const audit = {audit_json_str};

    let currentCategory = 'all';
    let currentAccess = 'all';
    let currentBuild = 'all';
    let currentMcp = 'all';
    let currentSearch = '';

    // Render Table
    function renderTable() {{
      const tbody = document.getElementById('tableBody');
      const filtered = rawApps.filter(app => {{
        // Category Filter
        if (currentCategory !== 'all' && app.category !== currentCategory) return false;
        // Access Filter
        if (currentAccess !== 'all' && app.access_model !== currentAccess) return false;
        // Build Filter
        if (currentBuild !== 'all' && app.buildability !== currentBuild) return false;
        // MCP Filter
        if (currentMcp === 'Official' && !app.mcp_status.includes('Official')) return false;
        if (currentMcp === 'Composio' && !app.mcp_status.includes('Composio')) return false;

        // Search Filter
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

      document.getElementById('tableCount').innerText = `Showing ${{filtered.length}} of ${{rawApps.length}} apps`;

      if (filtered.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="9" style="text-align: center; padding: 2.5rem; color: var(--text-dim);">No apps matching the selected filters.</td></tr>`;
        return;
      }}

      tbody.innerHTML = filtered.map(app => {{
        // Build badge class
        let bClass = 'badge-ready';
        if (app.buildability === 'Partial') bClass = 'badge-partial';
        else if (app.buildability === 'High Friction') bClass = 'badge-friction';
        else if (app.buildability === 'Blocked') bClass = 'badge-blocked';

        // Access badge class
        let aClass = 'badge-selfserve';
        if (app.access_model === 'Paid Gated') aClass = 'badge-paidgated';
        else if (app.access_model === 'Partner Gated') aClass = 'badge-partnergated';

        // MCP badge class
        let mClass = 'badge-mcp-none';
        if (app.mcp_status.includes('Official')) mClass = 'badge-mcp-official';
        else if (app.mcp_status.includes('Community')) mClass = 'badge-mcp-comm';
        else if (app.mcp_status.includes('Composio')) mClass = 'badge-mcp-composio';

        return `
          <tr onclick="openModal(${{app.id}})">
            <td style="color: var(--text-dim); font-family: monospace;">${{app.id}}</td>
            <td>
              <div class="app-title">${{app.name}}</div>
              <div class="app-cat">${{app.category}}</div>
            </td>
            <td style="color: var(--text-muted); font-size: 0.8rem; line-height: 1.4;">${{app.one_liner}}</td>
            <td><span style="font-family: monospace; font-size: 0.775rem;">${{app.primary_auth}}</span></td>
            <td><span class="badge ${{aClass}}">${{app.access_model}}</span></td>
            <td style="font-size: 0.775rem; color: var(--text-muted);">${{app.api_surface.split(',')[0]}}</td>
            <td><span class="badge ${{bClass}}">${{app.buildability}}</span></td>
            <td><span class="badge ${{mClass}}">${{app.mcp_status.split('/')[0].trim()}}</span></td>
            <td>
              <a href="${{app.docs_url}}" target="_blank" rel="noopener noreferrer" class="doc-link" onclick="event.stopPropagation()">
                Docs
                <svg width="10" height="10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                </svg>
              </a>
            </td>
          </tr>
        `;
      }}).join('');
    }}

    // Filter Handlers
    function setCategoryFilter(cat, elem) {{
      currentCategory = cat;
      elem.parentNode.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      elem.classList.add('active');
      renderTable();
    }}

    function setAccessFilter(acc, elem) {{
      currentAccess = acc;
      elem.parentNode.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      elem.classList.add('active');
      renderTable();
    }}

    function setBuildFilter(build, elem) {{
      currentBuild = build;
      elem.parentNode.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      elem.classList.add('active');
      renderTable();
    }}

    function setMcpFilter(mcp, elem) {{
      currentMcp = mcp;
      elem.parentNode.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      elem.classList.add('active');
      renderTable();
    }}

    // Search input listener
    document.getElementById('searchInput').addEventListener('input', (e) => {{
      currentSearch = e.target.value;
      renderTable();
    }});

    // Modal
    function openModal(appId) {{
      const app = rawApps.find(a => a.id === appId);
      if (!app) return;

      const content = document.getElementById('modalContent');
      content.innerHTML = `
        <div style="display: flex; align-items: baseline; gap: 0.75rem; margin-bottom: 0.5rem;">
          <h3 style="font-size: 1.4rem; font-weight: 800; color: white;">#${{app.id}}: ${{app.name}}</h3>
          <span style="font-size: 0.85rem; color: var(--text-dim);">${{app.category}}</span>
        </div>
        <p style="font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1.5rem;">${{app.one_liner}}</p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
          <div class="modal-field">
            <div class="modal-field-title">Primary Auth Method</div>
            <div class="modal-field-content" style="font-family: monospace;">${{app.primary_auth}}</div>
          </div>
          <div class="modal-field">
            <div class="modal-field-title">Supported Auth Schemes</div>
            <div class="modal-field-content">${{app.auth_methods.join(', ')}}</div>
          </div>
        </div>

        <div class="modal-field">
          <div class="modal-field-title">Access & Credential Provisioning</div>
          <div class="modal-field-content">${{app.access_details}}</div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem;">
          <div class="modal-field">
            <div class="modal-field-title">API Surface & Breadth</div>
            <div class="modal-field-content">${{app.api_surface}} (${{app.api_breadth}})</div>
          </div>
          <div class="modal-field">
            <div class="modal-field-title">Model Context Protocol (MCP)</div>
            <div class="modal-field-content">${{app.mcp_status}}</div>
          </div>
        </div>

        <div class="modal-field">
          <div class="modal-field-title">Buildability Verdict & Primary Blocker</div>
          <div class="modal-field-content">
            <strong>[${{app.buildability}}]</strong> &bull; ${{app.main_blocker}}
          </div>
        </div>

        <div class="modal-field" style="background: rgba(249, 115, 22, 0.08); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 8px; padding: 0.85rem;">
          <div class="modal-field-title" style="color: #fb923c;">Composio Toolkit Recommendation</div>
          <div class="modal-field-content">${{app.composio_strategy}}</div>
        </div>

        <div class="modal-field" style="margin-top: 1rem;">
          <div class="modal-field-title">Verification Notes (Pass 1 vs Ground Truth)</div>
          <div class="modal-field-content" style="font-size: 0.825rem; color: var(--text-muted); font-style: italic;">
            ${{app.verification_notes}}
          </div>
        </div>

        <div style="margin-top: 1.5rem; text-align: right;">
          <a href="${{app.docs_url}}" target="_blank" rel="noopener noreferrer" class="nav-btn" style="display: inline-flex;">
            Open Official Documentation
            <svg width="12" height="12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
            </svg>
          </a>
        </div>
      `;

      document.getElementById('detailModal').classList.add('open');
    }}

    function closeModal(e) {{
      document.getElementById('detailModal').classList.remove('open');
    }}

    // Export Functionality
    function exportData(type) {{
      if (type === 'json') {{
        const blob = new Blob([JSON.stringify(rawApps, null, 2)], {{ type: 'application/json' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'composio_100_apps_dataset.json';
        a.click();
      }} else if (type === 'csv') {{
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

    // Initial render
    renderTable();
  </script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote index.html successfully.")

if __name__ == "__main__":
    generate_html()
