import streamlit as st
from components.file_uploader import file_uploader
from components.load_data import load_data
from components.total_leaderboard import total_leaderboard
from components.weekly_leaderboard import weekly_leaderboard
from components.monthly_leaderboard import monthly_leaderboard
from components.total_cacca_counter import total_cacca_counter
from components.daily_bar_chart import daily_bar_chart
from components.cumulative_line_chart import cumulative_line_chart
from components.distribution_pie_chart import distribution_pie_chart
from components.hourly_distribution_bar_chart import hourly_distribution_bar_chart
from components.streaks import streaks
from components.records import records
from components.group_streak import group_streak

st.set_page_config(page_title="Cacca Dashboard", 
                   page_icon="image.png", 
                   layout="wide", 
                   initial_sidebar_state="collapsed", 
                   menu_items=None)

st.title('💩 Cacca Dashboard')
st.write('Dashboard per analizzare i dati di quanto il gruppo Kafèèè caga al giorno')

file = st.file_uploader('Upload your chat file', type='txt')

if file is not None:
    df = load_data(file)
    daily_counts = df.groupby(['day', 'name']).size().reset_index(name='element_count')
    weekly_counts = df.groupby(['week', 'name']).size().reset_index(name='element_count')
    monthly_counts = df.groupby(['month', 'name']).size().reset_index(name='element_count')  
    records(df, daily_counts, weekly_counts, monthly_counts)
    total_cacca_counter(df)
    total_leaderboard(df)
    weekly_leaderboard(df)
    monthly_leaderboard(df)
    daily_bar_chart(df)
    cumulative_line_chart(df)
    distribution_pie_chart(df)
    hourly_distribution_bar_chart(df)
    streaks(df)    
    group_streak(df)
    st.header('Tabella dei dati')
    st.write(df)
else:
    st.warning('Please upload a chat file to continue.')
