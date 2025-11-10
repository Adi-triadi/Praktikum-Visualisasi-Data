import streamlit as st 
from PIL import Image

img = Image.open("../Asset/animals.jpg")
st.title ("Padding")
st.write("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)