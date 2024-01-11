import streamlit as st
import mysql.connector

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    if tinggi == 0:
        st.error("Berat dan Tinggi tidak boleh nol. Harap masukkan nilai tinggi yang valid.")
        return None
    bmi1 = berat / (tinggi / 100) ** 2
    bmi = round(bmi1, 1)
    return bmi

# Fungsi untuk menilai BMI
def menilai_bmi(bmi, gender):
    if gender == "l":
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Ideal"
        elif 25 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"
    elif gender == "p":
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Ideal"
        elif 25 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"

# Fungsi untuk input jenis kelamin
def input_gender():
    gender = st.selectbox("Pilih jenis kelamin:", ["Laki-laki", "Perempuan"])
    return gender.lower()[0]  # Mengambil karakter pertama ("l" atau "p")

# Fungsi untuk mencetak hasil
def print_hasil(gender, bmi, kategori):
    st.write("\nHasil:")
    st.write("Jenis Kelamin:", "Laki-laki" if gender == "l" else "Perempuan")
    st.write("BMI Anda:", round(bmi, 2))
    st.write("Kategori BMI:", kategori)

# Fungsi untuk menyambungkan ke database MySQL
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bmi"
    )
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cowo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            jk VARCHAR(1),
            berat DOUBLE,
            tinggi DOUBLE,
            bmi DOUBLE,
            kategori VARCHAR(20)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cewe (
            id INT AUTO_INCREMENT PRIMARY KEY,
            jk VARCHAR(1),
            berat DOUBLE,
            tinggi DOUBLE,
            bmi DOUBLE,
            kategori VARCHAR(20)
        )
    ''')

    conn.commit()
    return conn, cursor

# Streamlit UI
st.title("Kalkulator BMI Sederhana")
st.write("------------------------")

# Membuat koneksi ke database
conn, cursor = connect_db()

# Input data BMI
berat = st.number_input("Masukkan berat (kg): ", 0, 1000)
tinggi = st.number_input("Masukkan tinggi (cm): ", 0, 1000)
gender = input_gender()

# Tombol untuk memulai perhitungan
calculate_button = st.button("Hitung BMI")

# Menghitung BMI jika tombol diklik
if calculate_button:
    # Menghitung BMI
    bmi = hitung_bmi(berat, tinggi)

    # Jika BMI telah dihitung
    if bmi is not None:
        # Menilai BMI
        kategori = menilai_bmi(bmi, gender)

        # Mencetak hasil
        print_hasil(gender, bmi, kategori)

        # Menyimpan data ke database sesuai jenis kelamin
        if gender == "l":
            cursor.execute('''
                INSERT INTO cowo (jk, berat, tinggi, bmi, kategori)
                VALUES (%s, %s, %s, %s, %s)
            ''', (gender, berat, tinggi, bmi, kategori))
        elif gender == "p":
            cursor.execute('''
                INSERT INTO cewe (jk, berat, tinggi, bmi, kategori)
                VALUES (%s, %s, %s, %s, %s)
            ''', (gender, berat, tinggi, bmi, kategori))

        conn.commit()

        st.success("Data berhasil ditambah")

# Menutup koneksi database
conn.close()
