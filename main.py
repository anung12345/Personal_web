import streamlit as st
import pandas

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

content2 = """
Below you can find some apps i have built in Python
"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])