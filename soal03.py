# Membuat daftar bilangan
bilangan = [5]

# Membaca jumlah bilangan dari pengguna
n = int(input("Masukkan jumlah bilangan: "))

# Membaca bilangan-bilangan dari pengguna
for i in range(n):
    bil = int(input(f"Masukkan bilangan ke-{i+1}: "))
    bilangan.append(bil)

# Mencetak bilangan ganjil dan genap
bilangan_ganjil = []
bilangan_genap = []

for bil in bilangan:
    if bil % 2 == 0:
        bilangan_genap.append(bil)
    else:
        bilangan_ganjil.append(bil)

print("Bilangan Ganjil:")
for ganjil in bilangan_ganjil:
    print(ganjil)

print("Bilangan Genap:")
for genap in bilangan_genap:
    print(genap)
