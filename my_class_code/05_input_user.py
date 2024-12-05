import streamlit as st

def main():


    # Received from Input User
    fname = st.text_input("Enter firstname", max_chars=10)
    st.title(fname)

    password = st.text_input("Enter password", type='password')
    st.write(password)

    message = st.text_area("Enter message", height=100)
    st.write(message)

    number = st.number_input("Enter number", 1 , 25, 5)
    st.write(number)

    my_appointment = st.date_input("Appointment")
    st.write(my_appointment)

    my_time = st.time_input("Insert time")
    st.write(my_time)

    color = st.color_picker("Select Color")
    st.write(color)
    
if __name__ == '__main__':
    main()