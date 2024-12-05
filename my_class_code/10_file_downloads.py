import streamlit as st


from sklearn.datasets import load_iris
import pandas as pd
import base64
import time

timestr = time.strftime("%Y%m%d-%H%M%S")

st.set_page_config(page_title='Download Files', layout='wide', initial_sidebar_state='auto')

class FileDownloader(object):
    def __init__(self, data, file_name='my_file', file_ext='txt'):
        super(FileDownloader, self).__init__()
        self.data = data
        self.filename = file_name
        self.file_ext = file_ext

    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"{self.filename}_{timestr}.{self.file_ext}"
        st.markdown("### Download File ###")
        href = f'<a href="data:application/{self.file_ext};base64,{b64}" download="{new_filename}">Click Here!!</a>'
        st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("Download Files")
    menu = ['Home', 'CSV', 'About']
    choice = st.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        my_text = st.text_area("Your message ...")
        if st.button("Save"):
            st.write(my_text)
            FileDownloader(my_text, file_name="text_file", file_ext="txt").download()
    elif choice == "CSV":
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['target'] = iris.target
        st.table(df)
        csv_data = df.to_csv(index=False)
        FileDownloader(csv_data, file_name="iris_data", file_ext="csv").download()
    else:
        st.subheader("About")
        st.write("This is a Streamlit app for downloading files.")

if __name__ == '__main__':
    main()
