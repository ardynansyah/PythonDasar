import math

# Fungsi untuk menghitung volume tabung
def hitung_volume_tabung(jari_jari, tinggi):
    volume = math.pi * jari_jari**2 * tinggi
    return volume

# Fungsi untuk menghitung volume balok
def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

# Input data dari pengguna
pilihan = input("Pilih bentuk yang akan dihitung (tabung / balok): ")

if pilihan == "tabung":
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi_tabung = float(input("Masukkan tinggi tabung: "))
    volume = hitung_volume_tabung(jari_jari, tinggi_tabung)
    print(f"Volume tabung: {volume}")
elif pilihan == "balok":
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi_balok = float(input("Masukkan tinggi balok: "))
    volume = hitung_volume_balok(panjang, lebar, tinggi_balok)
    print(f"Volume balok: {volume}")
else:
    print("Pilihan tidak valid")
