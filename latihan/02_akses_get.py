data = {
    "nama": "Ayu",
    "nilai": 85
}

print(data.get("nama"))
print(data.get("kelas", "Belum diisi"))

if "nilai" in data:
    print("Nilai tersedia.")