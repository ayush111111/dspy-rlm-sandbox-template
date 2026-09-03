import argparse
from pathlib import Path

from .config import Settings
from .runner import run


def main():
    parser = argparse.ArgumentParser(description="Ask a DSPy RLM about a text file")
    parser.add_argument("--file", type=Path, required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--trajectory", type=Path, default=Path("runs/last.json"))
    args = parser.parse_args()
    if not args.file.is_file():
        parser.error(f"input file does not exist: {args.file}")
    print(run(args.file, args.query, Settings(), args.trajectory))


if __name__ == "__main__":
    main()
