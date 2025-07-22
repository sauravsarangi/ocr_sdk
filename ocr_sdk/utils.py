from PIL import Image
import os
from .exceptions import ImageNotFoundError

def load_image(image_path):
    if not os.path.exists(image_path):
        raise ImageNotFoundError(f"Image not found: {image_path}")
    return Image.open(image_path)
