import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=500)

with col2:
    st.title("Anung")
    content = """
    Hi, I am Anung! I am a Python programmer, student, and founder of PythonHow. 
    """
    st.info(content)