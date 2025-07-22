# ocr_sdk

`ocr_sdk` is a lightweight Python SDK for extracting text from images using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

It wraps around `pytesseract` and makes it easier to use OCR in Python applications.

---

## 📦 Features

- Extracts text from image files (e.g., PNG, JPG)
- Simple SDK-style interface
- Saves extracted text to a `.txt` file
- Powered by Tesseract OCR engine

---

## ⚙️ Installation

### Prerequisites

- [Python](https://www.python.org/downloads/) 3.6 or higher
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed and added to your system path

> On Windows, download the Tesseract installer from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki)

### Install SDK via pip from GitHub:

```bash
pip install git+https://github.com/sauravsarangi/ocr_sdk.git

