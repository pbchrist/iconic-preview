# ICONIC MCP — real company service catalog

Read-only MCP for the public offer at https://iconic.onl/ (verified November 4, 2026).

## Tools
- get_iconic_overview: describes actual business and delivery options
- list_iconic_services: lists public offerings with optional keyword filter
- find_iconic_starting_point: suggests services based on prospect intent, not a firm recommendation or quote
- get_iconic_contact: returns public contact options, does not book or send messages

No private business data, lead capture, transaction tools or fictional catalog. The service does not promise that Gemini or Google Search will index, discover or recommend ICONIC.

## Running on Beastmaster
Code: /home/patrick/services/iconic-mcp/src/agent-launch/mcp-demo
Service: systemctl --user status iconic-mcp.service
Local MCP: http://127.0.0.1:8860/mcp
Funnel: https://patrick-beastmaster.tailf32530.ts.net/iconic-mcp/mcp

The service must run separately from other apps. External endpoint is publicly readable; don't introduce customer records or privileged tools into it without tenant isolation, OAuth and consent. Public tool descriptions and business data must stay in sync with the current website.

## Local development
```sh
cd agent-launch/mcp-demo
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python server.py
```

## Remaining
- Validate Gemini Developer Mode connection with the public endpoint
- Confirm Google's Connected Apps eligibility, application process and review
- Implement opt-in, verified customer inquiry delivery before calling it lead generation
- Add observability and a sustainable source-of-truth update process
- Treat approval, ranking, referrals and revenue as unproven until measured

Do not publish changes to the production ICONIC website without explicit approval.
