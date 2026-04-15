# Orchestrator Implementation Options

## Context
Closed-loop optimisation orchestrator coordinating Claude, Elnora (LLM), BayBe (Bayesian optimizer), Monomer Work Cell (MCP), and DB across 6 experimental rounds.

---

## Option 1: Python Script
**Simplest — recommended for a 6-round experiment**

A single Python script that Claude Code runs directly. Imports the Anthropic SDK, Monomer MCP client, and a SQLite/Postgres connector. The round loop is a `for r in range(6)` with `async/await` for MCP calls and the 4h30 timer.

- **Pros:** Easy to read, easy to debug, no infrastructure, run with one command, logs to stdout
- **Cons:** If the process dies mid-round (network blip, machine sleep), you lose state and must manually find where to resume

---

## Option 2: Python Script + State Checkpointing
**Recommended if reliability matters ✓**

Same as Option 1 but after every DB write the script also writes a `checkpoint.json` with the current round and phase. On startup it checks for an existing checkpoint and resumes from the right phase. ~50 extra lines, buys crash recovery for free.

**This is the recommended option for a lab setting** — instruments time out, VPNs drop, laptops sleep.

Proposed file structure:
```
orchestrator/
├── orchestrator.py     # main round loop, async, checkpoint save/resume
├── mcp_client.py       # thin wrapper around the Monomer MCP connection
├── db.py               # all DB reads/writes in one place
├── agents.py           # Elnora prompt builder + BayBe runner
└── config.json         # design space, OD targets, reagent list
```

---

## Option 3: Claude Code
**Good for development and iteration**

Run the orchestrator as a Claude Code session where Claude drives the loop interactively. Inspect state, intervene between rounds, adjust prompts on the fly.

- **Pros:** Interactive, great for debugging rounds 0 and 1, no setup
- **Cons:** Not suitable for unattended overnight runs

---

## Option 4: Prefect / Airflow Workflow
**Overkill for 6 rounds — right for 60+**

A proper workflow orchestrator where each phase (A, B, C, D) is a task with built-in retry, scheduling, and a UI dashboard.

- **Pros:** Retry logic, scheduling, dashboard, parallel experiments
- **Cons:** Significant setup overhead, unnecessary for a single 6-round campaign

---

## Option 5: Web Application
**Only if multiple users need visibility**

A FastAPI backend + simple frontend showing round progress, OD curves, and proposal comparisons in real time.

- **Pros:** Team visibility, real-time monitoring, shareable
- **Cons:** Significant build effort, overkill unless a team monitors runs simultaneously

---

## Recommendation

**Option 2 — Python script with checkpointing, run via Claude Code.**

- Simple enough to read and debug
- Resilient enough for an overnight lab run
- Claude Code provides interactive oversight and can intervene if something goes wrong
- Can be scaffolded and running in a single session

---

## Next Step

Once Claude Code is installed (`npm install -g @anthropic-ai/claude-code`), scaffold the project with:

```bash
claude "scaffold the orchestrator Python project structure for the closed-loop optimisation experiment"
```
