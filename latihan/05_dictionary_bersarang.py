mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "nilai": [85, 90, 88]
    },
    "A002": {
        "nama": "Budi",
        "nilai": [78, 82, 80]
    }
}

for nim, data in mahasiswa.items():
    rata = sum(data["nilai"]) / len(data["nilai"])
    print(f"{nim} - {data['nama']} - rata-rata {rata:.2f}")