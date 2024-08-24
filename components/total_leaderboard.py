import streamlit as st

def total_leaderboard(df):
    st.header('Leaderboard totale')
    st.write(df['name'].value_counts())
