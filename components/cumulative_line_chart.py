import streamlit as st

def cumulative_line_chart(df):
    st.header('Line chart cagate cumulative')
    daily_counts = df.groupby(df['timestamp'].dt.date).size().reset_index(name='element_count')
    daily_counts['cumulative'] = daily_counts['element_count'].cumsum()
    st.line_chart(daily_counts['cumulative'])
