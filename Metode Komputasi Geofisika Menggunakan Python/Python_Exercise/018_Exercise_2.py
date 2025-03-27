# Data barang dan harga
barang = ["Biskuit", "Deodorant", "Shampoo", "Deterjen", "Mug", "Handuk", "Kopi", "Sarung", "Tumbler", "Panci"]
harga = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Cashback OVO 30% dengan maksimum Rp 25.000
maks_cashback = 25000
persentase_cashback = 0.3

print("Biaya belanja Brian jika menggunakan OVO:")

# Loop untuk setiap barang
for i in range(len(barang)):
    cashback = harga[i] * persentase_cashback  # Hitung cashback 30%

    if cashback > maks_cashback:
        cashback = maks_cashback  # Batasi cashback maksimum Rp 25.000

    total_bayar = harga[i] - cashback  # Hitung total setelah cashback
    print(f"{barang[i]}: Rp {total_bayar:,}")  # Format output dengan pemisah ribuan
