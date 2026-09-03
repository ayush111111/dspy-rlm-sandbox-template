from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


def _int(name: str, default: int) -> int:
    value = os.getenv(name)
    return int(value) if value else default


@dataclass(frozen=True)
class Settings:
    lm: str = os.getenv("RLM_LM", "openrouter/openai/gpt-4o-mini")
    openrouter_api_key: str = os.getenv("OPENROUTER_API_KEY", "")
    openrouter_api_base: str = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
    max_iters: int = _int("RLM_MAX_ITERS", 8)
    max_llm_calls: int = _int("RLM_MAX_LLM_CALLS", 20)
    max_output_chars: int = _int("RLM_MAX_OUTPUT_CHARS", 6000)
