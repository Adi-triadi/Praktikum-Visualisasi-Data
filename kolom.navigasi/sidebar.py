import streamlit as st

st.header ("Praktikum02")
st.write("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

st.sidebar.title("Sidebar")
st.sidebar.radio("Are You a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)