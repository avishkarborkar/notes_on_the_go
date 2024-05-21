import streamlit as st
from PIL import Image
import pytesseract
import cv2
import tempfile
import numpy as np

def get_text_from_image(image_file):
    if image_file is None:  # Handle empty image
        return None
    if isinstance(image_file, str):  # Check if it's a file path (uploaded image)
        cv_image = cv2.imread(image_file)
    else:  # Assume it's captured image data (from get_camera_input)
        cv_image = cv2.imdecode(np.frombuffer(image_file.get_read_data(), np.uint8), cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    found_text = pytesseract.image_to_string(img_rgb)
    return found_text