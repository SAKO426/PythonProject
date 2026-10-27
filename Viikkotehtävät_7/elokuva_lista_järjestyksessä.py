# Luodaan elokuva lista, joka tulostaa elokuvat
# Järjestykseen vuosiluvun mukaan.

# .sort() järjestää listan, ei luo uutta listaa

# key kertoo millä perusteella järjestetään

# lambda luo pienen väliaikaisen funktion

# x tarkoittaa yhtä elokuvaa kerrallaan listasta

# x[year] hakee kyseisen elokuvan vuosiluvun



elokuvat = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Lapin sota", "year": 2026},
    {"name": "GTA VI", "year": 2035},
    {"name": "Inception", "year": 2010},
    {"name": "Wolf Of Wall Street", "year": 2013},
    {"name": "Tuntematon sotilas", "year": 1955}
]

# Luodaan tyhjät listat
vanhat =[]

uudet =[]

# Jaetaan elokuvat listoihin
for elokuva in elokuvat:
    if elokuva["year"] < 2000:
        vanhat.append(elokuva)
    else:
        uudet.append(elokuva)

#Järjestetään vuoden mukaan
vanhat.sort(key=lambda x: x["year"])
uudet.sort(key=lambda x: x["year"])

# Tulostetaan vanhat
print("Seuraavat elokuvat ovat ennen 2000-lukua:\n")

for elokuva in vanhat:
    print(elokuva["name"], elokuva["year"])

print()
print("===========================================")
print()

# Tulostetaan uudet
print("Seuraavat elokuvat ovat 2000-luvulta:\n")

for elokuva in uudet:
    print(elokuva["name"], elokuva["year"])