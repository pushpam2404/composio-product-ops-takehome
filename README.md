# Technical Research Report: 100 Application Toolkits for AI Agents

> **Composio AI Product Ops Evaluation**  
> An automated research pipeline and verification audit for 100 software applications across 10 categories. 
> Analyzes authentication types, developer access limits, API surfaces, and Model Context Protocol (MCP) readiness.
>
> 🌐 **Live Deployed Case Study Dashboard:** [https://pushpam2404.github.io/composio-product-ops-takehome/](https://pushpam2404.github.io/composio-product-ops-takehome/)  
> 📦 **GitHub Source Repository:** [https://github.com/pushpam2404/composio-product-ops-takehome](https://github.com/pushpam2404/composio-product-ops-takehome)

---

## 1. Technical Summary

Composio enables AI agents to execute actions in external applications. 
Before engineers create a tool for an application, they must verify four items:
1. **Authentication Type:** API key, OAuth2, HTTP Basic, or Bearer token.
2. **Access Model:** Self-serve developer access versus paid subscription or sales approval.
3. **API Surface:** REST, GraphQL, gRPC, or local command-line interface.
4. **Agent Readiness:** Whether an AI agent can execute operations immediately or faces technical blockers.

This project implements an automated research and verification pipeline. 
The pipeline analyzed 100 target applications and verified data accuracy through a multi-stage review loop.

### Aggregate Technical Metrics
* **Total Applications Analyzed:** 100 across 10 software categories.
* **Self-Serve Access Rate:** 73% (73 applications provide free developer accounts or trials).
* **Agent-Ready Rate:** 82% (82 applications possess public, documented write APIs).
* **Native MCP Support:** 26% (26 applications operate official Model Context Protocol servers).
* **Dominant Authentication:** 59% use API Keys or Bearer tokens; 33% use OAuth2.
* **Verification Accuracy Gain:** +17.0% net improvement (70.0% Pass 1 to 87.0% Pass 2 to 100.0% Human Ground Truth).

---

## 2. Macro Patterns and Technical Rules

Clustering the 100 applications establishes six technical rules:

### Rule 1: Infrastructure Uses Bearer Tokens; Collaborative Tools Use OAuth2
59 applications use static API keys or Bearer tokens. 
These are concentrated in developer infrastructure, web scraping, and AI model APIs. 
They permit autonomous agent calls without user browser interaction. 
33 applications mandate OAuth2. 
These are collaborative CRMs, Helpdesks, and Ad networks that require tenant scoping and user delegation.

### Rule 2: 73% of Tools Provide Self-Serve Credentials
73 applications allow instant developer registration with immediate access to keys. 
12 applications require an active paid subscription (e.g. Aircall, GoHighLevel, SE Ranking). 
15 applications require contact with sales representatives or enterprise contracts (e.g. DealCloud, PitchBook).

### Rule 3: Sales Approvals and App Reviews Are the Primary Blockers
Technical blockers are rarely missing HTTP endpoints. 
Enterprise applications (PitchBook, DealCloud, Waterfall.io) enforce mandatory contracts starting at $10,000 to $50,000 annually. 
Advertising platforms (Meta Ads, Google Ads Developer Token, LinkedIn Ads) require corporate legal verification and manual App Reviews.

### Rule 4: 26% of Applications Already Support Model Context Protocol
26 applications support MCP directly. 
This includes Devin, Consensus, TranscriptAPI, Otter, Firecrawl, Supabase, GitHub, and Sentry. 
Software vendors are deploying agent-native interfaces alongside standard REST endpoints.

### Rule 5: Local Command-Line Tools Require Container Environments
Sherlock and Mermaid CLI do not expose cloud REST APIs. 
An agent runtime must support local container execution to run open-source command-line tools.

### Rule 6: Consumer AI Interfaces Often Lack Public APIs
Google NotebookLM has no public developer API. 
Agents cannot call NotebookLM directly. Agents must use Google Cloud Vertex AI to access underlying models.

---

## 3. Tool Classification Matrix

| Quadrant | Applications | Technical Characteristics | Action Strategy |
| :--- | :--- | :--- | :--- |
| **Instant Wins** | **GitHub, Firecrawl, Supabase, Notion, Linear, Stripe, Apify, TranscriptAPI, Consensus, Reducto** | Self-serve keys, public schemas, official MCP servers or simple Bearer headers. | Build toolkits immediately. Zero credential delay. |
| **Enterprise Outreach** | **PitchBook, DealCloud, Salesforce Commerce Cloud, Waterfall.io, Gladly** | Gated behind annual enterprise contracts. No public developer sandbox. | Use Bring-Your-Own-Credentials (BYOC) pattern for contracted clients. |
| **Compliance Gated** | **Meta Ads, Google Ads, LinkedIn Ads, WhatsApp Business, Pinterest** | Sandboxes exist, but production write access requires App Review and business verification. | Complete platform partner programs and corporate identity verification. |
| **Local Runtime** | **Sherlock, Mermaid CLI** | No cloud REST endpoints. Pure open-source command-line execution. | Package inside containerized local MCP execution tools. |

---

## 4. Research Methodology, AI Tooling, and Human Hand-Off

### Honesty & Methodology Statement
In direct alignment with the assignment guidelines (*"Use AI tooling freely (that is the job), but understand and be able to explain everything you submit; if the agent got things wrong or an app defeated you, say so on the page"*), this research combines AI-assisted knowledge synthesis with rigorous human-in-the-loop verification against real vendor documentation and licensing terms. Single-turn AI generation was used to accelerate initial profiling, while manual investigation resolved enterprise paywalls, local CLI dependencies, and UI-only applications.

```
[Phase 1: Seed Intake & AI Synthesis] ──► [Phase 2: Schema Normalization] ──► [Phase 3: Live Docs Verification]
                                                                                        │
[Final Single-Page Case Study] ◄── [Phase 5: Ground Truth Synthesis] ◄── [Phase 4: Human Edge-Case Audit]
```

### Division of Work: AI Tooling vs Human Verification

#### Tasks Executed with AI Tooling & Scripts
* Generated initial technical candidate profiles across all 100 applications using LLM knowledge synthesis.
* Extracted and standardized HTTP authentication headers, token structures, and access models into a unified schema.
* Ingested OpenAPI and Redoc endpoints to estimate API surface breadth.
* Computed statistical macro pattern clustering across 10 software categories.
* Formatted and generated structured data files (`apps_100.json`, `apps_100.csv`) and verification audit records.
* Executed automated schema integrity validation and live documentation URL reachability checks.

#### Tasks Executed by Human Verification & Manual Auditing
* Identified commercial paywalls on open documentation portals (Ahrefs, SE Ranking, PitchBook).
* Overrode AI hallucination on NotebookLM (confirmed consumer UI has zero public developer API despite underlying Gemini models).
* Identified enterprise sales contract barriers on open Swagger portals (DealCloud).
* Verified local binary execution requirements for Sherlock and Mermaid CLI (requiring containers, not REST).
* Discovered newly launched official Model Context Protocol servers (Otter AI at `mcp.otter.ai`).
* Resolved unlisted developer documentation on subdomains (fanbasis at `dev-docs.fanbasis.com`).

---

## 5. Verification Benchmark and Hit/Miss Audit

We measured accuracy across three verification stages:
* **Pass 1 (Naive Agent):** **70.0% Accuracy** (30 errors). Single-pass extraction failed to detect enterprise paywalls and misclassified CLI tools as REST.
* **Pass 2 (Verification Loop):** **87.0% Accuracy** (**+17.0% net gain**). Automated cross-checks verified HTTP response codes, checked OpenAPI endpoints, and queried MCP registries.
* **Pass 3 (Human Ground Truth):** **100.0% Accuracy**. Manual review resolved all edge cases, paywalls, and unlisted portals.

### Specific Discrepancies and Corrections

1. **DealCloud (#10 - CRM and Sales):**
   * *Pass 1 Claim:* Self-serve REST API with standard public portal.
   * *Ground Truth:* Intapp DealCloud requires enterprise sales contracts. No public sandbox exists. Credentials are provisioned per corporate tenant.
   * *Lesson:* Open Swagger documentation does not mean open developer access.
2. **NotebookLM (#91 - AI, Research and Media-native):**
   * *Pass 1 Claim:* Ready agent toolkit using Google Gemini API keys.
   * *Ground Truth:* NotebookLM has **no public developer API**. The consumer product is UI-only.
   * *Lesson:* Do not conflate underlying foundation model infrastructure with consumer AI products.
3. **Otter AI (#92 - AI, Research and Media-native):**
   * *Pass 1 Claim:* High Friction because REST API requires an Enterprise Plan.
   * *Ground Truth:* Otter launched an official managed **MCP Server (`mcp.otter.ai`)** that allows AI tools to query meeting transcripts directly.
   * *Lesson:* Modern applications bypass REST paywalls by shipping native MCP endpoints.
4. **Threads (Meta) (#39 - Marketing and Social):**
   * *Pass 1 Claim:* Blocked; no public API exists for Threads.
   * *Ground Truth:* Threads released a public Graph API with OAuth2 support in June 2024.
   * *Lesson:* Active web verification is necessary to correct outdated training cutoffs.
5. **Sherlock (#58) & Mermaid CLI (#98):**
   * *Pass 1 Claim:* Cloud REST API with Bearer token authentication.
   * *Ground Truth:* Both are open-source command-line tools that run locally. Neither uses authentication.
   * *Lesson:* CLI tools must run in local container environments, not HTTP clients.
6. **fanbasis (#50 - Ecommerce):**
   * *Pass 1 Claim:* Blocked; consumer creator platform with no developer surface.
   * *Ground Truth:* Fanbasis provides an embedded checkout SDK on npm (`@fanbasis/checkout-sdk`) and documentation at `dev-docs.fanbasis.com`.
   * *Lesson:* Rebranded platforms often place developer documentation on dedicated subdomains.

---

## 6. How to Run the Research Agent and Verification Scripts

### Requirements
* Python 3.9 or higher (standard library only; no external package requirements).

### Run Commands

```bash
# 1. Profile a specific application (e.g. App #10 DealCloud or #91 NotebookLM)
python3 agent/research_pipeline.py --app-id 10
python3 agent/research_pipeline.py --app-id 91

# 2. Filter research by category
python3 agent/research_pipeline.py --category Fintech

# 3. Print macro distribution metrics
python3 agent/research_pipeline.py --summary

# 4. Actively check live reachability of docs URLs (HTTP HEAD/GET probes)
python3 agent/research_pipeline.py --verify-links --sample 10

# 5. Run schema integrity check and verification accuracy benchmark
python3 agent/verifier.py

# 6. Recompile the interactive HTML dashboard
python3 generate_html.py

# 7. Open the dashboard locally
open index.html
```

---

## 7. Repository File Structure

```
.
├── index.html                   # Interactive Case Study Dashboard (Anti-slop, STE-100)
├── README.md                    # Technical Research Report (STE-100)
├── requirements.txt             # Workspace dependencies
├── build_dataset.py             # Master Dataset Generator & Auditor
├── generate_html.py             # Dashboard Compiler & Batching Controller
├── agent/
│   ├── research_pipeline.py     # Research Profiling & Live Link CLI
│   ├── verifier.py              # Schema Integrity & Accuracy Benchmark
│   ├── analyzer.py              # Statistical Pattern Mining Script
│   └── requirements.txt         # Package Notes
└── data/
    ├── apps_100.json            # Verified 100-App Dataset (JSON)
    ├── apps_100.csv             # Verified 100-App Dataset (CSV)
    ├── patterns_summary.json    # Statistical Pattern Distributions
    └── verification_audit.json  # Verification Progression & Discrepancy Logs
```

---

## 8. Deliverable Submission Links

* **Live Deployed HTML Page / Case Study:** [https://pushpam2404.github.io/composio-product-ops-takehome/](https://pushpam2404.github.io/composio-product-ops-takehome/)
* **GitHub Source Repository:** [https://github.com/pushpam2404/composio-product-ops-takehome](https://github.com/pushpam2404/composio-product-ops-takehome)
