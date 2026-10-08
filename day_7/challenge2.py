import streamlit as st
st.title("Core Greeting App")
name = st.text_input("Enter Name:")
if name:
    st.write (f"hello,{name}!")