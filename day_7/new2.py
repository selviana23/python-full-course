import streamlit as st
clicked = st.button ("Calculate")
agree = st.checkbox("I agree to the terms")
fruit = st.selectbox ("Favourite fruit",["Apple", "Banana", "Mango"])

col1 , col2 = st.columns(2)
with col1:
    st.write("Left side")
with col2:
    st.write("Right side")