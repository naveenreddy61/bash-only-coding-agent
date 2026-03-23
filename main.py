"""Step 1: Simple LLM call using LiteLLM to route to Gemini."""

import litellm

MODEL = "gemini/gemini-3-flash-preview"

response = litellm.completion(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)

print(response.choices[0].message.content)
