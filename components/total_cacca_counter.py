import streamlit as st

def total_cacca_counter(df):
    st.header('Counter cagate totali gruppo')
    total_cacca = df.shape[0]
    st.write(f'Total cagate: {total_cacca}')
