#!/usr/bin/env python3
"""Automated PDF OCR — detects image-based pages and runs Tesseract only on those.
Usage:
    python pdf_ocr.py document.pdf              # auto-detect, output to stdout
    python pdf_ocr.py document.pdf -o out.md    # save to file
    python pdf_ocr.py document.pdf --force      # OCR every page regardless
    python pdf_ocr.py document.pdf --lang eng   # English only
"""

import io
import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

import fitz  # pymupdf
import pytesseract
from PIL import Image

TEXT_THRESHOLD = 50  # chars — pages with less text are treated as image-based
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


def page_is_image_based(page: fitz.Page, threshold: int = TEXT_THRESHOLD) -> bool:
    text = page.get_text().strip()
    return len(text) < threshold


def ocr_pixmap(pix: fitz.Pixmap, lang: str) -> str:
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    return pytesseract.image_to_string(img, lang=lang)


def pdf_ocr(pdf_path: str, lang: str = DEFAULT_LANG, force: bool = False) -> str:
    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        is_image = page_is_image_based(page)
        if force or is_image:
            pix = page.get_pixmap(dpi=300)
            text = ocr_pixmap(pix, lang)
            tag = "[OCR]" if not force else "[OCR-forced]"
        else:
            text = page.get_text()
            tag = "[Text]"

        header = f"## Page {i + 1} {tag}\n"
        pages.append(header + text.strip())

    doc.close()
    return "\n\n".join(pages)


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    pdf_path = args[0]
    lang = DEFAULT_LANG
    force = False
    output = None

    i = 1
    while i < len(args):
        if args[i] == "--lang":
            lang = args[i + 1]; i += 2
        elif args[i] == "--force":
            force = True; i += 1
        elif args[i] in ("-o", "--output"):
            output = args[i + 1]; i += 2
        else:
            print(f"Unknown flag: {args[i]}")
            sys.exit(1)

    result = pdf_ocr(pdf_path, lang=lang, force=force)

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(f"# OCR: {os.path.basename(pdf_path)}\n\n")
            f.write(result)
        print(f"Saved: {output}")
    else:
        print(result)
