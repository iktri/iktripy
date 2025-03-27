# Input gaji pokok
gaji_pokok = float(input("Masukkan gaji pokok: "))

# Menghitung tunjangan dan pajak
tunjangan = 0.2 * gaji_pokok
pajak = 0.15 * (gaji_pokok + tunjangan)

# Menghitung gaji bersih
gaji_bersih = gaji_pokok + tunjangan - pajak

# Menampilkan hasil
print("Gaji Bersih Karyawan adalah:", gaji_bersih)
