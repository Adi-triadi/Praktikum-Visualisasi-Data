import streamlit as st
from PIL import Image

st.header("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi - 0110222077
""")

img = Image.open("../Asset/animals.jpg")
st.title("Grid")
for a in range(4):
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)