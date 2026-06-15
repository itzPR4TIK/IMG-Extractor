# 📄 PDF → Images

A minimalist web tool that converts PDF pages into high‑quality PNG images and bundles them into a ZIP archive. Built with Flask and PyMuPDF, featuring a drag‑and‑drop interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- **Drag & drop** – simply drop a PDF on the page
- **Instant conversion** – every page becomes a crisp PNG (200 DPI)
- **ZIP download** – all images are packed into a single file
- **In‑memory processing** – no temporary files, no clutter
- **Modern UI** – clean, minimal, and responsive design
- **Client‑side validation** – rejects non‑PDFs and files >50 MB

## 🚀 Quick start

### Prerequisites

- Python 3.7 or higher
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. Clone or download this repository.
2. Install the dependencies:

```bash
pip install flask pymupdf
