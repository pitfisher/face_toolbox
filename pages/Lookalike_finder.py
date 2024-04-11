"""face lookalike search page"""

import os
import streamlit as st
import pandas as pd
import numpy as np
from deepface import DeepFace
from PIL import Image, ImageOps
import settings

if os.path.exists(settings.face_db_names):
    df_names = pd.read_csv(settings.face_db_names)
else:
    st.write("Faces DB file doesn't exist! Put in a correct path on Settings page")

def find_lookalikes():
    """Function that implements streamlit page to search fro a given photo 3 lookalikes from a pre-loaded face images DB"""
    image_file = st.sidebar.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg', 'JPEG', 'JPG', 'PNG'])
    if not image_file:
        return None

    original_image = Image.open(image_file)
    original_image = ImageOps.exif_transpose(original_image)
    original_image_np = np.asarray(original_image)

    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image(original_image, caption="", width = 296)
    dfs = DeepFace.find(img_path = original_image_np, 
                        db_path = r"C:\Users\HYPERPC\Documents\miem_lookalike\photo_staff", 
                        model_name='Facenet', 
                        threshold=1.5, 
                        detector_backend='mediapipe')
    print(dfs[0]['identity'])
    lookalikes = []
    lookalikes_names = []
    for i in range(min(len(dfs[0].index), 3)):
        print(f"identity: {dfs[0].iloc[i]['identity']}")
        filename = dfs[0].iloc[i]['identity'].split("\\")[-1]
        print(filename)
        id = int(filename.split('_')[0])
        lookalikes.append(Image.open(dfs[0].iloc[i]["identity"]))
        name = df_names.loc[df_names['id'] == id]['name'].item()
        lookalikes_names.append(name)
    columns = []
    columns = st.columns(3)
    # st.text("Обнаруженные люди")
    for column, i in zip(columns, range(min(len(dfs[0].index), 3))):
        column.image(lookalikes[i], caption = lookalikes_names[i], width = 296)

find_lookalikes()
