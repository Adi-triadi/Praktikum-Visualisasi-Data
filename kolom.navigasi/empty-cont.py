import streamlit as st
import time

st.header("Praktikum02")
st.title("Empty")
st.write("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

with st.empty():
    for seconds in range(5):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
        st.write("✔ Times up!")