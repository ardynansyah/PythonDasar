import turtle

# Fungsi menggambar pohon Fibonacci
def fibonacci_tree(branch_len, t):
    if branch_len < 5:
        return
    else:
        t.forward(branch_len)
        t.right(20)
        fibonacci_tree(branch_len - 15, t)
        t.left(40)
        fibonacci_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

# Inisialisasi turtle
turtle.speed(1)
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.color("green")

# Gambar pohon Fibonacci dengan panjang awal 100
fibonacci_tree(100, turtle)

# Tutup jendela saat selesai
turtle.exitonclick()