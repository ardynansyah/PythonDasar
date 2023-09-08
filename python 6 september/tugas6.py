import turtle

# Inisialisasi modul Turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan menggambar

# Menggambar lingkaran warna biru (lingkaran luar)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(100)
t.end_fill()

# Menggambar lingkaran warna putih (lingkaran dalam)
t.penup()
t.goto(0, -100)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(70)  # Ubah radius sesuai kebutuhan
t.end_fill()

# Menambahkan tulisan dengan warna hitam di tengah lingkaran
t.penup()
t.goto(0, -120)  # Posisi tengah lingkaran
t.pendown()
t.color("black")  # Ubah warna tulisan menjadi hitam
t.hideturtle()
t.write("SMK Prestasi Prima", align="center", font=("Arial", 14, "bold"))

# Tutup jendela grafik saat selesai
turtle.done()
