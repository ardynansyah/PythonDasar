# Membuat program python berdasarkan flowchart
# Meminta input pengguna untuk skor siswa
skor = int(input("Masukkan skor siswa: "))

# Memeriksa apakah skor lebih besar atau sama dengan 75
if skor >= 75:
  # Jika ya, maka siswa lulus
  print("Siswa lulus")
else:
  # Jika tidak, maka meminta input pengguna apakah siswa ingin mengulang tes
  ulang = input("Apakah siswa ingin mengulang tes? (y/n): ")
  # Memeriksa apakah input pengguna adalah y
  if ulang == "y":
    # Jika ya, maka siswa mengulang tes
    print("Siswa mengulang tes")
  else:
    # Jika tidak, maka siswa gagal
    print("Siswa gagal")
