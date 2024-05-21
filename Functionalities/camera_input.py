import streamlit as st
from PIL import Image
import pytesseract
import cv2
import tempfile
import numpy as np

def get_camera_input():
    captured_image = st.camera_input('Capture Image...')
    if captured_image is not None:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(captured_image.read())
            image_path = temp_file.name
            return image_path
    else:
        return None