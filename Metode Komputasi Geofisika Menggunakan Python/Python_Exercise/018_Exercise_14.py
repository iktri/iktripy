def cari_shio(tahun):
    shio_list = {
        0: "Tikus",
        1: "Kerbau",
        2: "Macan",
        3: "Kelinci",
        4: "Naga",
        5: "Ular",
        6: "Kuda",
        7: "Kambing",
        8: "Monyet",
        9: "Ayam",
        10: "Anjing",
        11: "Babi"
    }

    shio_awal = 1924  # Tahun awal siklus shio
    indeks_shio = (tahun - shio_awal) % 12  # Menghitung indeks shio berdasarkan siklus 12 tahun

    return shio_list[indeks_shio]

# Input tahun lahir
tahun_lahir = int(input("Masukkan tahun lahir: "))
shio = cari_shio(tahun_lahir)

print(f"Tahun {tahun_lahir} memiliki shio {shio}.")
