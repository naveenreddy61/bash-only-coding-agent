# Bash-Only Coding Agent

A minimal coding agent that uses only a bash tool — built step by step to illustrate how agent loops work under the hood.

Uses [LiteLLM](https://docs.litellm.ai/) for LLM routing and [DSPy](https://dspy.ai/) for declarative prompting.

## Setup

```bash
# clone and enter the repo
git clone https://github.com/naveenreddy61/bash-only-coding-agent.git
cd bash-only-coding-agent

# create a .env file with your API key
echo "GEMINI_API_KEY=your-key-here" > .env

# install dependencies (requires uv)
uv sync
```

## Run

```bash
uv run python main.py
```

## Tags

Checkout any tag to see the code at that stage:

```bash
git checkout v1-simple-call
```

| Tag | Description |
|-----|-------------|
| `v1-simple-call` | Minimal LiteLLM call to Gemini |
| `v2-dspy-predict` | Same call using DSPy Signature + Predict |
