# ICONIC Agent Launch — November 1, 2026
Service landing page: `agent-launch/index.html`
Demonstration MCP: `agent-launch/mcp-demo/server.py`

## What this is
A proposed ICONIC service offering and a **read-only, fixture-backed** remote MCP demo.
It is not connected to Elk Grove Buick GMC, VinSolutions, vAuto, or a live appointment system.
No Google submission, publication, hosting, or marketplace approval is implied.

## Test locally
```bash
cd agent-launch/mcp-demo
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python server.py
```
MCP endpoint: `http://localhost:8000/mcp`.
Test with `npx @modelcontextprotocol/inspector` and the streamable-HTTP transport.

## Deploy
Build Docker image from `agent-launch/mcp-demo` and deploy to HTTPS hosting with `PORT` bound.
Do not expose inventory, credentials, customer records, or write tools until authorization, authentication,
rate limiting, logging, input validation, and data retention policies are implemented.
Use OAuth 2.1 and per-user consent for any private account access.
Do not claim fixture data is current.

## Google Connected Apps
1. Validate server with MCP Inspector.
2. Host on public HTTPS and test via Gemini Developer Mode.
3. Apply for Connected Apps preview and register only when admitted.
4. Document data-use, privacy, consent, schema descriptions, and tool annotations.
5. Obtain platform review before describing as available in Gemini or Search.

Reference: https://developers.google.com/connected-apps/mcp

## Commercial pilot scope
- Discovery workshop: one buyer intent and conversion action
- Read-only integration to customer-authorized product/catalog data
- Functional test suite and human approval gate for all write actions
- Verified telemetry and operational handoff
- Separate platform registration and review, subject to acceptance

## Release
Per root README, work in a feature branch, test locally, then merge through staging
and only promote to main when explicitly approved for a production release.
