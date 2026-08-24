#!/usr/bin/env python3
"""OCR text extraction from images.

Tesseract is located via (in order):
  1. TESSERACT_CMD env var
  2. `tesseract` on PATH
  3. common install locations
"""

import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

import pytesseract
from PIL import Image

DEFAULT_LANG = os.environ.get("OCR_LANG", "deu+eng+chi_sim")


def find_tesseract() -> str:
    if os.environ.get("TESSERACT_CMD"):
        return os.environ["TESSERACT_CMD"]
    found = shutil.which("tesseract")
    if found:
        return found
    candidates = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        "/usr/bin/tesseract",
        "/usr/local/bin/tesseract",
        "/opt/homebrew/bin/tesseract",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return "tesseract"


pytesseract.pytesseract.tesseract_cmd = find_tesseract()


def ocr(image_path: str, lang: str = DEFAULT_LANG) -> str:
    """Extract text from an image file. Returns the text string."""
    img = Image.open(image_path)
    return pytesseract.image_to_string(img, lang=lang)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python ocr.py <image_path> [lang]")
        print(f"Default lang: {DEFAULT_LANG}")
        sys.exit(1)

    path = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_LANG

    try:
        print(ocr(path, lang))
    except Exception as e:
        print(f"OCR error: {e}", file=sys.stderr)
        sys.exit(1)
