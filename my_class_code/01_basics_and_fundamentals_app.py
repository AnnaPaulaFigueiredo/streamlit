import streamlit as st

def main():

    st.text("Hello World this is a text")
    name="Anna"
    st.text("My name is {}.".format(name))

    st.header("This is a Header.")
    st.subheader("This is a Subheader.")

    st.title("This is a Title.")

    st.markdown("# This is markdown.")
    st.markdown("## This is markdown.")

 # Color text with bootstrap 
    st.success("Successful!")
    st.warning("This is danger!")
    st.info("This is info!")
    st.error("This is an error!")
    try:
    # Código que pode gerar uma exceção
        x = 1 / 0
    except Exception as e:
        st.exception("This is in exception{} !".format(e))

# Superfunction
    st.text("# This is a text")
    st.text(1+1)

    st.write(dir(st))

# Help function
    st.help(range)
if __name__ == '__main__':
    main()