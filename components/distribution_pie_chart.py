import plotly.express as px
import streamlit as st

def distribution_pie_chart(df):
    st.header('Pie chart distribuzione cagate gruppo')
    name_counts = df['name'].value_counts()
    fig = px.pie(names=name_counts.index, values=name_counts.values, 
                 title='Distribuzione Cagate per Persona',
                 labels={'names': 'Name', 'values': 'Count'}) 
    st.plotly_chart(fig)
