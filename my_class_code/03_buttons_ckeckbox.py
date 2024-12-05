import streamlit as st



def main():

    # Buttons
    name='Anna'

    if st.button("Submit", key='first_name'):
        st.write("Name: {}.".format(name.upper()))

    if st.button("Submit", key='second_name'):
        st.write("Name: {}.".format(name.lower()))

    # Radio buttons
    status = st.radio("Whats is radio status?", ("Active", "Inactive", "I don't know"))
    if status == 'Active':
        st.success('You are active')
    if status == "Inactive":
        st.warning("Inactive")
    else:
        st.info("I don't know")
    
    if st.checkbox("Show/hide"):
        st.text("Showing something")

    with st.expander('Anna Paula'):
        st.text("Hello Anna")

    # select option
    my_languages = ['python', 'julia', 'go', 'rust']
    choice = st.selectbox("Language", my_languages)
    st.write("You selected {}.".format(choice))

    spoken_languages = ("English", "French", "Spanish", "Twi")
    my_spoken_lang = st.multiselect("Spoken Language: ", spoken_languages, default='English')

    # numbers
    # anydata type (int/float/dates)
    age = st.slider("Age", 1,100,5) # start in 5

    # slider text
    color = st.select_slider("Choose Color:", options=['yellow', 'red', 'blue', 'black'], value=("yellow", "red")) 

if __name__ == '__main__':
    main()