import streamlit as st

def daily_bar_chart(df):
    st.header('Bar chart cagate al giorno gruppo')
    daily_counts = df.groupby(df['timestamp'].dt.date).size().reset_index(name='element_count')
    daily_counts['date'] = daily_counts['timestamp'].astype(str)
    daily_counts = daily_counts.drop(columns=['timestamp']).set_index('date')
    st.bar_chart(daily_counts)
