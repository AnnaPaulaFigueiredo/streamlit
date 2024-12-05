import streamlit as st

st.set_page_config(page_title='hello everyone',
                   page_icon= '🥰', layout='centered', layout='wide',
                   initial_sidebar_state='expanded')#collapsed/auto #':smiley:') or image from image_open

def main():

    st.title("Page config 🥰, ':smiley:'")
    st.sidebar.success("Menu")
    
if __name__ == '__main__':
    main()