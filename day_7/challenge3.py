#app requirements
import streamlit as st
st.title ("Greeting App")
style = st.radio ("Style",['Formal', 'Casual', 'Excited'])
name = st.text_input("What's your name?")
if name:
    if style == "Formal":msg = f"Greetings, {name}."
    elif style == 'Casual': msg = f"Hey{name}!, What's Up?"
    else: msg = f'WELCOME{name}!!!'
