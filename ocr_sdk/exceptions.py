class OCRSDKError(Exception):
    """Base class for OCR SDK errors."""
    pass

class ImageNotFoundError(OCRSDKError):
    """Raised when the input image is not found."""
    pass

class OCRProcessingError(OCRSDKError):
    """Raised when OCR fails unexpectedly."""
    pass
