import tkinter as tk

def hitung_total():
    harga_barang = float(entry_harga_barang.get())
    jumlah_barang = int(entry_jumlah_barang.get())
    total = harga_barang * jumlah_barang
    label_total.config(text=f"Total: Rp {total:.2f}")

# Buat jendela utama
root = tk.Tk()
root.title("Program Kasir")

# Label Harga Barang
label_harga_barang = tk.Label(root, text="Harga Barang (Rp):")
label_harga_barang.pack()

# Entry Harga Barang
entry_harga_barang = tk.Entry(root)
entry_harga_barang.pack()

# Label Jumlah Barang
label_jumlah_barang = tk.Label(root, text="Jumlah Barang:")
label_jumlah_barang.pack()

# Entry Jumlah Barang
entry_jumlah_barang = tk.Entry(root)
entry_jumlah_barang.pack()

# Tombol Hitung
tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()

# Label Total
label_total = tk.Label(root, text="")
label_total.pack()

# Menjalankan aplikasi
root.mainloop()
