"""Main page of a streamlit multi-page app"""

import streamlit as st
import settings
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)

def settings_page():

    settings.face_db_names = st.text_input("Face database CSV file", r"C:\Users\HYPERPC\Documents\miem_lookalike\staff_photo.csv")
    # st.sidebar.success("Select a function from menu above")

    # df = pd.read_csv('od_models.csv')
    # st.table(df)

settings_page()
