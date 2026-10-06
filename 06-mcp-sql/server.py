import sqlite3
from pathlib import Path
from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("superstore-sql")

# Absolute path, so it works no matter where the server gets launched from
DB_PATH = Path(__file__).resolve().parent / "superstore.db"
# mode=ro opens the database read-only at the database level
DB_URI = DB_PATH.as_uri() + "?mode=ro"


@mcp.tool()
def get_schema() -> str:
    """Return the column names and types of the 'orders' table. Call this first
    to learn what data is available before writing any SQL query."""
    conn = sqlite3.connect(DB_URI, uri=True)
    try:
        rows = conn.execute("PRAGMA table_info(orders)").fetchall()
        return "\n".join(f"{r[1]} ({r[2]})" for r in rows)
    finally:
        conn.close()


@mcp.tool()
def run_query(sql: str) -> str:
    """Run a read-only SQL SELECT query against the 'orders' table and return up
    to 100 rows as JSON. Only SELECT statements are allowed."""
    if not sql.strip().lower().startswith(("select", "with")):
        return "Error: only SELECT queries are allowed."

    conn = sqlite3.connect(DB_URI, uri=True)
    conn.row_factory = sqlite3.Row
    try:
        rows = conn.execute(sql).fetchmany(100)
        return json.dumps([dict(r) for r in rows], indent=2)
    except sqlite3.Error as e:
        # Return the error as text so an agent can read it and fix its query
        return f"SQL error: {e}"
    finally:
        conn.close()


if __name__ == "__main__":
    mcp.run()