A repository capturing my progress learning Python and how to build AI Agents roughly following the following curriculum:

STEP 1: Python Fundamentals 

Resource path: Scrimba's interactive Learn Python course first (fast, hands-on), then Automate the Boring Stuff for practical projects, then CS50P for depth 
Scrimba
 — don't skip straight to CS50P, its pace is academic and can stall beginners who need momentum early.

Order of topics, in sequence — don't skip ahead until each is solid:

Variables, data types, string formatting (f-strings specifically — you'll use these constantly later)
Control flow: if/else, loops, list/dict comprehensions
Functions: arguments, return values, default params, *args/**kwargs
Data structures: lists, dicts, sets, tuples — go deep here, agent code passes dicts and JSON constantly
Object-oriented programming: classes, inheritance, __init__, methods. Don't use any course that skips OOP entirely — modern Python codebases use classes heavily, and agent frameworks are built almost entirely out of classes. 
Scrimba
File I/O and working with JSON (json.load/dumps) — this is exactly the shape of data agents pass around
Error handling: try/except, raising custom exceptions
pandas basics: DataFrames, filtering, groupby — leans directly on your SQL intuition

Checkpoint project: rewrite one of your existing dashboards as a Python script — pull data from a CSV or public API, clean it with pandas, output a chart. Commit it to GitHub.

STEP 2: Software Engineering Basics
Git properly: branches, .gitignore, meaningful commits, pull requests (even solo — practice the workflow)
Virtual environments (venv) and requirements.txt — every project gets its own
Calling REST APIs with requests: GET/POST, headers, auth tokens, handling errors — this is the single most important skill for what's coming, since agents are fundamentally "call an API, parse the result, decide next step"
Basic pytest: write tests for 2–3 of your earlier functions
Async basics (async/await) — skim this now, you'll need it for LangGraph later

Checkpoint project: a script that calls a free public API (weather, stock price, whatever), handles a failed request gracefully, and logs the result to a file.

STEP 3: LLM APIs & Prompting 
Get API keys for Anthropic and OpenAI (free tier/small credit is enough)
Make your first raw API call in Python — no framework, just requests or the anthropic SDK
System prompts vs user prompts — how they shape behavior
Function/tool calling — this is the actual mechanical foundation of every agent. Learn: how you define a tool schema, how the model "chooses" to call it, how you execute it and return the result
Structured outputs (getting reliable JSON back from the model)
Few-shot prompting and basic eval thinking (how do you know if a prompt is "good"?)

Checkpoint project: a CLI tool that takes a CSV, lets you ask natural-language questions about it, and the model calls a "run_pandas_query" tool you've defined to answer. This is your first real taste of agentic behavior, and it directly reuses your data background.

STEP 4: RAG & Vector Databases 
What embeddings are, conceptually (a vector representing meaning)
Pick one vector DB to start — Qdrant or ChromaDB (Chroma installs locally in one line, zero setup friction, best for learning)
Build the RAG loop by hand: chunk documents → embed → store → retrieve top-k → stuff into prompt → generate
Learn why naive RAG fails (bad chunking, irrelevant retrieval) before reaching for a framework to paper over it

Checkpoint project: RAG chatbot over a real document set — your own company's internal docs, or public SEC filings, or product documentation. Ship it as a simple Streamlit or Gradio app so it's demoable, not just a notebook.

STEP 5: MCP — Your Bridge Project 

This is where your SQL background becomes a genuine unlock. Build an MCP server from scratch in Python that lets Claude Desktop safely query a local SQLite database 
Medium
 — the FastMCP library makes this straightforward, and starting with a database-connected server is one of the highest-value first builds since MCP has become the standard way agents connect to tools and data in 2026. 
Fungies

Steps:

Read through Anthropic's official MCP quickstart docs
Build a "SQLite Inspector" MCP server (follow the pattern above) using a sample database
Swap the sample DB for something closer to real BI data — e.g., a Snowflake sandbox or a Postgres instance loaded with sample sales data
Connect it to Claude Desktop and actually use it to answer business questions conversationally

Checkpoint project: this MCP server is your first "Agentic Analytics" portfolio piece — natural language in, SQL query out, real answer back.

STEP 6: LangGraph

Start with LangChain Academy — a free, structured course specifically for learning LangGraph basics, 
GitHub
 then Real Python's LangGraph tutorial for a full worked example. 
Real Python

Order of concepts:

StateGraph — the core abstraction: nodes as functions, edges as transitions
Conditional edges (branching logic — "if the agent needs a tool, go here; if done, go there")
Checkpointing/memory — in-memory MemorySaver for development, then a database-backed checkpointer like SQLite or Postgres for anything persistent 
Cowork
Human-in-the-loop nodes (a pause-for-approval step — critical for anything touching real data or real actions)
Multi-agent patterns: subgraphs, supervisor/worker patterns

Checkpoint project: extend your MCP/SQL project into a full LangGraph agent — one node plans the query, one executes it via your MCP server, one writes a plain-English summary, with a human-approval step before anything "sends."

STEP 7: Production Skills
Add Langfuse (free tier) for tracing — see every step your agent takes
Build a small eval set: 10–15 test questions with expected answers, script that checks your agent against them
Add basic guardrails — scope limits on what the SQL agent is allowed to query/modify (read-only by default)
Deploy one project somewhere real — a small cloud VM, Render, or Fly.io — so it's a live link, not just local code
