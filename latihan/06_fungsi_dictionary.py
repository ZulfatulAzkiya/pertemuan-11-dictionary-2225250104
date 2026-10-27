def cari_mahasiswa(data, nim):
    return data.get(nim, "Data mahasiswa tidak ditemukan")


data = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 90}
}

nim = input("Masukkan NIM: ").strip().upper()

print(cari_mahasiswa(data, nim))