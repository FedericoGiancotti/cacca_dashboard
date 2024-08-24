import pandas as pd
import streamlit as st
import plotly.express as px

pd.set_option('display.max_rows', None)

st.set_page_config(page_title="Cacca Dashboard", 
                page_icon="image.png", 
                layout="wide", 
                initial_sidebar_state="collapsed", 
                menu_items=None)

st.title('💩 Cacca Dashboard')
st.write('Dashboard per analizzare i dati di quanto il grupo Kafèèè caga al giorno')

# File uploader
# file = st.file_uploader('Upload your chat file', type='txt')
file = '_chat.txt'
# Load data function
def load_data(file):
    df = pd.read_csv(file, delimiter="\t", header=None)
    df = df[df[0].str.endswith('💩')]
    pattern = r'\[(.*?)\] (.*?): (.*)'
    df[['timestamp', 'name', 'element']] = df[0].str.extract(pattern)
    df = df.drop(columns=[0])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%y, %H:%M:%S')
    return df

if file is not None:
    df = load_data(file)

    # Leaderboard cagate totali
    st.header('Leaderboard cagate totali')
    st.write(df['name'].value_counts())

    # Leaderboard cagate settimanali con filtro settimana
    st.header('Leaderboard cagate settimanali')
    df['week'] = df['timestamp'].dt.isocalendar().week
    weekly_counts = df.groupby(['week', 'name']).size().reset_index(name='element_count')
    selected_week = st.selectbox('Select Week:', sorted(weekly_counts['week'].unique()))
    filtered_data = weekly_counts[weekly_counts['week'] == selected_week]
    ranking = filtered_data.sort_values(by='element_count', ascending=False).reset_index(drop=True)
    st.write(f"Ranking for Week: {selected_week}")
    st.write(ranking)

    # Leaderboard cagate mensili con filtro mese
    st.header('Leaderboard cagate mensili')
    df['month'] = df['timestamp'].dt.month_name()
    monthly_counts = df.groupby(['month', 'name']).size().reset_index(name='element_count')
    selected_month = st.selectbox('Select Month:', sorted(monthly_counts['month'].unique()))
    filtered_data = monthly_counts[monthly_counts['month'] == selected_month]
    ranking = filtered_data.sort_values(by='element_count', ascending=False).reset_index(drop=True)
    st.write(f"Ranking for Month: {selected_month}")
    st.write(ranking)

    # Counter cagate totali gruppo
    st.header('Counter cagate totali gruppo')
    total_cacca = df.shape[0]
    st.write(f'Total cagate: {total_cacca}')

    # Bar chart cagate al giorno gruppo
    st.header('Bar chart cagate al giorno gruppo')
    daily_counts = df.groupby(df['timestamp'].dt.date).size().reset_index(name='element_count')
    daily_counts['date'] = daily_counts['timestamp'].astype(str)
    daily_counts = daily_counts.drop(columns=['timestamp']).set_index('date')
    st.bar_chart(daily_counts)

    # Line chart cagate cumulative
    st.header('Line chart cagate cumulative')
    daily_counts['cumulative'] = daily_counts['element_count'].cumsum()
    st.line_chart(daily_counts['cumulative'])

    # Pie chart distribuzione cagate gruppo
    st.header('Pie chart distribuzione cagate gruppo')
    name_counts = df['name'].value_counts()
    fig = px.pie(names=name_counts.index, values=name_counts.values, 
                title='Distribuzione Cagate per Persona',
                labels={'names': 'Name', 'values': 'Count'}) 
    st.plotly_chart(fig)

    # Bar chart distribuzione oraria cagate gruppo
    st.header('Bar chart distribuzione oraria cagate gruppo')
    df['hour'] = df['timestamp'].dt.hour
    hourly_counts = df['hour'].value_counts().sort_index()
    hourly_counts_df = hourly_counts.reset_index()
    hourly_counts_df.columns = ['Hour of the Day', 'Count']
    st.bar_chart(hourly_counts_df.set_index('Hour of the Day'))

    # Current Streak giorni con cagate per persona
    st.header('Streak corrente giorni con cagate per persona')
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
    streaks['starting_date'] = streaks['starting_date'].dt.strftime('%d/%m/%Y')
    longest_streaks = streaks.groupby('name')['current_streak'].max().reset_index()
    longest_streaks.rename(columns={'current_streak': 'longest_streak'}, inplace=True)
    latest_streaks = streaks.groupby('name').apply(lambda x: x.loc[x['starting_date'].idxmax()]).reset_index(drop=True)
    latest_streaks = latest_streaks.merge(longest_streaks, on='name')
    latest_streaks = latest_streaks.sort_values(by='current_streak', ascending=False)
    st.write(latest_streaks[['name', 'starting_date', 'current_streak', 'longest_streak']])

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

    # Streak giorni in cui tutti abbiamo cagato
    st.header('Streak giorni in cui tutti abbiamo cagato')
    current_streak = df['current_streak'].min()
    st.write(f'Massimo streak di giorni in cui tutti abbiamo cagato: {current_streak} giorni')
    
else:
    st.warning('Please upload a chat file to continue.')


