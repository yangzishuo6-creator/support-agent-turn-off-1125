# Write one UTF-8 contest reply with a trailing newline. Keep the file under 200 characters.
import os
from pathlib import Path


TEXT = "Thanks for holding. Has it fixed itself, or should I put the music back on?"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
