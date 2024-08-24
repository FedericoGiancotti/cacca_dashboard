import streamlit as st
import pandas as pd

def streaks(df):
    st.header('Giorni consecutivi di cagate')
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
    streaks['starting_date'] = streaks['starting_date'].dt.strftime('%d/%m/%Y')
    longest_streaks = streaks.groupby('name')['current_streak'].max().reset_index()
    longest_streaks.rename(columns={'current_streak': 'longest_streak'}, inplace=True)
    latest_streaks = streaks.groupby('name').apply(lambda x: x.loc[x['starting_date'].idxmax()]).reset_index(drop=True)
    latest_streaks = latest_streaks.merge(longest_streaks, on='name')
    latest_streaks = latest_streaks.sort_values(by='current_streak', ascending=False)
    st.write(latest_streaks[['name', 'starting_date', 'current_streak', 'longest_streak']])
