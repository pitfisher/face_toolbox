"""face lookalike search page"""

import os
import streamlit as st
import pandas as pd
import numpy as np
from deepface import DeepFace
from PIL import Image, ImageOps
import settings

# if os.path.exists(settings.face_db_names):
#     df_names = pd.read_csv(settings.face_db_names)
# else:
#     st.write("Faces DB file doesn't exist! Put in a correct path on Settings page")

def compare_faces():
    """Function that implements streamlit page to comapre faces from two uploaded images"""
    left_co, right_co = st.columns(2)
    with left_co:
        image_file_1 = st.file_uploader("Upload First Image", type=['jpg', 'png', 'jpeg', 'JPEG', 'JPG', 'PNG'])
        if not image_file_1:
            st.text("No image 1!")
            return None
    with right_co:
        image_file_2 = st.file_uploader("Upload Second Image", type=['jpg', 'png', 'jpeg', 'JPEG', 'JPG', 'PNG'])
        if not image_file_2:
            st.text("No image 2!")
            return None
    
    face_image_1 = Image.open(image_file_1)
    face_image_1 = ImageOps.exif_transpose(face_image_1)
    if face_image_1.mode == 'RGBA':
        face_image_1 = face_image_1.convert('RGB')
    face_image_1_np = np.asarray(face_image_1)

    face_image_2 = Image.open(image_file_2)
    face_image_2 = ImageOps.exif_transpose(face_image_2)
    if face_image_2.mode == 'RGBA':
        face_image_2 = face_image_2.convert('RGB')
    face_image_2_np = np.asarray(face_image_2)

    # left_co, right_co = st.columns(2)
    with left_co:
        st.image(face_image_1, caption="", width = 296)
    with right_co:
        st.image(face_image_2, caption="", width = 296)

    # # debug try to get representation of a face
    # embedding_1 = DeepFace.represent(img_path = face_image_1_np)
    # print(f"Embedding of face 1: {embedding_1}")

    try:
        result = DeepFace.verify(
        img1_path = face_image_1_np,
        img2_path = face_image_2_np,
        detector_backend = "ssd",
        model_name = "Facenet",
        )
        st.text(str(result))
    except ValueError as e:
        print(f"Face not found, error message: {repr(e)}")
    except Exception as e:
        st.text(f"An error has occured, message: {repr(e)}")

compare_faces()
