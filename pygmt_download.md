#PyGMT - Download Data Katalog Gempabumi

Sebelum melakukan visualisasi, terlebih dahulu kita melakukan download data katalog gempabumi yang dapat diambil dari beberapa agensi. Beberapa pengertian dari istilah yang muncul dalam gempabumi adalah:
- Hiposenter merupakan lokasi terjadinya gempabumi dilihat dari kedalaman, jika ditunjukkan dalam koordinat maka hiposenter memiliki posisi (xo, yo, zo). Sedangkan episenter merupakan lokasi terjadinya gempabumi dilihat di permukaan, sebagai proyeksi dari hiposenter. Episenter memiliki posisi (xo, yo). Sementara kedalaman gempabumi disebut sebagai fokus.
- Katalog gempabumi merupakan daftar kejadian gempabumi yang terdiri atas waktu kejadian gempabumi, lokasi, kekuatan gempabumi (magnitudo dan/atau intensitas). Informasi lainnya yang dapat dimasukkan ke dalam katalog gempabumi adalah fasa gempa, waktu tiba gempa di stasiun, dan informasi-informasi lainnya.

_Catalog_ terdiri atas daftar beberapa kejadian gempabumi (event), yang berisikan:
- _Origin_: parameter kejadian gempabumi (latitude, longitude, depth, time, dll)
- _Magnitude_: kekuatan gempabumi
- _Picks_: waktu tiba gempabumi
- _Focal mechanism_: mekanisme fokus
Katalog gempa dapat disimpan dalam file ASCII ataupun Ms. Excel.
![Sumber: https://docs.obspy.org/packages/obspy.core.html](https://github.com/iktri/iktripy/blob/4dbe06948078b66030fa06ecf055ab9ad06ecf09/gambar/download01.png)
Untuk script Python Download_Data.ipynb dapat diakses pada:
[PyGMT-Download Data](https://github.com/iktri/iktripy/blob/dcab169f03c20e5c09c8c828d262e9207fe5ecc9/pygmt/01_download_data.ipynb)

##Download Katalog Gempa

1. _New python file_ telah dibuat di Jupyter Notebook, dengan baris pertama berisi _importing packages_ untuk _library_ yang dibutuhkan dalam pengolahan data seismologi (**pygmt, obspy, pandas, numpy**). Pada _library_ obspy, modul yang diperlukan adalah **Client** (lembaga yang menyediakan data gempabumi) dan juga **UTCDateTime** (waktu _Coordinated Universal Time_ yang menunjukkan standar waktu internasional).
Eksekusi dengan cara klik **Run** atau tekan **Shift + Enter** pada _line_ yang berisikan _script_.

import pygmt
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd
import numpy as np

_Client_ merupakan lembaga yang tergabung dalam _International Federation of Digital Seismograph Networks (FDSN)_ yang menyediakan data seismogram secara _open-source_. Berikut merupakan daftar _Client_ yang dapat diakses:
| **No** | **Agensi**    | **Keterangan**    | **Website**    |
|-----|----------|-------------|-------------|
| 01  | AUSPASS  | The Australian Passive Seismic Server    | http://auspass.edu.au |
| 02  | BGR      | Bundesanstalt fur Geowissenschaften und Rohstoffe | http://eida.bgr.de |
| 03  | EIDA     | European Integrated Data Archive      | http://eida-federator.ethz.ch |

2. Diketahui gempa Tohoku, Jepang 2011 dengan keterangan berikut:
![Sumber: https://commons.m.wikimedia.org/wiki/File:ShakeMap_of_The_2011_off_the_Pacific_coast_of_Tohoku_Earthquake.pdf#/search](https://github.com/iktri/iktripy/blob/dcab169f03c20e5c09c8c828d262e9207fe5ecc9/gambar/download02.jpg)

Misalkan data katalog yang dibutuhkan adalah dengan batasan sebagai berikut: 
| **No** | **Agensi**    | **Keterangan**    | **Website**    |
|-----|----------|-------------|-------------|
| 01  | AUSPASS  | The Australian Passive Seismic Server    | http://auspass.edu.au |
| 02  | BGR      | Bundesanstalt fur Geowissenschaften und Rohstoffe | http://eida.bgr.de |
| 03  | EIDA     | European Integrated Data Archive      | http://eida-federator.ethz.ch |

Maka dapat dituliskan script pada Jupyter sebagai berikut:
 
client = Client("IRIS")
starttime = UTCDateTime("2011-03-01T00:00:00")
endtime = UTCDateTime("2011-03-16T00:00:00")
min_lon = 135
max_lon = 145
min_lat = 35
max_lat = 42

catalog = client.get_events(starttime=starttime, endtime=endtime, minmagnitude=6,
                       minlongitude=min_lon, maxlongitude=max_lon,
                       minlatitude=min_lat, maxlatitude=max_lat)

3. Catalog dibuat dalam kolom time, lon, lat, depth, mag.

lon, lat, depth, mag, time = [], [], [], [], []
for i in range(len(catalog)):
    event = catalog[i]
    origins = event.origins[0]
    time.append(origins.time)
    lon.append(origins.longitude)
    lat.append(origins.latitude)
    depth.append(origins.depth/1000)
    mag.append(event.magnitudes[0].mag)

data = pd.DataFrame({"time":time,"lon":lon, "lat":lat, "depth_km":depth, "mag":mag})

4. Catalog dibuat dalam kolom date dan time yang dipisahkan ke dalam kolom year, month, day, hour, minute, second.

year, month, day, hour, minute, second = [], [], [], [], [], []
for i in range(len(catalog)):
    datetime = UTCDateTime(time[i])
    year.append(datetime.year)
    month.append(datetime.month)
    day.append(datetime.day)
    hour.append(datetime.hour)
    minute.append(datetime.minute)
    second.append(datetime.second + datetime.microsecond/(10**6))

data = pd.DataFrame({"year":year, "month":month, "day":day, "hour":hour, "minute":minute, "second":second, "lon":lon, 
                     "lat":lat, "depth_km":depth, "mag":mag})

5. Catalog disimpan ke dalam format CSV agar dapat dibaca di perangkat lainnya, seperti Ms. Excel.

data.to_csv("Katalog_Gempa_Tohoku_2011.csv")

Maka file CSV akan muncul pada folder yang sama dengan file *.ipynb
File tersebut juga dapat dibuka di Ms. Excel


