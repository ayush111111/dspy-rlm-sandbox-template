import dspy


def word_count(text: str) -> int:
    """Count whitespace-delimited words in a string."""
    return len(text.split())


class AnalyzeContext(dspy.Signature):
    """Answer a question by programmatically exploring the supplied context."""

    context: str = dspy.InputField(desc="Large text available as a sandbox variable")
    query: str = dspy.InputField()
    answer: str = dspy.OutputField()


def build_rlm(settings):
    lm_kwargs = {}
    if settings.lm.startswith("openrouter/"):
        lm_kwargs["api_base"] = settings.openrouter_api_base
        lm_kwargs["api_key"] = settings.openrouter_api_key
    lm = dspy.LM(settings.lm, **lm_kwargs)
    dspy.configure(lm=lm)
    return dspy.RLM(
        AnalyzeContext,
        max_iters=settings.max_iters,
        max_llm_calls=settings.max_llm_calls,
        max_output_chars=settings.max_output_chars,
        tools=[word_count],
        # Default PythonInterpreter is the local Deno/Pyodide sandbox.
        interpreter_factory=dspy.PythonInterpreter,
    )
