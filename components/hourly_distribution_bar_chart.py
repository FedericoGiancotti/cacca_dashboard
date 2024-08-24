import streamlit as st

def hourly_distribution_bar_chart(df):
    st.header('Bar chart distribuzione oraria cagate gruppo')
    df['hour'] = df['timestamp'].dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()
    hourly_counts_df = hourly_counts.reset_index()
    hourly_counts_df.columns = ['Hour of the Day', 'Count']
    st.bar_chart(hourly_counts_df.set_index('Hour of the Day'))
