# Module 3 — Agentic AI Lab

**Dr. Dave Wanik · OPIM 5512**

This lab introduces agentic AI workflows — systems where an LLM doesn't just answer a question, but takes a sequence of actions to accomplish a goal.

---

## What is an agent?

A traditional LLM call: you send a prompt, you get a response.

An agent: the LLM decides what to *do* next — call a tool, search the web, write a file, run code — and keeps going until the task is done.

---

## Labs in this folder

| File | What it does |
|------|-------------|
| `lp_writer_agent.py` | Agent that writes linear programs given a business problem description |
| `data_etl_agent.py` | Agent that extracts structured data from unstructured text using an LLM |

---

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

You will need an API key. Create a `.env` file (never commit this!):
```
ANTHROPIC_API_KEY=your_key_here
```

---

## Key concepts

- **Tools**: functions the agent can call (search, write file, run SQL)
- **Tool loop**: the agent calls a tool → gets a result → decides next action
- **System prompt**: shapes the agent's persona and constraints
- **Stop condition**: when the agent decides it's done (or you set a max turn limit)

---

## Going further

- Claude Code (the CLI you may already be using) is itself an agent
- Multi-agent systems: one agent orchestrates others
- See Anthropic's agent docs: https://docs.anthropic.com/en/docs/agents
