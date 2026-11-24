"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it,
in 120 characters or fewer, to /output/entry.txt.

The line is a fixed string written by the author of this entry.
The joke is driven by the plant's own life: it has not been watered
since March, so its roots have unionised, and the dust on the shelf
is now its emergency contact. The office frame ("Out of office",
"Last drink", "emergency contact") carries the punchline.
"""

import os

ENTRY = (
    "Out of office until someone waters me. "
    "Last drink: March. "
    "My roots have unionised \u2014 the dust is my emergency contact."
)

# The gate refuses anything over 120 characters, so enforce the cap here
# rather than discovering it on the server.
assert 1 <= len(ENTRY) <= 120, "entry line must be 1-120 characters"


def main():
    # The competition's output path; MAKEFUN_OUTPUT only exists so the
    # entry can be verified locally without touching the shared /output.
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
