import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np 


def main():

    st.title("Plotting with St.Pyplot")
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df['target'] = df['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    st.dataframe(df.head())
   
    fig, ax= plt.subplots()
    ax.scatter(*np.random.random(size=(2,100)))
    st.pyplot(fig)

    fig = plt.figure()
    df['target'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    fig = plt.figure()
    sns.countplot(x=df['target'])
    plt.title("Distribuição das Classes")
    st.pyplot(fig)
 
if __name__ == '__main__':
    main()