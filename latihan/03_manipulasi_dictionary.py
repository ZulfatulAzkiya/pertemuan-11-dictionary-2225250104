data = {
    "nama": "Ayu",
    "nilai": 85
}

data["kelas"] = "A"
data["nilai"] = 90
data.update({"program_studi": "Pendidikan Matematika"})

print("Setelah ditambah/diubah:", data)

data.pop("kelas", None)

print("Setelah kelas dihapus:", data)