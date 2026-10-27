# Luodaan elokuva lista

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

# Tulostetaan otsikko
print("Seuraavat elokuvat on julkaistu 2000-luvulla:\n")

# Luodaan silmukka uusille
for uudet in elokuvat:
    if uudet["year"] >= 2000:
        print(uudet["name"], uudet["year"])

print()
print("=========================================")
print()

print("Seuraavat elokuvat on julkaistu ennen 2000-lukua:\n")

# Luodaan silmukka vanhoille
for vanhat in elokuvat:
    if vanhat["year"] < 2000:
        print(vanhat["name"], vanhat["year"])
