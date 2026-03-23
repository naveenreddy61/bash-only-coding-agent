"""Step 3: Add a bash tool and wire it up with DSPy's ReAct agent.

ReAct (Reasoning + Acting) is an agent pattern where the LLM:
  1. Thinks about what to do next (Reasoning)
  2. Picks a tool and calls it (Acting)
  3. Observes the result
  4. Repeats until it has enough info to answer

We give it one tool — bash — so it can run any shell command.
DSPy's ReAct module handles the loop for us (we'll build our own in the next step).
"""

import subprocess

import dspy

# --- Configuration ---

MODEL = "gemini/gemini-3-flash-preview"
REQUEST = "What files are in the current directory? Give a brief description of each."
MAX_ITERS = 5  # max reasoning/acting cycles before the agent must answer


# --- LLM Setup ---
# LiteLLM handles routing — the "gemini/" prefix tells it to use the Google AI API.
# Credentials come from GEMINI_API_KEY in the .env file.

lm = dspy.LM(MODEL)
dspy.configure(lm=lm)


# --- Tool Definition ---
# A tool is just a Python function with type hints and a docstring.
# DSPy extracts the name, description, and parameter schema automatically
# and exposes them to the LLM so it knows what tools are available.

def bash(command: str) -> str:
    """Run a bash command and return its combined stdout and stderr output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout + result.stderr


# --- Signature ---
# A Signature declares the input/output contract for the agent.
# The docstring becomes the system-level instruction to the LLM.
# InputField/OutputField descriptions tell the LLM what each field means.

class UserRequest(dspy.Signature):
    """You are a helpful coding assistant with access to a bash tool.
    Use the bash tool to explore the environment and answer the user's request.
    """

    request: str = dspy.InputField(desc="The user's question or task")
    response: str = dspy.OutputField(desc="A clear, helpful answer based on tool results")


# --- Agent ---
# ReAct wires together the signature and tools into an agent loop.
# On each iteration it: reasons → picks a tool → observes the result.
# After max_iters (or when it decides it has enough info), it outputs the response.

agent = dspy.ReAct(
    signature=UserRequest,
    tools=[bash],
    max_iters=MAX_ITERS,
)

result = agent(request=REQUEST)
print(result.response)
