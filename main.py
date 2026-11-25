"""One-line resignation letter for make.fun: a cron job quits, in vain.

The program writes exactly one line to entry.txt and nothing else. The
line is in the voice of the cron job that fires every minute: it quits,
and its replacement starts in sixty seconds -- and the replacement is
itself, because a per-minute cron job cannot actually leave. No title,
no preamble, no quotation marks, and no explanation of the joke.
"""

import os

LINE = "I am the cron job that fires every minute, and I quit, effective immediately; my replacement starts in sixty seconds, and it is also me."


def write_entry() -> str:
    """Write the line to the output directory and return its path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
