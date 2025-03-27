def hitung_tarif(durasi):
    total_biaya = 0

    if durasi > 5 * 60:
        total_biaya += 5000  # 5 menit pertama
        durasi -= 5 * 60
    else:
        return 5000  # Jika kurang dari 5 menit, tetap Rp. 5000

    if durasi > 15 * 60:
        total_biaya += 15 * 60 * 10  # 15 menit berikutnya (Rp. 10/detik)
        durasi -= 15 * 60
    else:
        return total_biaya + durasi * 10

    if durasi > 30 * 60:
        total_biaya += 30 * 60 * 5  # 30 menit berikutnya (Rp. 5/detik)
        durasi -= 30 * 60
    else:
        return total_biaya + durasi * 5

    total_biaya += durasi * 1  # Tarif Rp. 1/detik untuk sisa waktu

    return total_biaya

# Contoh penggunaan
durasi_panggilan = 4287  # Durasi dalam detik
tarif = hitung_tarif(durasi_panggilan)
print(f"Total tarif percakapan: Rp. {tarif}")
