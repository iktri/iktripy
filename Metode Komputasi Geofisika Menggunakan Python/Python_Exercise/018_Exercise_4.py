# Input tahun kelahiran
tahun = int(input("Masukkan tahun kelahiran: "))

# Menentukan generasi
if 1945 <= tahun <= 1960:
    generasi = "Baby Boomers"
elif 1961 <= tahun <= 1980:
    generasi = "X"
elif 1981 <= tahun <= 1994:
    generasi = "Y"
elif 1995 <= tahun <= 2010:
    generasi = "Z"
elif 2011 <= tahun <= 2019:
    generasi = "Alpha"
else:
    generasi = "Tahun tidak termasuk dalam kategori generasi yang ada"

# Menampilkan hasil
print("Anda termasuk generasi:", generasi)
