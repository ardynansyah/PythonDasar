import tkinter as tk
from datetime import datetime

class ParkirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Parkir")

        self.entry_plat = tk.Entry(root, width=30)  # Lebar textbox diperbesar
        self.entry_plat.grid(row=0, column=1, padx=10, pady=10)
        self.label_plat = tk.Label(root, text="Nomor Plat:")
        self.label_plat.grid(row=0, column=0, padx=10, pady=10)

        self.btn_masuk = tk.Button(root, text="Masuk", command=self.masuk_parkir)
        self.btn_masuk.grid(row=1, column=0, padx=10, pady=10)
        self.btn_keluar = tk.Button(root, text="Keluar", command=self.keluar_parkir)
        self.btn_keluar.grid(row=1, column=1, padx=10, pady=10)

        self.label_waktu_masuk = tk.Label(root, text="Waktu Masuk:")
        self.label_waktu_masuk.grid(row=2, column=0, padx=10, pady=10)
        self.label_waktu_keluar = tk.Label(root, text="Waktu Keluar:")
        self.label_waktu_keluar.grid(row=3, column=0, padx=10, pady=10)
        self.label_lama_parkir = tk.Label(root, text="Lama Parkir:")
        self.label_lama_parkir.grid(row=4, column=0, padx=10, pady=10)
        self.label_biaya_parkir = tk.Label(root, text="Biaya Parkir (Rp):")
        self.label_biaya_parkir.grid(row=5, column=0, padx=10, pady=10)

        # Tambahkan label biaya per jam dengan warna merah
        self.label_biaya_per_jam = tk.Label(root, text="Biaya per jam Rp. 2000", fg="red")
        self.label_biaya_per_jam.grid(row=6, column=0, columnspan=2, padx=10, pady=(0, 10))

        self.entry_waktu_masuk = tk.Entry(root, state='disabled', width=30)  # Lebar textbox diperbesar
        self.entry_waktu_masuk.grid(row=2, column=1, padx=10, pady=10)
        self.entry_waktu_keluar = tk.Entry(root, state='disabled', width=30)  # Lebar textbox diperbesar
        self.entry_waktu_keluar.grid(row=3, column=1, padx=10, pady=10)
        self.entry_lama_parkir = tk.Entry(root, state='disabled', width=30)  # Lebar textbox diperbesar
        self.entry_lama_parkir.grid(row=4, column=1, padx=10, pady=10)
        self.entry_biaya_parkir = tk.Entry(root, state='disabled', width=30)  # Lebar textbox diperbesar
        self.entry_biaya_parkir.grid(row=5, column=1, padx=10, pady=10)

        self.waktu_masuk = None
        self.data_pelanggan_terakhir_keluar = []
        self.data_pelanggan_banyak_bayar = []

    def masuk_parkir(self):
        self.waktu_masuk = datetime.now()
        self.entry_waktu_masuk.config(state='normal')
        self.entry_waktu_masuk.delete(0, 'end')
        self.entry_waktu_masuk.insert(0, self.waktu_masuk.strftime('%Y-%m-%d %H:%M:%S'))
        self.entry_waktu_masuk.config(state='disabled')

    def keluar_parkir(self):
        if self.waktu_masuk:
            waktu_keluar = datetime.now()
            lama_parkir = waktu_keluar - self.waktu_masuk
            biaya_per_jam = 2000  # Biaya per jam, Rp 2000

            # Hitung biaya parkir
            biaya_parkir = lama_parkir.total_seconds() / 3600 * biaya_per_jam
            self.entry_waktu_keluar.config(state='normal')
            self.entry_waktu_keluar.delete(0, 'end')
            self.entry_waktu_keluar.insert(0, waktu_keluar.strftime('%Y-%m-%d %H:%M:%S'))
            self.entry_waktu_keluar.config(state='disabled')
            self.entry_lama_parkir.config(state='normal')
            self.entry_lama_parkir.delete(0, 'end')
            self.entry_lama_parkir.insert(0, str(lama_parkir))
            self.entry_lama_parkir.config(state='disabled')
            self.entry_biaya_parkir.config(state='normal')
            self.entry_biaya_parkir.delete(0, 'end')
            self.entry_biaya_parkir.insert(0, '{:.2f}'.format(biaya_parkir))
            self.entry_biaya_parkir.config(state='disabled')
            self.waktu_masuk = None

            # Tambahkan data pelanggan terakhir keluar
            self.data_pelanggan_terakhir_keluar.append({
                "Plat": self.entry_plat.get(),
                "Waktu Keluar": waktu_keluar.strftime('%Y-%m-%d %H:%M:%S'),
                "Biaya Parkir": biaya_parkir
            })

            # Tambahkan data pelanggan dengan biaya parkir tertinggi
            if not self.data_pelanggan_banyak_bayar or biaya_parkir > self.data_pelanggan_banyak_bayar[0]["Biaya Parkir"]:
                self.data_pelanggan_banyak_bayar = [{
                    "Plat": self.entry_plat.get(),
                    "Waktu Keluar": waktu_keluar.strftime('%Y-%m-%d %H:%M:%S'),
                    "Biaya Parkir": biaya_parkir
                }]
            elif biaya_parkir == self.data_pelanggan_banyak_bayar[0]["Biaya Parkir"]:
                self.data_pelanggan_banyak_bayar.append({
                    "Plat": self.entry_plat.get(),
                    "Waktu Keluar": waktu_keluar.strftime('%Y-%m-%d %H:%M:%S'),
                    "Biaya Parkir": biaya_parkir
                })

if __name__ == "__main__":
    root = tk.Tk()
    app = ParkirApp(root)
    root.mainloop()
