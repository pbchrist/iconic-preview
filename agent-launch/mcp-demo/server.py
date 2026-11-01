"""ICONIC agent-commerce read-only demo. Illustrative fixtures, never live dealership data."""
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "ICONIC Automotive Agent Demo",
    instructions=(
        "This server demonstrates automotive shopping tools. All listings and offers "
        "are illustrative fixtures, not live inventory or verified prices. "
        "Never claim a vehicle is available for purchase or an appointment is booked. "
        "Do not submit customer data using these read-only tools."
    ),
    stateless_http=True,
    json_response=True,
)
VEHICLES = [
    {"id": "DEMO-1001", "year": 2026, "make": "GMC", "model": "Sierra 1500", "trim": "Elevation", "price_usd": 59995, "status": "DEMO_ONLY"},
    {"id": "DEMO-1002", "year": 2026, "make": "Buick", "model": "Enclave", "trim": "Preferred", "price_usd": 46995, "status": "DEMO_ONLY"},
    {"id": "DEMO-1003", "year": 2026, "make": "GMC", "model": "Terrain", "trim": "Elevation", "price_usd": 33995, "status": "DEMO_ONLY"},
]

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def search_demo_inventory(make: str = "", model: str = "", maximum_price_usd: int = 0) -> dict:
    """Search clearly fictional fixture inventory by optional make, model, and maximum USD price.
    Prices are demonstration numbers, not quotes. Returns an explicit DEMO_ONLY data provenance.
    """
    matches = [v for v in VEHICLES
               if (not make or make.casefold() in v["make"].casefold())
               and (not model or model.casefold() in v["model"].casefold())
               and (maximum_price_usd <= 0 or v["price_usd"] <= maximum_price_usd)]
    return {"source": "ILLUSTRATIVE_FIXTURE_NOT_LIVE", "count": len(matches), "vehicles": matches}

@mcp.tool(annotations={"readOnlyHint": True, "openWorldHint": False})
def explain_next_steps(vehicle_id: str) -> dict:
    """Explain how a shopper would request verified availability and a human appointment.
    Does not reserve a vehicle, collect PII, or schedule anything.
    """
    vehicle = next((v for v in VEHICLES if v["id"] == vehicle_id), None)
    if vehicle is None:
        return {"error": "Unknown demo vehicle ID", "booked": False}
    return {"vehicle_id": vehicle_id, "booked": False, "availability_verified": False,
            "instructions": "In production, connect dealer-approved inventory and appointment APIs; require explicit user confirmation before any write action.",
            "source": "ILLUSTRATIVE_FIXTURE_NOT_LIVE"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = port
    mcp.run(transport="streamable-http")
