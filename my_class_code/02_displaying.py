import streamlit as st

import pandas as pd

from sklearn.datasets import load_iris

def main():

    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target

    # dymaic table
    st.dataframe(df, 200, 100)

    # adding color in the maximum values
    st.dataframe(df.style.highlight_max(axis=0))
    # static table
    st.table(df)

    # using superfunction
    st.write(df.head())

    # json files
    st.json({'name':'anna'})

    # code
    my_code = """def say_hello():
    print("Hello Streamlit")"""
    st.code(my_code, language='python')

if __name__ == '__main__':
    main()