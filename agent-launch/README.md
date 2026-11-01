# ICONIC Agent Distribution as a Service

Cross-industry agent-distribution service landing page and reusable **public fixture** MCP proof of concept. This replaces the vehicle-specific proof of concept.

## Architecture
Client business → consented data adapters and business workflows → tenant-specific permission boundary → MCP tools → compatible agent clients. ICONIC operates the infrastructure; customer end users interact with the client business, not ICONIC's scheduling system.

Current demo is intentionally **single-public-catalog only**, not a secure production multi-tenant service. Do not host private tenants or customer secrets through it.

### Demo tools
- `discover_businesses(category, keyword)`
- `get_business_services(business_id)`
- `get_action_options(business_id, service_id)` (read-only descriptive; performs no transactions)

All records in `businesses.json` are fictional, with example-domain URLs. No real inventory, offers, schedules, reservations or commerce actions are present.

## Run
```sh
cd agent-launch/mcp-demo
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python server.py
```
Local endpoint: http://127.0.0.1:8000/mcp (Streamable HTTP). Inspect via `npx @modelcontextprotocol/inspector`.

## Before production
- Isolated tenant identity and authorization, approved OAuth 2.1 flows where relevant
- Connection to business-authorized sources and explicit action schemas
- Mandatory confirmation for state changes, idempotency, transaction audit logs
- Input validation, rate limits, prompt injection defenses, redacted logs
- Health checks, tests, HTTPS endpoint, documented privacy and retention
- Per-platform compliance, eligibility and approval; no assumed organic placement

## Commercial offer
1. Agent readiness audit: buyers' intents, candidate workflows, integration effort
2. One paid pilot per client: secure catalog/knowledge and one approved transaction or inquiry workflow
3. Platform submission where eligible, plus measurement and maintenance

Client onboarding and business consultations may use ICONIC email/calendar on the **human sales website** only. MCP actions must address the client's own approved systems. No cross-tenant routing or appointment diversion.

## Release
Feature branch → staged review and tests → explicitly approved production release. Production iconic.onl remains untouched until authorized.
