class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.status = "Aktif" 
      
    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim} dari jurusan {self.jurusan}"
    
    def ubah_status(self, status_baru):
        self.status = status_baru
        print(f"Status {self.nama} diubah menjadi {self.status}")

mahasiswa1 = Mahasiswa("Budi", "12345", "Informatika")
mahasiswa2 = Mahasiswa("Ani", "67890", "Sistem Informasi")

print(mahasiswa1.nama)
print(mahasiswa1.perkenalan())

mahasiswa1.ubah_status("Cuti")
