tinggi_segitiga = int(input("masukan jumlah baris segitiga: "))
for i in range(1, tinggi_segitiga + 1):
    print(" " * (tinggi_segitiga - i) + "*" * (2 * i - 1))