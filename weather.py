from mcp.server.fastmcp import FastMCP
import os
mcp = FastMCP("WeatherServer")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather for a location"""
    # This is where you'll later add the actual weather API call
    # For now, returning mock data
    return f"The weather in {location} is sunny"

if __name__=="__main__":
    mcp.run(transport="streamable-http")