import streamlit as st

st.title("WELCOME TO S&S BEVERAGES")

name = st.text_input("Enter your company name:")
adr = st.text_area("Enter your company address:")
pname = st.text_input("Enter your machine name:")

button = st.button("Done")
if button:
    st.markdown(f"""
        Name: {name}
        Address: {adr}
        Machine name: {pname}
    """)
