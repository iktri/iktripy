# Input koordinat
x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))

# Menentukan kuadran
if x > 0 and y > 0:
    print("Titik berada di Kuadran I")
elif x < 0 and y > 0:
    print("Titik berada di Kuadran II")
elif x < 0 and y < 0:
    print("Titik berada di Kuadran III")
elif x > 0 and y < 0:
    print("Titik berada di Kuadran IV")
elif x == 0 and y != 0:
    print("Titik berada di sumbu Y")
elif y == 0 and x != 0:
    print("Titik berada di sumbu X")
else:
    print("Titik berada di titik asal (0,0)")
