#apps requirements
import streamlit as st

height = st.number_input("Height(m)")
weight = st.number_input ("Weight(kg)")
if st.button("calculate"):
    bmi = weight / (weight ** 2)
    st.write(f"Your BMI : {bmi:.2f}")