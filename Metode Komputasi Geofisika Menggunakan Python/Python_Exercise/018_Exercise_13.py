def hitung_gaji(golongan):
    upah_per_jam = {
        'A': 50000,
        'B': 40000,
        'C': 30000,
        'D': 20000
    }
    jam_kerja = 40  # Dihitung hanya untuk 40 jam kerja per minggu

    if golongan in upah_per_jam:
        gaji = jam_kerja * upah_per_jam[golongan]
        return gaji
    else:
        return "Golongan tidak valid"

# Input golongan karyawan
golongan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
gaji_mingguan = hitung_gaji(golongan)

if isinstance(gaji_mingguan, int):
    print(f"Total gaji mingguan untuk golongan {golongan}: Rp. {gaji_mingguan}")
else:
    print(gaji_mingguan)
