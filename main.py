"""Main page of a streamlit multi-page app"""

import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)


def run():
    """Main function launching streamlit multi-page app"""
    st.set_page_config(
        page_title="Face toolbox",
        page_icon="??",
        layout="wide",
    )

    st.write("# ")

    st.sidebar.success("Select a function from menu above")

    # df = pd.read_csv('od_models.csv')
    # st.table(df)

if __name__ == "__main__":
    run()
