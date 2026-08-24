# Claude Code Skill: OCR

A [Claude Code skill](https://code.claude.com/docs/en/skills) that extracts text from images and scanned PDFs via Tesseract, with built-in support for German / English / Simplified Chinese (deu + eng + chi_sim).

> 中文说明见文末 · Chinese version at the bottom.

## Features

| Script | Purpose |
|--------|---------|
| `scripts/ocr.py` | Single-image OCR |
| `scripts/pdf_ocr.py` | Smart PDF OCR: auto-detects image-based pages, runs Tesseract only on those, and extracts native text from text-based pages |

## Prerequisites

1. **Python 3.8+** with the following packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Tesseract OCR engine** with the deu / eng / chi_sim language packs:
   - Windows: [UB-Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki)
   - macOS: `brew install tesseract tesseract-lang`
   - Debian/Ubuntu: `sudo apt install tesseract-ocr tesseract-ocr-deu tesseract-ocr-chi-sim`

## Installation

Clone this repository into Claude Code's personal skills directory:

```bash
git clone <your-repo-url> ~/.claude/skills/ocr
```

(On Windows Git Bash, `~` is `C:\Users\<you>`.)

Restart Claude Code, then invoke `/ocr` or just say "OCR this PDF".

## Configuration (optional environment variables)

| Variable | Description | Default |
|----------|-------------|---------|
| `TESSERACT_CMD` | Path to the tesseract executable | Auto-detected |
| `TESSDATA_PREFIX` | Directory of language packs | Tesseract default |
| `OCR_LANG` | Default recognition language | `deu+eng+chi_sim` |

## Usage

```bash
# Single image
python scripts/ocr.py label.png             # default deu+eng+chi_sim
python scripts/ocr.py label.png eng         # English only

# Smart PDF OCR
python scripts/pdf_ocr.py scan.pdf          # print to stdout
python scripts/pdf_ocr.py scan.pdf -o out.md
python scripts/pdf_ocr.py scan.pdf --force   # force OCR every page
python scripts/pdf_ocr.py scan.pdf --lang eng
```

## Extending languages

Only deu / eng / chi_sim are enabled by default. To add more, download the matching `.traineddata` into your tessdata directory — **no code changes needed**:

```bash
curl -L -o fra.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/fra.traineddata
```

Common codes: `fra` French, `spa` Spanish, `ita` Italian, `jpn` Japanese, `kor` Korean, `rus` Russian.

> Trade-off: the more languages you combine, the slower and more memory-hungry OCR becomes. Prefer on-demand combinations (e.g. `--lang fra` or `OCR_LANG=fra`) over enabling everything.

## License

[MIT](LICENSE)

---

# Claude Code Skill: OCR（中文）

一个 Claude Code [skill](https://code.claude.com/docs/en/skills)，用 Tesseract 从图片和扫描 PDF 提取文字，支持德语 / 英语 / 中文（deu + eng + chi_sim）。

## 功能

| 脚本 | 用途 |
|------|------|
| `scripts/ocr.py` | 单张图片 OCR |
| `scripts/pdf_ocr.py` | PDF 智能 OCR：自动检测图片页，仅对图片页跑 Tesseract，纯文字页直接提取 |

## 前置依赖

1. **Python 3.8+** 及以下包：

   ```bash
   pip install -r requirements.txt
   ```

2. **Tesseract OCR 引擎**，并安装 deu / eng / chi_sim 语言包：
   - Windows: [UB-Mannheim 安装包](https://github.com/UB-Mannheim/tesseract/wiki)
   - macOS: `brew install tesseract tesseract-lang`
   - Debian/Ubuntu: `sudo apt install tesseract-ocr tesseract-ocr-deu tesseract-ocr-chi-sim`

## 安装

把本仓库克隆到 Claude Code 的个人 skills 目录：

```bash
git clone <你的仓库地址> ~/.claude/skills/ocr
```

（Windows Git Bash 中 `~` 即 `C:\Users\<你>`。）

重启 Claude Code 后，输入 `/ocr` 或直接说「OCR 这个 PDF」即可触发。

## 配置（可选环境变量）

| 变量 | 说明 | 默认 |
|------|------|------|
| `TESSERACT_CMD` | tesseract 可执行文件路径 | 自动探测 |
| `TESSDATA_PREFIX` | 语言包目录 | tesseract 默认 |
| `OCR_LANG` | 默认识别语言 | `deu+eng+chi_sim` |

## 用法

```bash
# 单图
python scripts/ocr.py label.png             # 默认 deu+eng+chi_sim
python scripts/ocr.py label.png eng         # 纯英文

# PDF 智能 OCR
python scripts/pdf_ocr.py scan.pdf          # 输出到 stdout
python scripts/pdf_ocr.py scan.pdf -o out.md
python scripts/pdf_ocr.py scan.pdf --force   # 强制全页 OCR
python scripts/pdf_ocr.py scan.pdf --lang eng
```

## 扩展语言

默认只使用 deu / eng / chi_sim。如需更多语言，下载对应 `.traineddata` 放进 tessdata 目录即可，**无需改脚本**：

```bash
curl -L -o fra.traineddata https://github.com/tesseract-ocr/tessdata/raw/main/fra.traineddata
```

常用语言代码：`fra` 法语、`spa` 西语、`ita` 意语、`jpn` 日语、`kor` 韩语、`rus` 俄语。

> 副作用：语言组合越多，OCR 越慢、内存占用越大。建议按需组合（如 `--lang fra` 或 `OCR_LANG=fra`），而非全量启用。

## License

[MIT](LICENSE)
