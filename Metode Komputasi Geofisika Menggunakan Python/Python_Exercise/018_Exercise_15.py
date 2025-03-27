import numpy as np

# Membaca data dari file
data = np.genfromtxt("Data_den.txt", delimiter="\t", skip_header=1)

# Loop untuk menghitung galat dan menampilkan hasil
for row in data:
    titik = int(row[0])
    pengamatan = row[1]
    perhitungan = row[2]
    galat = abs(perhitungan - pengamatan)

    if galat > 0.015:
        print(f"Titik {titik} mempunyai galat > 0.015 yaitu {galat:.6f}")
    else:
        print(f"Titik {titik} mempunyai galat < 0.015 yaitu {galat:.6f}")
