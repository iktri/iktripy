def hitung_gaji(jam_kerja):
    upah_per_jam = 20000
    upah_lembur_per_jam = 30000
    batas_jam_normal = 40

    if jam_kerja > batas_jam_normal:
        jam_lembur = jam_kerja - batas_jam_normal
        gaji = (batas_jam_normal * upah_per_jam) + (jam_lembur * upah_lembur_per_jam)
    else:
        gaji = jam_kerja * upah_per_jam

    return gaji

# Input jumlah jam kerja
jam_kerja = int(input("Masukkan jumlah jam kerja dalam seminggu: "))
gaji_mingguan = hitung_gaji(jam_kerja)

print(f"Total gaji mingguan: Rp. {gaji_mingguan}")
