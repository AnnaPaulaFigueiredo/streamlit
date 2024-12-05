import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px

st.set_page_config(page_title='plots', layout='wide',
                   initial_sidebar_state='expanded')#collapsed/auto #':smiley:') or image from image_open

def main():

    st.title("Plotting in Streamlit with Plotly")

    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df.head())

    # pie chart
    fig = px.pie(df, values='Sum', names='lang', title='Pie Chart by Languages')
    st.plotly_chart(fig)

    # Bar chart
    fig2=px.bar(df, x='lang', y='Sum', title='Bar chart')
    st.plotly_chart(fig2)
if __name__ == '__main__':
    main()