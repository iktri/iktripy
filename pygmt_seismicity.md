# PyGMT - Plot Seismisitas Gempa

•	Seismisitas adalah distribusi gempabumi secara geografis dan historis. Seismisitas memiliki informasi lokasi, kedalaman, magnitudo, intensitas gempabumi.
•	Seismisitas menunjukkan seberapa aktif pergerakan tektonik suatu daerah, biasanya terjadi pada batas lempeng dan sesar aktif di daratan.
•	Data gempabumi diperoleh dari data katalog yang telah diunduh sebelumnya dari suatu agensi penyedia data gempabumi seperti IRIS, USGS, ISC, BMKG, dll.
•	Selain data gempabumi, data stasiun juga dapat divisualisasikan menggunakan PyGMT.

## Instalasi _Ghostscript_
•	Ghostscript merupakan perangkat lunak tambahan di GMT yang digunakan sebagai penyimpanan gambar hasil visualisasi.
•	Buka anaconda prompt dan ketik script berikut untuk meng-install ghostscript di Anaconda.
conda install -c conda-forge ghostscript
<img width="839" height="111" alt="image" src="https://github.com/user-attachments/assets/2ce71faa-443f-4313-ad31-2dfba0107adc" />
•	Setelah berhasil, bukalah Jupyter Notebook

## Plot Garis Pantai

1.	Buatlah sebuah new python file pada Jupyter Notebook, misalnya dengan nama plot_seismicity.ipynb kemudian buatlah script berikut pada line pertama untuk meng-import pygmt terbaru pada Python

```python
import pygmt
pygmt.__version__
```
Secara otomatis, pygmt yang terdeteksi adalah yang terbaru yaitu versi 0.7.0 (Juli 2022). Jika terjadi error, maka coba upgrade terlebih dahulu xarray yang terbaru dan pygmt terbaru yang infromasinya dapat diperoleh di https://pypi.org/project/xarray/ dan https://pypi.org/project/pygmt/

```python
!pip install --upgrade xarray==2022.10.0
!pip install pygmt==0.7
```

Namun setelah sukses instalasi, jadikan perintah diatas sebagai _comment_ agar tidak ter-eksekusi kembali karena akan menyita waktu.

2.	Untuk visualisasi (plotting), buatlah sebuah figure kosong untuk menempatkan hasil gambar yang nantinya akan dihasilkan dengan menuliskan script berikut:

```python
fig = pygmt.Figure()
```

3.	Berikut adalah _script_ untuk menampilkan garis pantai dengan keterangan:
**shorelines=True** (menunjukkan bahwa benar yang di-plot adalah garis pantai dengan default warna hitam)
**region** berada pada wilayah antara 180oBB – 180oBT dan 80oLU – 80oLS
**projection** merupakan **M** (Mercator) atau proyeksi geografis bumi standar internasional, dengan ukuran 16c (16 cm)
**resolution** c = crude, pilihan resolusi adalah (f)ull, (h)igh, (i)ntermediate, (l)ow, (c)rude

Semakin tinggi resolusi peta, maka semakin berat komputasi dan semakin lama waktu yang dibutuhkan.

```python
fig = pygmt.Figure()

fig.coast(shorelines=True, region=[-180,180,-80,80], projection="M16c", resolution='c')
fig.show()
```

Referensi untuk plotting dapat dilihat pada laman [https://www.pygmt.org/latest/api/index.html](https://www.pygmt.org/latest/api/index.html)

4.	Jika ingin mengganti warna dan tebal garis pantai, dapat mengubah informasi pada shorelines, misalnya dengan mengganti True menjadi 2p, blue (p = pen untuk menunjukkan ketebalan garis pantai, dan blue menunjukkan warna garis pantai menjadi warna biru)

```python
fig = pygmt.Figure()

fig.coast(shorelines="2p,blue", region=[-180,180,-80,80], projection="M16c", resolution='c')
fig.show()
```

5.	Untuk membuka gambar dalam format PDF, dapat menggunakan script berikut:

```python
fig.show(method="external")
```

6.	**Frame** merupakan garis bantu untuk menunjukkan posisi koordinat pada sumbu X (longitude) dan sumbu Y (latitude). 
**frame = ‘f’**				tanpa koordinat di frame
**frame = ‘a’** atau **frame = True**	koordinat di frame
**frame = ‘ag’**			koordinat dan grid line di frame
**frame = ‘40’**			koordinat setiap 40o
**frame = [“xa40g40”, “ya40g40”]**	koordinat setiap 40o di frame dan 40o di grid line
**frame = [“xa40g60”, “ya40g60”]**	koordinat setiap 40o di frame dan 60o di grid line

```python
fig = pygmt.Figure()

fig.coast(shorelines=True, region=[-180,180,-80,80], projection="M16c", frame='af')
fig.show()
```







