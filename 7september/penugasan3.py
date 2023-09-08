import tkinter as tk

class DataSiswaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Data Siswa")

        # Tambahkan label "DATA SISWA" dengan warna biru
        self.label_data_siswa = tk.Label(root, text="DATA SISWA", font=("Helvetica", 20), fg="blue")
        self.label_data_siswa.pack()

        self.data_siswa = []

        self.label_nama = tk.Label(root, text="Nama Lengkap:")
        self.label_nama.pack()

        self.entry_nama = tk.Entry(root, width=50)
        self.entry_nama.pack()

        self.label_tanggal_lahir = tk.Label(root, text="Tanggal Lahir:")
        self.label_tanggal_lahir.pack()

        self.entry_tanggal_lahir = tk.Entry(root, width=50)
        self.entry_tanggal_lahir.pack()

        self.label_asal_sekolah = tk.Label(root, text="Asal Sekolah:")
        self.label_asal_sekolah.pack()

        self.entry_asal_sekolah = tk.Entry(root, width=50)
        self.entry_asal_sekolah.pack()

        self.label_nisn = tk.Label(root, text="NISN:")
        self.label_nisn.pack()

        self.entry_nisn = tk.Entry(root, width=50)
        self.entry_nisn.pack()

        self.label_nama_ayah = tk.Label(root, text="Nama Ayah:")
        self.label_nama_ayah.pack()

        self.entry_nama_ayah = tk.Entry(root, width=50)
        self.entry_nama_ayah.pack()

        self.label_nama_ibu = tk.Label(root, text="Nama Ibu:")
        self.label_nama_ibu.pack()

        self.entry_nama_ibu = tk.Entry(root, width=50)
        self.entry_nama_ibu.pack()

        self.label_nomor_telepon = tk.Label(root, text="Nomor Telepon:")
        self.label_nomor_telepon.pack()

        self.entry_nomor_telepon = tk.Entry(root, width=50)
        self.entry_nomor_telepon.pack()

        self.label_alamat = tk.Label(root, text="Alamat:")
        self.label_alamat.pack()

        self.entry_alamat = tk.Entry(root, width=50)
        self.entry_alamat.pack()

        # Tambahkan tombol "Simpan" dengan warna biru
        self.btn_simpan = tk.Button(root, text="Simpan", command=self.simpan_siswa, fg="blue")
        self.btn_simpan.pack()

        # Tambahkan tombol "Hapus" dengan warna merah
        self.btn_hapus = tk.Button(root, text="Hapus", command=self.hapus_siswa, fg="red")
        self.btn_hapus.pack()

        self.listbox = tk.Listbox(root, width=80, height=10)
        self.listbox.pack()

    def simpan_siswa(self):
        nama = self.entry_nama.get()
        tanggal_lahir = self.entry_tanggal_lahir.get()
        asal_sekolah = self.entry_asal_sekolah.get()
        nisn = self.entry_nisn.get()
        nama_ayah = self.entry_nama_ayah.get()
        nama_ibu = self.entry_nama_ibu.get()
        nomor_telepon = self.entry_nomor_telepon.get()
        alamat = self.entry_alamat.get()

        if nama and nisn:
            siswa = f"Nama Lengkap: {nama}, Tanggal Lahir: {tanggal_lahir}, Asal Sekolah: {asal_sekolah}, NISN: {nisn}, Nama Ayah: {nama_ayah}, Nama Ibu: {nama_ibu}, Nomor Telepon: {nomor_telepon}, Alamat: {alamat}"
            self.data_siswa.append(siswa)
            self.listbox.insert(tk.END, siswa)
            self.entry_nama.delete(0, tk.END)
            self.entry_tanggal_lahir.delete(0, tk.END)
            self.entry_asal_sekolah.delete(0, tk.END)
            self.entry_nisn.delete(0, tk.END)
            self.entry_nama_ayah.delete(0, tk.END)
            self.entry_nama_ibu.delete(0, tk.END)
            self.entry_nomor_telepon.delete(0, tk.END)
            self.entry_alamat.delete(0, tk.END)

    def hapus_siswa(self):
        selected_index = self.listbox.curselection()

        if selected_index:
            index = selected_index[0]
            self.listbox.delete(index)
            del self.data_siswa[index]

if __name__ == "__main__":
    root = tk.Tk()
    app = DataSiswaApp(root)
    root.mainloop()
