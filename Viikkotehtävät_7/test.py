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

for weather in weather:
    print(weather)