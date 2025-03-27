import math

# Input jari-jari
r = float(input("Masukkan jari-jari: "))

# Menghitung hasil
keliling = 2 * math.pi * r
luas_lingkaran = math.pi * r * r
volume_bola = (4/3) * math.pi * r**3
luas_permukaan_bola = 4 * math.pi * r**2

# Menampilkan hasil
print("Keliling lingkaran:", keliling)
print("Luas lingkaran:", luas_lingkaran)
print("Volume bola:", volume_bola)
print("Luas permukaan bola:", luas_permukaan_bola)
