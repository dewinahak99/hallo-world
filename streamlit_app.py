import streamlit as st

# Fungsi untuk menentukan salam berdasarkan bahasa
def salam(bahasa, nama):
    if bahasa == "Indonesia":
        return f"Selamat datang, {nama}! Senang bertemu dengan Anda di Hub Informatika!"
    elif bahasa == "English":
        return f"Welcome, {nama}! Great to see you at Informatics Hub!"
    elif bahasa == "Español":
        return f"¡Bienvenido, {nama}! ¡Es un placer verte en el Centro de Informática!"
    elif bahasa == "Français":
        return f"Bienvenue, {nama} ! Ravi de vous voir au Hub Informatique!"
    return f"Hello, {nama}! Welcome to Informatics Hub!"

# Judul aplikasi
st.title("🌟 HUB INFORMATIKA 🌟")

# Penjelasan aplikasi
st.write("Masukkan nama Anda dan pilih preferensi Anda di bawah ini:")

# Input untuk nama
nama = st.text_input("Masukkan nama Anda:", "")

# Pilihan bahasa
bahasa = st.selectbox("Pilih bahasa Anda:", ["Indonesia", "English", "Español", "Français"])

# Pilihan tema warna
tema = st.radio("Pilih tema warna:", ["Biru", "Hijau", "Merah", "Kuning"])

# Warna berdasarkan tema
warna_tema = {
    "Biru": "#1f77b4",
    "Hijau": "#2ca02c",
    "Merah": "#d62728",
    "Kuning": "#ff7f0e"
}

# Menyimpan preferensi
st.write(f"Anda memilih tema {tema} dan bahasa {bahasa}. Pilihan Anda akan disimpan!")

# Tampilkan pesan sambutan jika nama sudah diisi
if nama:
    st.markdown(f"<h2 style='color:{warna_tema[tema]};'>{salam(bahasa, nama)}</h2>", unsafe_allow_html=True)
else:
    st.write("Silakan masukkan nama Anda untuk mendapatkan sambutan.")

# Opsi checkbox untuk menampilkan detail tambahan
if st.checkbox("Tampilkan informasi tambahan"):
    st.write("Terima kasih telah menggunakan aplikasi ini. Kami berharap Anda menikmati pengalaman di Hub Informatika!")

# Tambahkan link eksternal (contoh link ke halaman resmi Streamlit)
st.write("Pelajari lebih lanjut tentang [Streamlit](https://streamlit.io) untuk membuat aplikasi web interaktif dengan Python.")
