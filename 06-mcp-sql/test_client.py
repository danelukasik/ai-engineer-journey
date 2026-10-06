import asyncio
import sys
from h11 import SERVER
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pathlib import Path


async def main():
    SERVER = str(Path(__file__).resolve().parent / "server.py")
    params = StdioServerParameters(command=sys.executable, args=[SERVER])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Tools found:", [t.name for t in tools.tools])

            schema = await session.call_tool("get_schema", {})
            print(schema.content[0].text)

            result = await session.call_tool(
                "run_query",
                {"sql": "SELECT Region, ROUND(SUM(Sales), 2) AS total_sales FROM orders GROUP BY Region"},
            )
            print(result.content[0].text)

            blocked = await session.call_tool("run_query", {"sql": "WITH x AS (SELECT 1) DELETE FROM orders"})
            print(blocked.content[0].text)


asyncio.run(main())