# Write the contest reply as one UTF-8 line with a trailing newline.
import os
from pathlib import Path


TEXT = "Good news, I found your backup. If you zoom in, you can read most of the filenames."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
