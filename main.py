# from ocr_sdk import OCRClient, OCRProcessingError

# ocr = OCRClient(tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe")

# try:
#     text = ocr.extract_text("stock_gs200.png")
#     print("Extracted Text:\n", text)
# except OCRProcessingError as e:
#     print("OCR Error:", e)

from ocr_sdk import OCRClient, OCRProcessingError
import os

# Set path to the Tesseract executable
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize OCR client
ocr = OCRClient(tesseract_cmd=tesseract_path, lang='eng')

# Input image file
image_path = "stock_gs200.png"

# Output text file (same name as image, with .txt extension)
output_text_path = os.path.splitext(image_path)[0] + ".txt"

try:
    # Extract text from image
    result = ocr.extract_text(image_path)

    # Save to text file
    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✅ OCR text saved to {output_text_path}")

except OCRProcessingError as e:
    print("❌ OCR Error:", e)
