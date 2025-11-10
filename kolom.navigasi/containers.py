import streamlit as st
import numpy as np

st.title("Container")
st.write("Kelompok: 26")
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")

st.title("Out of Order Container")
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Ountside Container")

container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4)) 