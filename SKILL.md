---
description: OCR text extraction from images and PDFs via Tesseract (deu/eng/chi_sim). Use when the user asks to OCR, recognize scanned documents, or extract text from images or PDFs. 通过 Tesseract 从图片/PDF 提取文字（德语/英语/中文），用于 OCR、识别扫描件。
allowed-tools: Bash(python *) Bash(python3 *)
---

Extract text from images and scanned PDFs. Requires a local Tesseract installation with deu / eng / chi_sim language packs (see README).

## Single image

```
python "${CLAUDE_SKILL_DIR}/scripts/ocr.py" <image-path> [lang]
```

Default language `deu+eng+chi_sim`; override with e.g. `eng`, `deu`, `chi_sim`. Outputs plain text.

## PDF (recommended, auto-detects image pages)

```
python "${CLAUDE_SKILL_DIR}/scripts/pdf_ocr.py" <pdf-path> [-o output.md] [--lang eng] [--force]
```

Page-by-page detection: pages with < 50 characters are treated as image-based and OCR'd; text pages are extracted directly. Each page is tagged `[Text]` or `[OCR]`.

## Notes

- Quote paths that contain spaces.
- Use `pdf_ocr.py` for scanned PDFs, `ocr.py` for single screenshots/photos.
- Plain-text PDFs need no OCR — read them directly.
- Output may mix DE / EN / CN; report it verbatim, do not guess or "fix" the recognized text.

---

从图片或扫描 PDF 提取文字。需要本机已安装 Tesseract 引擎及 deu / eng / chi_sim 语言包（见 README）。

## 单张图片

```
python "${CLAUDE_SKILL_DIR}/scripts/ocr.py" <图片路径> [lang]
```

默认语言 `deu+eng+chi_sim`，可指定如 `eng`、`deu`、`chi_sim`。输出纯文本。

## PDF（推荐，自动识别图片页）

```
python "${CLAUDE_SKILL_DIR}/scripts/pdf_ocr.py" <pdf路径> [-o 输出.md] [--lang eng] [--force]
```

逐页检测：文字量 < 50 字符判定为图片页，仅对这些页跑 OCR；纯文字页直接提取。每页标注 `[Text]` 或 `[OCR]`。

## 要点

- 路径含空格务必加引号。
- 扫描件 PDF 用 `pdf_ocr.py`，单张截图/照片用 `ocr.py`。
- 纯文本 PDF 无需 OCR，直接读取即可。
- 输出可能 DE / EN / CN 混合，按原文如实报告，不要臆改识别结果。
