class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    
    def __str__(self):
        """Tampilan friendly untuk user"""
        status = "Aktif" if self.ipk >= 2.0 else "Peringatan"
        return f"{self.nama} | {self.nim} | IPK: {self.ipk} ({status})"
    
    def __repr__(self):
        """Tampilan detail untuk developer"""
        return (f"Mahasiswa(nama='{self.nama}', nim='{self.nim}', "
                f"jurusan='{self.jurusan}', ipk={self.ipk})")

mhs1 = Mahasiswa("Aji", "252410103104", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Mbud", "252410103105", "Sistem Informasi", 1.8)

print("=== Data Mahasiswa ===")
print(mhs1) 
print(mhs2)  

print("\n=== Debug Info ===")
print(repr(mhs1))
print(mhs1.__repr__())
