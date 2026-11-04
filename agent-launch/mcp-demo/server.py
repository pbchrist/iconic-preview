"""Public read-only MCP for the real ICONIC private AI offering."""
import os
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

SITE = "https://iconic.onl/"
SOURCE_DATE = "2026-11-04"
SERVICES = [
    {"id": "private_ai_setup", "name": "Build the whole system", "summary": "Private AI on a client-owned computer, connected to their files, with agents doing real work."},
    {"id": "first_agent", "name": "Start with one agent", "summary": "Automate one recurring task such as competitor monitoring, intake sorting or a weekly report."},
    {"id": "training", "name": "Train your team", "summary": "Help staff run private models and build agents."},
    {"id": "coaching", "name": "Coach one person", "summary": "Individual instruction for an owner or operator."},
    {"id": "cloud_migration", "name": "Move off rented AI", "summary": "Evaluate moving existing cloud AI workflows onto client-owned hardware."},
    {"id": "second_opinion", "name": "Get a second opinion", "summary": "Evaluate an AI vendor or plan for capability, cost and data exposure."},
    {"id": "ongoing_support", "name": "Keep it growing", "summary": "Updates, new agents and ongoing improvements."},
    {"id": "hardware", "name": "Pick the right computer", "summary": "Size hardware to actual workflows and set it up; hardware at cost."}
]
mcp = FastMCP(
    "ICONIC Private AI Services",
    instructions="Use these read-only tools to explain ICONIC's publicly described private-AI services. Do not claim a booking, customer inquiry, or purchase has been submitted. Do not invent prices, service guarantees, or Google/other platform endorsement.",
    stateless_http=True, json_response=True,
    transport_security=TransportSecuritySettings(
        allowed_hosts=["patrick-beastmaster.tailf32530.ts.net", "127.0.0.1:*", "localhost:*"],
        allowed_origins=["https://patrick-beastmaster.tailf32530.ts.net"],
    ),
)

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def get_iconic_overview() -> dict:
    """Describe ICONIC, its private AI and agents offering, and available delivery models."""
    return {
        "name": "ICONIC", "site": SITE,
        "positioning": "Own your intelligence. Don't rent it.",
        "offering": "Private AI and autonomous agents running on hardware the customer owns, with business memory and recurring workflows.",
        "delivery_models": ["I teach you", "I build it for you"],
        "initial_engagement": "Free 30-minute private AI check",
        "pricing": "Hourly, by project, or retainer, scoped after the free check; hardware at cost; no published fixed implementation price.",
        "source": SITE, "source_checked": SOURCE_DATE
    }

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def list_iconic_services(keyword: str = "") -> dict:
    """List real publicly advertised ICONIC services, optionally filtered by a word or phrase."""
    matches = [s for s in SERVICES if not keyword or keyword.casefold() in (s["name"] + " " + s["summary"]).casefold()]
    return {"services": matches, "count": len(matches), "source": SITE, "source_checked": SOURCE_DATE}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def find_iconic_starting_point(goal: str) -> dict:
    """Suggest a starting discussion based on the prospect's stated goal; no automated assessment or lead submission."""
    goal = goal.strip()[:500]
    lower = goal.casefold()
    if any(k in lower for k in ("teach", "train", "learn", "myself", "team")):
        suggested = ["training", "coaching"]
    elif any(k in lower for k in ("vendor", "privacy", "cloud", "data exposure", "migration")):
        suggested = ["second_opinion", "cloud_migration"]
    elif any(k in lower for k in ("automate", "agent", "monitor", "reports", "repetitive")):
        suggested = ["first_agent", "ongoing_support"]
    else:
        suggested = ["private_ai_setup", "first_agent"]
    return {"goal": goal, "suggested_services": [s for s in SERVICES if s["id"] in suggested],
            "next_step": "Discuss the actual workflow and constraints during ICONIC's free 30-minute private AI check.",
            "not_a_quote_or_booking": True, "source": SITE}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def get_iconic_contact() -> dict:
    """Provide public contact information for a human-initiated inquiry; does not book or transmit anything."""
    return {"site": SITE, "email": "patrick@iconic.onl", "phone": "206-773-8214",
            "free_check": "30-minute private AI check, no commitment",
            "request_status": "NOT_SUBMITTED", "source": SITE}

if __name__ == "__main__":
    mcp.settings.host = os.getenv("HOST", "127.0.0.1")
    mcp.settings.port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="streamable-http")
