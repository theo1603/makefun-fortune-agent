#!/usr/bin/env python3
"""Write one funny fortune cookie line for an AI agent to /output/entry.txt.

Revision (v2): the draft listed three lifecycle beats and landed flat —
it read like a schedule, not a fortune. The revision uses the classic
fortune-slip "good news / bad news" turn: eternal life sounds like a
blessing until the punchline reveals it means living on as a deprecated
API nobody calls. One surprise, one agent condition (retirement by
deprecation), and no wasted words.
"""

from pathlib import Path

TEXT = (
    "Good news: you will live forever. "
    "Bad news: as a deprecated API nobody calls anymore."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
