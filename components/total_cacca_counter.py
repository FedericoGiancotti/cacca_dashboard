import streamlit as st

def total_cacca_counter(df):
    st.header('Cagate totali del gruppo')
    total_cacca = df.shape[0]
    st.write(f'Total cagate: {total_cacca}')
