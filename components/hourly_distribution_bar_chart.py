import streamlit as st

def hourly_distribution_bar_chart(df):
    st.header('Distribuzione oraria cagate del gruppo')
    hourly_counts = df['hour'].value_counts().sort_index()
    hourly_counts_df = hourly_counts.reset_index()
    hourly_counts_df.columns = ['Hour of the Day', 'Count']
    st.bar_chart(hourly_counts_df.set_index('Hour of the Day'))
