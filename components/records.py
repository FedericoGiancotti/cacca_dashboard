import streamlit as st

def records(df, weekly_counts, monthly_counts):
    # Record persona con più cagate in un giorno
    st.header('Record persona con più cagate in un giorno')
    max_cacca = df['name'].value_counts().idxmax()
    max_cacca_count = df['name'].value_counts().max()
    max_cacca_people = df['name'].value_counts()[df['name'].value_counts() == max_cacca_count].index.tolist()
    st.write(f'{", ".join(max_cacca_people)}: {max_cacca_count} cagate in un giorno')

    # Record persona con più cagate in una settimana
    st.header('Record persona con più cagate in una settimana')
    max_weekly_cacca = weekly_counts.groupby('name')['element_count'].max().idxmax()
    max_weekly_cacca_count = weekly_counts.groupby('name')['element_count'].max().max()
    max_weekly_cacca_people = weekly_counts.groupby('name')['element_count'].max()[weekly_counts.groupby('name')['element_count'].max() == max_weekly_cacca_count].index.tolist()
    st.write(f'{", ".join(max_weekly_cacca_people)}: {max_weekly_cacca_count} cagate in una settimana')

    # Record persona con più cagate in un mese
    st.header('Record persona con più cagate in un mese')
    max_monthly_cacca = monthly_counts.groupby('name')['element_count'].max().idxmax()
    max_monthly_cacca_count = monthly_counts.groupby('name')['element_count'].max().max()
    max_monthly_cacca_people = monthly_counts.groupby('name')['element_count'].max()[monthly_counts.groupby('name')['element_count'].max() == max_monthly_cacca_count].index.tolist()
    st.write(f'{", ".join(max_monthly_cacca_people)}: {max_monthly_cacca_count} cagate in un mese')
