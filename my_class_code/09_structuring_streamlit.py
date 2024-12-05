import streamlit as st
from eda_app import run_eda_app
from ml_app import run_ml_app

import logging

#LOGS_FORMAT = "%(levelname)s %(asctime)s.%(msecs)03d -%(message)s"
#logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formater = logging.Formatter("%(levelname)s %(asctime)s.%(msecs)03d -%(message)s")

file_handler = logging.FileHandler('logs/activity.log')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

def main():
    
    st.set_page_config(page_title='structuring streamlit', layout='wide',
                   initial_sidebar_state='auto')
    st.title("Main App")
    st.subheader("Track all Activities Pages Visited of App")
    menu=['Home', 'EDA', 'ML', 'About']
    choice = st.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        #logger.info("Home Section.")
    elif choice == 'EDA':
        run_eda_app()
        #logger.info("EDA Section.")
    elif choice == 'ML':
        run_ml_app()
        #logger.info("ML Section.")
    else:
        st.subheader("About")
        #logger.info("About Section.")


if __name__ == '__main__':
    main()