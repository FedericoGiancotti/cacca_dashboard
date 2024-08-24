import streamlit as st

def monthly_leaderboard(df):
    st.header('Leaderboard mensile')
    monthly_counts = df.groupby(['month', 'name']).size().reset_index(name='element_count')
    selected_month = st.selectbox('Select Month:', sorted(monthly_counts['month'].unique()))
    filtered_data = monthly_counts[monthly_counts['month'] == selected_month]
    ranking = filtered_data.sort_values(by='element_count', ascending=False).reset_index(drop=True)
    st.write(f"Ranking for Month: {selected_month}")
    st.write(ranking)
