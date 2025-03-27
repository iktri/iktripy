import numpy as np

# Load data dari file "Brian.txt"
data = np.genfromtxt("018_Brian.txt", delimiter="\t", dtype=str, skip_header=1)

# Menampilkan data
print("Data dari file Brian.txt:")
print(data)

import csv

# Membaca file Brian.txt
with open("Brian.txt", newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)  # Lewati header
    data = [row for row in reader]

# Menampilkan data
print("Data dari file Brian.txt:")
for row in data:
    print(row)

