# Membuat program python berdasarkan flowchart
# Meminta input pengguna untuk umur
umur = int(input("Masukkan umur: "))

# Memeriksa apakah umur kurang dari 10
if umur < 10:
  # Jika ya, maka kategori adalah anak-anak
  kategori = "Anak-anak"
# Memeriksa apakah umur kurang dari 18
elif umur < 18:
  # Jika ya, maka kategori adalah remaja
  kategori = "Remaja"
# Memeriksa apakah umur kurang dari 35
elif umur < 35:
  # Jika ya, maka kategori adalah dewasa
  kategori = "Dewasa"
else:
  # Jika tidak, maka kategori adalah tua
  kategori = "Tua"

# Menampilkan output kategori
print("Kategori:", kategori)
