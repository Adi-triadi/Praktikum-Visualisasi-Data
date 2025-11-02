import streamlit as st # Untuk mengimpor librari
import time # untuk mengimpor modul time        

st.title("Praktikum 4 - Visualisasi Data")
st.caption("Bagian 4: Button Sliders")

# Markdown menampilkan teks di Streamlit dengan format agar tampil lebih rapi dan menarik
st.markdown("""
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
 """)

# Buttons
# st.title digunakan untuk membuat judul utama di aplikasi Streamlit.
st.title('Creatiting a Button') 
# button = st.button digunakan untuk menjalankan aksi ketika pengguna menekannya
button = st.button('Click Here')
if button:
    st.write('Youn Have Klicked the Button')
else:
    st.write('You Hane Not Clicked the Button')

#Radio Button 
st.title('Creating Radio Button')

# gender = st.radio digunakan untuk menampilkan daftar pilihan, 
# dan hanya satu opsi yang bisa dipilih oleh pengguna
gender = st.radio( 
    "Select your gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You Have Selected Male')
elif gender == 'Female':
    st.write('You Have Selected Female')
else:
    st.write('You Have Selected Others')

#Check Boxes
st.title('Creating Checkboxes')
# st.write digunakan untuk menampilkan output atau isi variabel
st.write('select Your Hobies:')
# check_1 = st.checkbox digunakan untuk menampilkan kotak centang yang bisa dipilih (✔) 
# atau dikosongkan oleh pengguna
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

#Drop-Downs
st.title('Creating Dropdown')
# hobby = st.selectbox digunakan untuk menampilkan daftar pilihan dalam bentuk dropdown, 
# di mana pengguna hanya bisa memilih satu nilai
hobby = st.selectbox('Choose your hobby:',
('Books', 'Movies', 'Sports'))

#Multiselects
st.title('Multi-Select')
# hobbies = st.multiselect digunakan untuk menampilkan daftar pilihan, 
# dan pengguna bisa memilih beberapa opsi sekaligus
hobbies = st.multiselect(
    'Where are you Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing'])

#Download Buttons
st.title('Download Button')
# down_btn = st.download_button membuat tombol unduh yang memungkinkan pengguna
# mengunduh data atau file dari aplikasi
down_btn = st.download_button(
    label="Download Book",
    data = open("C:/Users/Adi/Documents/VisDAt/Tugas/files/gambar buku.jpg", "rb"),
    file_name="gambar buku.jpg",
    mime="image/jpg"
)
down_btn = st.download_button(
    label="Download Movies",
    data = open("C:/Users/Adi/Documents/VisDAt/Tugas/files/OIP.JFIF", "rb"),
    file_name="OIP>JFIF",
    mime="image/JFIF"
)
down_btn = st.download_button(
    label="Download Sports",
    data = open("C:/Users/Adi/Documents/VisDAt/Tugas/files/sports.jpg ", "rb"),
    file_name="sports.jpg",
    mime="image/jpg"
)
#Progress Bars
st.title('Porgress Bar')
# download = st.progress(0) digunakan untuk menampilkan indikator kemajuan (progress bar) 
# dengan nilai antara 0 sampai 100%
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

#Spinners
st.title('spinner')
# with st.spinner digunakan untuk menampilkan pesan dan animasi loading
#  sementara kode di dalam blok sedang berjalan
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')