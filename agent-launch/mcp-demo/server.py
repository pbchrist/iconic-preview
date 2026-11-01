"""ICONIC multi-tenant agent distribution prototype. Public fixture data only."""
import os
import json
from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "ICONIC Agent Distribution Demo",
    instructions="Public demonstration only. All businesses, services and offers are fictional. No customer records, bookings, purchases, or privileged actions.",
    stateless_http=True,
    json_response=True,
)
DATA = json.loads(Path(__file__).with_name("businesses.json").read_text(encoding="utf-8"))
def public_business(b):
    return {k: b[k] for k in ("id", "name", "category", "description", "website", "capabilities")}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def discover_businesses(category: str = "", keyword: str = "") -> dict:
    """Find public business capabilities by industry/category and intent keyword. Demonstration fixtures only."""
    rows = [public_business(b) for b in DATA if
            (not category or category.casefold() in b["category"].casefold()) and
            (not keyword or keyword.casefold() in json.dumps(b).casefold())]
    return {"provenance": "FICTIONAL_DEMO_FIXTURES", "count": len(rows), "businesses": rows}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def get_business_services(business_id: str) -> dict:
    """Return public services for one business, including descriptive information. No live availability or price claims."""
    b = next((b for b in DATA if b["id"] == business_id), None)
    return {"provenance": "FICTIONAL_DEMO_FIXTURES", "business_id": business_id, "services": b["services"]} if b else {"error": "Unknown business ID"}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def get_action_options(business_id: str, service_id: str) -> dict:
    """Describe supported next steps for a service; does not collect data or execute transactions."""
    b = next((b for b in DATA if b["id"] == business_id), None)
    s = next((s for s in b["services"] if s["id"] == service_id), None) if b else None
    if not s:
        return {"error": "Unknown business or service"}
    return {"provenance": "FICTIONAL_DEMO_FIXTURES", "business_id": business_id,
            "service_id": service_id, "actions": s["actions"], "executed": False,
            "notice": "Agent integrations must connect to each tenant's authorized systems; this demo performs no actions."}

if __name__ == "__main__":
    mcp.settings.host = os.getenv("HOST", "127.0.0.1")
    mcp.settings.port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="streamable-http")
