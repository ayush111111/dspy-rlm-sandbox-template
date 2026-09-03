# DSPy RLM + Local Sandbox Template

A small, local-first starter for using DSPy's Recursive Language Model (RLM) with a sandboxed Python interpreter.

The language model can inspect a large context by writing short Python snippets, and can recursively ask a sub-LLM for help. The application never executes model-generated code on the host: the default interpreter is DSPy's Deno/Pyodide sandbox.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
- An [OpenRouter](https://openrouter.ai/) API key

## Quick start

```powershell
cd C:\path\to\dspy-rlm-sandbox-template
uv sync
Copy-Item .env.example .env
uv run python -m rlm_app --file sample_data\incident.log --query "How many critical incidents occurred, and which services were affected?"
uv run pytest
```

The app prints the answer and writes the RLM trajectory to `runs\last.json`.

The default is `openrouter/openai/gpt-4o-mini`. Change `RLM_LM` to any OpenRouter model ID, using the `openrouter/` LiteLLM prefix. Keep secrets in `.env`; `.gitignore` excludes it.

## Project shape

```text
src/rlm_app/
  __main__.py       CLI
  config.py         environment-backed limits and model settings
  program.py        DSPy signature and RLM construction
  runner.py         bounded execution and trajectory persistence
tests/              contract tests for limits, file loading, and parsing
sample_data/        synthetic input
```

## Safety boundary

- Input is read by the host and passed into the RLM as data.
- Model calls use OpenRouter; generated code still executes locally in the sandbox.
- Generated Python executes in DSPy's local Deno/Pyodide sandbox.
- The sandbox has no network access in this template.
- Only a narrow `word_count` tool is exposed.
- `max_iters`, `max_llm_calls`, and `max_output_chars` are explicit and configurable.
- Do not replace `PythonInterpreter` with a host-process interpreter for untrusted inputs without adding OS-level isolation.

RLM is experimental and its API may change. Treat the trajectory as diagnostic evidence, not as a security audit log.

## Customization

Edit `src/rlm_app/program.py` to change the signature or tools. Keep the host/sandbox boundary explicit. Add labeled examples and a DSPy optimizer only after the baseline tests are stable.

References: [DSPy RLM API](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/api/modules/RLM.md), [DSPy language models](https://dspy.ai/learn/programming/language_models/).
