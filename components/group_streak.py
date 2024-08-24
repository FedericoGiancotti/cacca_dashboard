import streamlit as st
import pandas as pd 

def group_streak(df):
    st.header('Giorni consecutivi in cui tutti abbiamo cagato')
    df['day'] = df['timestamp'].dt.date
    df = df[['name', 'day']].drop_duplicates()
    df['day'] = pd.to_datetime(df['day'])
    df['day_diff'] = df.groupby('name')['day'].diff().dt.days.fillna(1)
    df['new_streak'] = df['day_diff'] > 1
    df['streak_id'] = df.groupby('name')['new_streak'].cumsum()
    streaks = df.groupby(['name', 'streak_id']).agg(
        name=('name', 'first'),
        starting_date=('day', 'min'), 
        current_streak=('day', 'count')
    ).reset_index(drop=True)
    current_streak = streaks['current_streak'].min()
    st.write(f'Current streak di giorni in cui tutti abbiamo cagato: {current_streak} giorni')