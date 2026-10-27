import json
import urllib.request

# Tallennetaan verkkosivuston osoite muttujaan url
url = "https://edu.frostbit.fi/api/weather/"

# Luodaan HTTP- pyyntö
req = urllib.request.Request(url)

# Tässä tapahtuu varsinainen haku internetistä.
# .req() avaa yhteyden palvelimeen
# .read() Lukee sieltä saadun datan
# .decode("UTF-8") muuttaa datan tekstiksi
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# Muutetaan JSON-teksti Pythonin tietorakenteeksi (lista+sanakirja)
weather = json.loads(raw_data)

# Weather- muuttujan voi tulostaa ensin tarkastaakseen
# Mitä avaimia sanakirjassa on
# Esimerkkejä:
# print(weather)
# print(weather[0])
# print(weather[0]["location"])
# Luodaan silmukka, jolla saadaan jokainen

# Tällä voit tarkistaa listan avaimet
# for station in weather:
# print(station)



# Muuttujat johon tallennetaan
eniten_tuulee = weather [0]
vähiten_tuulee = weather [0]


for paikka in weather:
    if paikka ["wind"] > eniten_tuulee ["wind"]:
        eniten_tuulee = paikka

    if paikka["wind"] < vähiten_tuulee ["wind"]:
        vähiten_tuulee = paikka


print(f"Tänään eniten tuulee sijainnissa: {eniten_tuulee['location']}, {eniten_tuulee['wind']} m/s")

print(f"Tänään vähiten tuulee sijainnissa: {vähiten_tuulee['location']}, {vähiten_tuulee['wind']} m/s")


