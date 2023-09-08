class Contact:
    def __init__(self, nama, nomor_telpon, email):
        self.nama = nama
        self.nomor_telpon = nomor_telpon
        self.email = email

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Nomor_telpon: {self.nomor_telpon}")
        print(f"Email: {self.email}")
        print()

class AddresBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilkan_semua_kontak(self):
        print("daftar kontak:")
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

if __name__ == "__main__":
    addres_book = AddresBook()

    while True:
        print("Menu:")
        print("1. Tambah kontak")
        print("2. Tampilkan semua kontak")
        print("3. Keluar")

        pilihan = input("pilih menu (1/2/3): ")

        if pilihan == "1":
            nama = input("Nama: ")
            nommor_telpon = input("Nomor_telpon: ")
            email = input("email: ")
            kontak_baru = Contact(nama, nommor_telpon, email)
            addres_book.tambah_kontak(kontak_baru)
        elif pilihan == "2":
            addres_book.tampilkan_semua_kontak()
        elif pilihan == "3":
            break
        else:
            print("pilihan tidak valid. silahkan pilih menu yang benar.")