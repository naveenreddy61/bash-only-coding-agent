"""Step 2: Same hello call, but using DSPy's declarative Signature + Predict.

Instead of manually constructing messages and parsing responses,
we define *what* we want (a Signature) and let DSPy handle the *how*.
"""

import dspy

MODEL = "gemini/gemini-3-flash-preview"

lm = dspy.LM(MODEL)
dspy.configure(lm=lm)


# A Signature is just: inputs -> outputs, described in plain English.
class UserRequest(dspy.Signature):
    """You are a helpful assistant. Respond to the user's request."""

    request: str = dspy.InputField()
    response: str = dspy.OutputField()


result = dspy.Predict(UserRequest)(request="Say hello in one sentence.")
print(result.response)
