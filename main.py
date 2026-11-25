# Write one UTF-8 line for the make.fun contest.
import os
from pathlib import Path


TEXT = "I’ve sent the repair instructions to your printer. Is it still making that grinding noise?"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
