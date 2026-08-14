tugas = []

while input("Apakah Anda ingin menambahkan tugas? (Iya/Tidak): ").lower() == "iya":
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)

    print(f"\nTugas {tugas_baru} berhasil ditambahkan.\n")

print(f"\nDaftar Tugas: {tugas}")
