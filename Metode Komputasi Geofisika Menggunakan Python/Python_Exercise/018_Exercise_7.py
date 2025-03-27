# Total durasi percakapan dalam detik
total_detik = 4287

# Konversi ke jam, menit, dan detik
jam = total_detik // 3600  # 1 jam = 3600 detik
sisa_detik = total_detik % 3600
menit = sisa_detik // 60  # 1 menit = 60 detik
detik = sisa_detik % 60

# Menampilkan hasil
print("Waktu percakapan:", jam, "jam", menit, "menit", detik, "detik")
