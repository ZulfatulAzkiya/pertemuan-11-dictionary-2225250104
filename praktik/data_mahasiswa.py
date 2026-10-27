def tampilkan_mahasiswa(data):
    for nim, info in data.items():
        print(f"{nim} | {info['nama']} | nilai {info['nilai']}")


def main():
    data = {
        "2225250101": {"nama": "Ayu", "nilai": 85},
        "2225250102": {"nama": "Budi", "nilai": 92},
        "2225250103": {"nama": "Citra", "nilai": 78}
    }

    print("SISTEM DATA MAHASISWA")

    nim = input(
        "Cari NIM (kosong untuk tampilkan semua): "
    ).strip()

    if nim:
        info = data.get(nim)

        if info:
            print(f"Nama: {info['nama']}")
            print(f"Nilai: {info['nilai']}")
        else:
            print("NIM tidak ditemukan.")
    else:
        tampilkan_mahasiswa(data)


if __name__ == "__main__":
    main()