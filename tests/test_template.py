from pathlib import Path

from rlm_app.config import Settings
from rlm_app.program import word_count


def test_word_count_tool_is_deterministic():
    assert word_count("one two three") == 3


def test_sample_input_is_utf8_text():
    sample = Path(__file__).parents[1] / "sample_data" / "incident.log"
    assert "CRITICAL" in sample.read_text(encoding="utf-8")


def test_defaults_are_bounded():
    settings = Settings()
    assert 0 < settings.max_iters <= 100
    assert 0 < settings.max_llm_calls <= 500
    assert settings.max_output_chars > 0
