# Membaca jumlah baris dari pengguna
n = int(input("Masukkan jumlah baris segitiga: "))

# Loop untuk membuat segitiga siku-siku
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
