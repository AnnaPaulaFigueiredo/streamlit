import streamlit as st


def main():

    # create a storage for Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    #st.write(st.session_state.messages)
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("Ask something")
    if prompt:
        
        # add the user prompt to the chat history
        st.session_state.messages.append({'role':'user','content':prompt})
        with st.chat_message("user"):
            st.write(prompt)

        #with st.chat_message("assistant"):
        #    st.write(prompt)

        # custom avatar
        #with st.chat_message("bot", avatar="🐼"):
        #    st.write(prompt)

if __name__ == '__main__':
    main()