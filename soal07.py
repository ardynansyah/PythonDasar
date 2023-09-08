# Membuat program python berdasarkan flowchart
# Meminta input pengguna untuk nama dan gaji pokok
nama = input("Masukkan nama: ")
gaji_pokok = int(input("Masukkan gaji pokok: "))

# Menghitung tunjangan dan pajak
tunjangan = 0.2 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)

# Menghitung gaji bersih
gaji_bersih = gaji_pokok + tunjangan - pajak

# Menampilkan output nama, gaji pokok, dan gaji bersih
print("Nama:", nama)
print("Gaji Pokok:", gaji_pokok)
print("Gaji Bersih:", gaji_bersih)
