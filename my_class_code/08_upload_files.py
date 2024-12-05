import streamlit as st
from docx import Document
# File processing packages
from PIL import Image

import pandas as pd
import docx2txt
from PyPDF2 import PdfReader
import pdfplumber
import os 

@st.cache_data
def load_images(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):

    pdf_reader = PdfReader(file)
    all_page_text = ""

    # Itera pelas páginas diretamente
    for page in pdf_reader.pages:
        all_page_text += page.extract_text()

    return all_page_text

def save_upload_file(uploaded_file):

    if uploaded_file is not None:
        with open(os.path.join("tempDir", str(uploaded_file.name)), "wb") as f:        
            f.write(uploaded_file.getbuffer())
        return st.success("File Saved")

st.set_page_config(page_title='upload files', layout='wide',
                   initial_sidebar_state='expanded')#collapsed/auto #':smiley:') or image from image_open

def main():

    st.title("FIle Upload ")
    
    menu=["Image","Dataset", "Document Files", "Multiple Files"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image":
        st.subheader("Image")
        image_file = st.file_uploader("Upload Images", type=['png', "jpg", "jpeg"])
        if image_file is not None:
            #st.write(type(image_file))
            # methods and atributes 
            st.write(dir(image_file))
            file_details = {'filename':image_file.name, 'file_type':image_file.type, 'file_size':image_file.size}
            st.write(file_details)

            img = load_images(image_file)
            st.image(img)
            # saving file
        
        save_upload_file(image_file)

    if choice == "Dataset":
        st.subheader("Dataset")
        
        dataset_file = st.file_uploader("Upload Images", type=['csv'])
        if dataset_file is not None:
            st.write(dir(dataset_file))
            file_details = {'filename':dataset_file.name, 'file_type':dataset_file.type, 'file_size':dataset_file.size}
            st.write(file_details)

            df = pd.read_csv(dataset_file)
            st.table(df)
        
        save_upload_file(dataset_file)

    if choice == "DocumentFiles":
        st.subheader("Document Files")
        docx_file = st.file_uploader("Upload Document", type=["pdf", "docx", "txt"])

        if st.button("Process"):
            if docx_file is not None:

                # Mostrar informações do arquivo
                file_details = {'filename': docx_file.name, 'file_type': docx_file.type,'file_size': docx_file.size}
                st.write(file_details)
                
                if docx_file.type == "text/plain":
                    #read as bytes                    
                    #raw_text = docx_file.read()
                    #st.write(raw_text)
                    #st.text(raw_text)
                    raw_text = str(docx_file.read(), "utf-8")
                    st.text(raw_text)

                # Processar o arquivo .docx
                elif docx_file.type == "application/pdf":
                    
                    ''' try:
                        with pdfplumber.open(docx_file) as pdf:
                            pages = pdf.pages[0]
                            st.write(pages.extract_text())
                       
                    except:
                        st.warning("None")
                    '''
                   
                    raw_text = read_pdf(docx_file)
                    st.write(raw_text)
                else:
                    raw_text = docx2txt.process(docx_file)
                    st.write(raw_text)
                    #st.text(raw_text)
                
                save_upload_file(docx_file)
    if choice == "Multiple Files":
        st.subheader("Multiple Files")

        uploadedfiles = st.file_uploader("Upload Multiple Files.", type=['png','jpeg', 'jpg'], accept_multiple_files=True)
        if uploadedfiles is not None:
            st.write(uploadedfiles)
            for image_file in uploadedfiles:
                st.write(image_file.name)
                st.image(load_images(image_file), width=250)
                save_upload_file(image_file)
        else:
            st.subheader("About App")

if __name__ == '__main__':
    main()