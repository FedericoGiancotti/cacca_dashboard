import streamlit as st

def file_uploader():
    file = st.file_uploader('Upload your chat file', type='txt')
    return file
