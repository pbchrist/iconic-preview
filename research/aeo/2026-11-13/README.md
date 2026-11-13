# ICONIC competitor landscape and ChatGPT citation benchmark

**Snapshot date:** 2026-11-13.

Source of truth: [ICONIC — Competitor Landscape & Citation Grid](https://docs.google.com/spreadsheets/d/1CfoN-M59SZLH5vD-Zken70xiEcL5VGEw6LmsTSTUZo4/edit).

## Contents

| File | Description |
| --- | --- |
| [`competitor-grid.csv`](competitor-grid.csv) | 97 consolidated company-level competitor and alternative records, their category, relation to ICONIC, source URLs, prompt frequency, and review priority. |
| [`source-register.csv`](source-register.csv) | 107 distinct cited domains, including reference sources and utilities that are not competitors. |
| [`30-prompt-audit.csv`](30-prompt-audit.csv) | 30 buyer-intent prompts, observed ICONIC mention/citation, cited domains and links, and answer excerpts. |
| [`market-additions.csv`](market-additions.csv) | 8 adjacent market companies not counted in the unpersonalized benchmark. |
| [`sheet-notes.csv`](sheet-notes.csv) | Data dictionary and methodology notes from the spreadsheet's Read Me tab. |

## Methodology

- On 2026-11-12 to 2026-11-13, 30 separate temporary ChatGPT conversations were run with **Unpersonalized** selected (15 private/on-premise AI, 15 automotive-dealership intelligence).
- **Baseline: 0/30** ChatGPT responses mentioned ICONIC and **0/30** directly cited `iconic.onl`. It was an immediately post-launch baseline, not a judgment of product quality.
- Counts represent distinct prompt responses in which a company/domain was linked, **not** market share, verified product quality, search rankings, or every competitor in the space.
- Company-level citation counts combine relevant subdomains (e.g., MarketCheck and CarGurus). The source register intentionally retains the raw cited domains.
- `market-additions.csv` includes separately found vendors and excludes them from the 30-prompt citation counts.
- One earlier **personalized** ChatGPT query mentioned and cited ICONIC, but that observation is deliberately excluded from the unpersonalized score.

## Website indexing at time of snapshot

- Google Search Console showed `sitemap.xml` successfully read on 2026-11-11 and 23 URLs discovered.
- The homepage was indexed. Priority crawl requests were accepted for `/ai/case-study-dealership.md`, `/agents/reserve/`, `/ai/services.md` and `/ai/pricing-engagement.md`. Requests do not guarantee indexing.

**Deployment note:** This directory is research data. It does not modify the site's application code, demo, sitemap, robots policy, or runtime.
