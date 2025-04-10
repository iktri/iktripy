# PyGMT - Download Data Katalog Gempabumi

Sebelum melakukan visualisasi, terlebih dahulu kita melakukan download data katalog gempabumi yang dapat diambil dari beberapa agensi. Beberapa pengertian dari istilah yang muncul dalam gempabumi adalah:
- Hiposenter merupakan lokasi terjadinya gempabumi dilihat dari kedalaman, jika ditunjukkan dalam koordinat maka hiposenter memiliki posisi (xo, yo, zo). Sedangkan episenter merupakan lokasi terjadinya gempabumi dilihat di permukaan, sebagai proyeksi dari hiposenter. Episenter memiliki posisi (xo, yo). Sementara kedalaman gempabumi disebut sebagai fokus.
- Katalog gempabumi merupakan daftar kejadian gempabumi yang terdiri atas waktu kejadian gempabumi, lokasi, kekuatan gempabumi (magnitudo dan/atau intensitas). Informasi lainnya yang dapat dimasukkan ke dalam katalog gempabumi adalah fasa gempa, waktu tiba gempa di stasiun, dan informasi-informasi lainnya.

_Catalog_ terdiri atas daftar beberapa kejadian gempabumi (event), yang berisikan:
- _Origin_: parameter kejadian gempabumi (latitude, longitude, depth, time, dll)
- _Magnitude_: kekuatan gempabumi
- _Picks_: waktu tiba gempabumi
- _Focal mechanism_: mekanisme fokus
Katalog gempa dapat disimpan dalam file ASCII ataupun Ms. Excel.

![Sumber: https://docs.obspy.org/packages/obspy.core.html](https://raw.githubusercontent.com/iktri/iktripy/4dbe06948078b66030fa06ecf055ab9ad06ecf09/gambar/download01.png)

Untuk script Python Download_Data.ipynb dapat diakses pada:
[PyGMT-Download Data](https://github.com/iktri/iktripy/blob/dcab169f03c20e5c09c8c828d262e9207fe5ecc9/pygmt/01_download_data.ipynb)

## Download Katalog Gempa

1. _New python file_ telah dibuat di Jupyter Notebook, dengan baris pertama berisi _importing packages_ untuk _library_ yang dibutuhkan dalam pengolahan data seismologi (**pygmt, obspy, pandas, numpy**). Pada _library_ obspy, modul yang diperlukan adalah **Client** (lembaga yang menyediakan data gempabumi) dan juga **UTCDateTime** (waktu _Coordinated Universal Time_ yang menunjukkan standar waktu internasional).
Eksekusi dengan cara klik **Run** atau tekan **Shift + Enter** pada _line_ yang berisikan _script_.

```python
import pygmt
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import pandas as pd
import numpy as np
```

_Client_ merupakan lembaga yang tergabung dalam _International Federation of Digital Seismograph Networks (FDSN)_ yang menyediakan data seismogram secara _open-source_. Berikut merupakan daftar _Client_ yang dapat diakses:
| **No** | **Agensi** | **Keterangan** | **Website** |
|--------|------------|----------------|------------|
| 01     | AUSPASS    | The Australian Passive Seismic Server | [http://auspass.edu.au](http://auspass.edu.au) |
| 02     | BGR        | Bundesanstalt fur Geowissenschaften und Rohstoffe | [http://eida.bgr.de](http://eida.bgr.de) |
| 03     | EIDA       | European Integrated Data Archive | [http://eida-federator.ethz.ch](http://eida-federator.ethz.ch) |
| 04     | EMSC       | European-Mediterranean Seismological Centre | [http://www.seismicportal.eu](http://www.seismicportal.eu) |
| 05     | ETH        | ETH Zurich     | [http://eida.ethz.ch](http://eida.ethz.ch) |
| 06     | GEOFON     | GFZ German Research Center for Geosciences | [http://geofon.gfz-potsdam.de](http://geofon.gfz-potsdam.de) |
| 07     | GEONET     | Geonet New Zealand | [http://service.geonet.org.nz](http://service.geonet.org.nz) |
| 08     | GFZ        | GFZ Potsdam     | [http://geofon.gfz-potsdam.de](http://geofon.gfz-potsdam.de) |
| 09     | ICGC       | Institut Cartografic i Geologic de Catalunya | [http://ws.icgc.cat](http://ws.icgc.cat) |
| 10     | IESDMC     | The Data Management | [http://batsws.earth.sinica.edu.tw](http://batsws.earth.sinica.edu.tw) |
| 11     | INGV       | The Istituto Nazionale di Geofisica e Vulcanologia | [http://webservices.ingv.it](http://webservices.ingv.it) |
| 12     | IPGP       | Institut de Physique du Globe de Paris | [http://ws.ipgp.fr](http://ws.ipgp.fr) |
| 13     | IRIS       | Incorporated Research Institutions for Seismology | [http://service.iris.edu](http://service.iris.edu) |
| 14     | IRISPH5    | Incorporated Research Institutions for Seismology | [http://service.iris.edu](http://service.iris.edu) |
| 15     | ISC        | International Seismological Centre | [http://isc-mirror.iris.washington.edu](http://isc-mirror.iris.washington.edu) |
| 16     | KNMI       | Royal Dutch Meteorological Institute | [http://rdsa.knmi.nl](http://rdsa.knmi.nl) |
| 17     | KOERI      | Kandilli Observatory and Earthquake Research Institute | [http://eida.koeri.boun.edu.tr](http://eida.koeri.boun.edu.tr) |
| 18     | LMU        | Ludwig-Maximilians Universitat Munchen | [http://erde.geophysik.uni-muenchen.de](http://erde.geophysik.uni-muenchen.de) |
| 19     | NCEDC      | The Northern California Earthquake Data Center | [http://service.ncedc.org](http://service.ncedc.org) |
| 20     | NIEP       | The National Institute for Earth Physics | [http://eida-sc3.infp.ro](http://eida-sc3.infp.ro) |
| 21     | NOA        | National Seismic Network | [http://eida.gein.noa.gr](http://eida.gein.noa.gr) |
| 22     | ODC/ORFEUS | ORFEUS Data Center | [http://www.orfeus-eu.org](http://www.orfeus-eu.org) |
| 23     | RASPISHAKE | | [https://fdsnws.raspberryshakedata.com](https://fdsnws.raspberryshakedata.com) |
| 24     | RESIF      | | [http://ws.resif.fr](http://ws.resif.fr) |
| 25     | RESIFPH5   | | [http://ph5ws.resif.fr](http://ph5ws.resif.fr) |
| 26     | SCEDC      | The Southern California Earthquake Data Center | [http://service.scedc.caltech.edu](http://service.scedc.caltech.edu) |
| 27     | TEXNET     | Texas Seismological Network | [http://rtserve.beg.utexas.edu](http://rtserve.beg.utexas.edu) |
| 28     | UIB-NORSAR | Universitas Bergensis-Norwegian Seismic Array | [http://eida.geo.uib.no](http://eida.geo.uib.no) |
| 29     | USGS       | United States Geological Survey | [http://earthquake.usgs.gov](http://earthquake.usgs.gov) |
| 30     | USP        | Centro de Sismologia | [http://sismo.iag.usp.br](http://sismo.iag.usp.br) |

2. Diketahui gempa Tohoku, Jepang 2011 dengan keterangan berikut:
![Sumber: ShakeMap of The 2011 off the Pacific coast of Tohoku Earthquake](https://github.com/iktri/iktripy/blob/dcab169f03c20e5c09c8c828d262e9207fe5ecc9/gambar/download02.jpg?raw=true)

Misalkan data katalog yang dibutuhkan adalah dengan batasan sebagai berikut: 

|        | **Min**        | **Max**        |
|--------|----------------|----------------|
| Time   | 1 Maret 2011   | 15 Maret 2011  |
| Longitude | 135°E        | 145°E          |
| Latitude  | 35°N          | 42°N           |
| Depth    | -              | -              |
| Magnitude | 6            | -              |

Maka dapat dituliskan _script_ pada Jupyter sebagai berikut:

```python
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
```

3. _Catalog_ dibuat dalam kolom _time, lon, lat, depth, mag_.

```python
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
```

4. _Catalog_ dibuat dalam kolom _date_ dan _time_ yang dipisahkan ke dalam kolom _year, month, day, hour, minute, second._

```python
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
```

5. _Catalog_ disimpan ke dalam format CSV agar dapat dibaca di perangkat lainnya, seperti Ms. Excel.

```python
data.to_csv("Katalog_Gempa_Tohoku_2011.csv")
```

Maka file CSV akan muncul pada folder yang sama dengan file ***.ipynb**
File tersebut juga dapat dibuka di Ms. Excel


