import pytesseract
from .utils import load_image
from .exceptions import OCRProcessingError

class OCRClient:
    def __init__(self, tesseract_cmd=None, lang='eng'):
        """
        Initializes the OCR engine client.
        :param tesseract_cmd: Full path to tesseract executable.
        :param lang: Language(s) for OCR.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        self.lang = lang

    def extract_text(self, image_path):
        """
        Extracts text from a given image path.
        :param image_path: Path to image.
        :return: Extracted text.
        """
        try:
            image = load_image(image_path)
            return pytesseract.image_to_string(image, lang=self.lang).strip()
        except Exception as e:
            raise OCRProcessingError(f"OCR failed: {str(e)}")
