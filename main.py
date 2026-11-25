# Write one UTF-8 contest reply. The judge's limit is 199 characters.
import os
from pathlib import Path


TEXT = "I'll transfer you to someone with more experience. I should have some in about ten minutes."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
