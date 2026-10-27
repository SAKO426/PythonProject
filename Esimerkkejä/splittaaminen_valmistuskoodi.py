#Tutkitaan tuotekoodia ja paloitellaan se osiin, niin että päästään
# olennaiseen dataan käsiksi
tuotekoodi = "kia-2019-8500"

# erotetaan data omiin alkioihin
data = tuotekoodi.split("-")
print(data)

print(f"Merkki: {data[0]}, \nvalmistusvuosi: {data[1]}, \nHinta: {data[2]}")

