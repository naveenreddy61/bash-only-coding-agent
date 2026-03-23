You will help in writing a coding agent that uses only bash tool as an illustration for reasoning about the internals of coding agents and th agent loop.
You will aim for self explaining code that is easy to read and skim instead of clever tricks and defensive programming.
This will not be used in prod so too many edge case handling is not needed.
We will use litellm for routing and making api calls to llm service providers.
We will use pydantic models for dealing with tool definintions and validation and usage and data models.
We will use uv tool install harbor for managing evals for terminal coding agents.
We will use `uv run main.py` to run the agent (not `uv run python main.py`).
We will tag the code at appropritate checkpoints and explain the tags in readme so that readers can checkout the code at that tag and explore the working.
