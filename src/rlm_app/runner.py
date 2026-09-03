import json
from pathlib import Path

from .program import build_rlm


def run(path: Path, query: str, settings, output_path: Path = Path("runs/last.json")):
    context = path.read_text(encoding="utf-8")
    result = build_rlm(settings)(context=context, query=query)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps({
        "answer": result.answer,
        "trajectory": getattr(result, "trajectory", []),
        "final_reasoning": getattr(result, "final_reasoning", None),
    }, indent=2, default=str), encoding="utf-8")
    return result.answer
