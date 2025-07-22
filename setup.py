from setuptools import setup, find_packages

setup(
    name="ocr_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "Pillow"
    ],
    author="Saurav Sarangi",
    description="A simple Python OCR SDK using Tesseract",
    python_requires='>=3.6',
)
