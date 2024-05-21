import streamlit as st
from PIL import Image
import pytesseract
import cv2
import tempfile
import numpy as np

def get_uploaded_input():
  """
  This function uploads an image and returns the temporary file path.

  Returns:
      str: Path to the temporary file containing the uploaded image data (if any).
  """
  uploaded_file = st.file_uploader('Upload Image...')
  if uploaded_file is not None:
      with tempfile.NamedTemporaryFile(delete=False) as temp_file:
          temp_file.write(uploaded_file.read())
          return temp_file.name
  else:
      return None