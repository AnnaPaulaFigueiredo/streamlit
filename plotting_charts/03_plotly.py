import streamlit as st

import numpy as np 
from sklearn.datasets import load_iris
import pandas as pd

import plotly.express as px


def main():

    st.title("Plotting with Plotly")
    
    df = pd.read_csv(r"../my_class_code/data/prog_languages_data.csv")
    st.dataframe(df.head())

    fig = px.pie(df, values='Sum', names='lang', title='Pie chart with plotly')
    st.plotly_chart(fig)

    fig2 = px.bar(df, x='lang', y='Sum')
    st.plotly_chart(fig2)
    

if __name__ == '__main__':
    main()