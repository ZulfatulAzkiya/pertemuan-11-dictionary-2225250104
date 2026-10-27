nilai = {
    "Matematika": 90,
    "Bahasa Indonesia": 85,
    "Python": 88
}

print("Keys:")
for mata_kuliah in nilai.keys():
    print(mata_kuliah)

print("Values:")
for skor in nilai.values():
    print(skor)

print("Items:")
for mata_kuliah, skor in nilai.items():
    print(f"{mata_kuliah}: {skor}")