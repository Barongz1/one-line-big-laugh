"""One Line, Big Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The joke: the toaster knows too much and chooses silence.
TEXT = "My toaster has seen things. It just refuses to talk about them, and honestly, neither should you."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
