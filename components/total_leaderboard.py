import streamlit as st

def total_leaderboard(df):
    st.header('Leaderboard cagate totali')
    st.write(df['name'].value_counts())
