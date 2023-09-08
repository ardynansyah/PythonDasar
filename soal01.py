# Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

# Fungsi untuk menghitung luas dan keliling persegi panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Fungsi untuk menghitung luas dan keliling trapezium
def hitung_trapezium(panjang_atas, panjang_bawah, tinggi):
    luas = 0.5 * (panjang_atas + panjang_bawah) * tinggi
    keliling = panjang_atas + panjang_bawah + 2 * (tinggi**2 + ((panjang_atas - panjang_bawah)**2))**0.5
    return luas, keliling

# Input data dari pengguna
pilihan = input("Pilih bentuk yang akan dihitung (persegi / persegi panjang / trapezium): ")

if pilihan == "persegi":
    sisi = float(input("Masukkan panjang sisi: "))
    luas, keliling = hitung_persegi(sisi)
    print(f"Luas persegi: {luas}")
    print(f"Keliling persegi: {keliling}")
elif pilihan == "persegi panjang":
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas, keliling = hitung_persegi_panjang(panjang, lebar)
    print(f"Luas persegi panjang: {luas}")
    print(f"Keliling persegi panjang: {keliling}")
elif pilihan == "trapezium":
    panjang_atas = float(input("Masukkan panjang sisi atas: "))
    panjang_bawah = float(input("Masukkan panjang sisi bawah: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas, keliling = hitung_trapezium(panjang_atas, panjang_bawah, tinggi)
    print(f"Luas trapezium: {luas}")
    print(f"Keliling trapezium: {keliling}")
else:
    print("Pilihan tidak valid")
