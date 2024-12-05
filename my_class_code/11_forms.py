import streamlit as st
import pandas as pd

def main():
    st.title("Stremlit Forms & Salary Calculator")

    menu = ['Home', 'About']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        with st.form(key='salaryform'):
            col1, col2, col3 = st.columns([3,2,1])  

            with col1:
                amount = st.number_input("Hourly Rate in $")

            with col2:
                hour_per_week = st.number_input("Hours per week", 1, 120)

            with col3:
                st.text("Salary")        
                submit_salary = st.form_submit_button("Calculate Salary")

        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hour_per_week]

                df = pd.DataFrame({'hourly':amount, 'daily':daily, 'weekly':weekly})
                st.dataframe(df)


        #method 1 -  para resetar o formulário ao clicar em submit
        with st.form(key='form1', clear_on_submit=True): 
            
            first_name = st.text_input("First Name:")
            last_name = st.text_input("Last Name:")
            date_birt = st.date_input("Date of Birth")


            submit_button = st.form_submit_button(label='SingUp')

        if submit_button:
            st.write("{} you ve created your account!".format(first_name))

    
        # method 2:
        form2 = st.form(key='form2')
        user_name = form2.text_input("User name:")
        jobtype = form2.selectbox("Job", ['Dev', 'Data Scientist', 'Doctor'])
        submit_button2 = form2.form_submit_button("Submit")

        if submit_button2:
            st.write("{} you ve created your account! \n Your selected job:{}".format(user_name, jobtype))
           

    else:
        st.subheader("About")
    

if __name__ == '__main__':
    main()