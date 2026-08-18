#!/usr/bin/env python3
"""Paper Trail — real mini-challenge (paper-trail)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'author-field')


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "paper-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    pdf_meta = (
        "=== paper.pdf.txt (metadata dump) ===\n"
        "Title: Quarterly Threat Briefing\n"
        f"Author: {key}\n"
        "Creator: LaTeX with hyperref\n"
        "Producer: pdfTeX\n"
        "Keywords: osint, leak, author-field\n"
    )
    with open("/challenge/paper.pdf.txt", "w") as fh:
        fh.write(pdf_meta)
    print("Paper Trail — Author field in paper.pdf.txt is the key.")


if __name__ == "__main__":
    main()
