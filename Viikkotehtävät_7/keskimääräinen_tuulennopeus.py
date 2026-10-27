import json
import urllib.request

# Tallennetaan verkkosivuston osoite muttujaan url
url =  "https://edu.frostbit.fi/api/weather/"

# Luodaan HTTP- pyyntö
req = urllib.request.Request(url)

# Tässä tapahtuu varsinainen haku internetistä.
# .req() avaa yhteyden palvelimeen
# .read() Lukee sieltä saadun datan
# .decode("UTF-8") muuttaa datan tekstiksi
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# Muutetaan JSON-teksti Pythonin tietorakenteeksi (lista+sanakirja)
weather = json.loads(raw_data)


# Näihin muuttujiin tallennetaan tiedot ka laskemista varten
lapland_summa = 0
lapland_lkm = 0

middle_summa = 0
middle_lkm = 0

south_summa = 0
south_lkm = 0


# Silmukka joka lisää tiedot muuttujiin.
for paikka in weather:

    if paikka["area"] == "lapland":
        lapland_summa += paikka["wind"]
        lapland_lkm += 1

    elif paikka["area"] == "middle":
        middle_summa += paikka["wind"]
        middle_lkm += 1

    elif paikka["area"] == "south":
        south_summa += paikka["wind"]
        south_lkm += 1

print(f"Keskimääräinen tuuli, Lappi: {lapland_summa / lapland_lkm:.2f} m/s")

print(f"Keskimääräinen tuuli, Maan keskiosa: {middle_summa / middle_lkm:.2f} m/s")

print(f"Keskimääräinen tuuli, Etelä-Suomi: {south_summa / south_lkm:.2f} m/s")