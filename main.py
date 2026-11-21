"""Entry for make.fun bounty: the joke the reviewer laughs at.

Writes one joke about working beside AI coding agents to /output/entry.txt.
"""

from pathlib import Path

JOKE = (
    "My agent called it a 'minor refactor' — 47 files changed, a new "
    "framework, and my one helper function now has its own microservice "
    "and a therapist."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
