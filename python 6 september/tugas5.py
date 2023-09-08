import turtle

# Inisialisasi modul Turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan menggambar

# Menggambar spiral berwarna
colors = ["red", "blue", "green", "purple"]
for i in range(400):
    t.pencolor(colors[i % 4])
    t.forward(i)
    t.left(91)

# Tutup jendela grafik saat selesai
turtle.done()
