import streamlit as st 

st.title ("Columns")
st.write("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

col1, col2 = st.columns(2)
col1.write("Ini adalah kolom pertama")
col1.image("../Asset/animals.jpg")
col2.write("Ini adalah kolom kedua")
col2.image("../Asset/animals2.jpg")