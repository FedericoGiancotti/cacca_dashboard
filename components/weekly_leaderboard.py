import streamlit as st

def weekly_leaderboard(df):
    st.header('Leaderboard settimanale')
    weekly_counts = df.groupby(['week', 'name']).size().reset_index(name='element_count')
    selected_week = st.selectbox('Select Week:', sorted(weekly_counts['week'].unique()))
    filtered_data = weekly_counts[weekly_counts['week'] == selected_week]
    ranking = filtered_data.sort_values(by='element_count', ascending=False).reset_index(drop=True)
    st.write(f"Ranking for Week: {selected_week}")
    st.write(ranking)
