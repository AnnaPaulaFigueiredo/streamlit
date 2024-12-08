import streamlit as st

import matplotlib
matplotlib.use("Agg")
import numpy as np 
from sklearn.datasets import load_iris
import pandas as pd

import altair as alt 

def main():

    st.title("Plotting with Altair")
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    df2 = pd.read_csv(r"C:\Users\annap\Documents\streamlit\my_class_code\data\lang_data.csv")

    st.dataframe(df.head())

    st.bar_chart(df['sepal length (cm)'])

    st.bar_chart(df[['sepal length (cm)', 'petal length (cm)']])

    # Line chart
    st.dataframe(df2.head())
    lang_list = df2.columns.to_list()
    lang_choices = st.multiselect("Choose Language", lang_list, default='Python' )
    new_df = df2[lang_choices]
    st.line_chart(new_df)

    # Area chart
    st.area_chart(new_df, use_container_width=True)

    # Altair
    df3 = pd.DataFrame( np.random.randn(200,3), columns=['a','b','c'])
    st.dataframe(df3.head())

    c = alt.Chart(df3).mark_circle().encode( x='a', y='b', size='c', color='c',
                                            tooltip=['a','b'])

    #st.write(c)
    st.altair_chart(c, cuse_container_width=True)

if __name__ == '__main__':
    main()