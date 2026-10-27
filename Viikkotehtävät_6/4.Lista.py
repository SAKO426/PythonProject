
# Kaikki tilauskoodit listattuina.
tilauskoodit = [
    "T1565_2020",
    "T2432_2019",
    "T8511_2018",
    "T3342_2019",
    "T9814_2018",
    "T7733_2020"
]

#Kysytään käyttäjältä minkä vuoden tuotteet haluaa nähdä
vuosi = input("Anna vuosiluku:\n")

print(f"\nTilauskoodit vuodelta {vuosi}:")

#Luodaan ohjelmaan toiminto, joka ilmoittaa, mikäli tuotteita ei ole. Aluksi se on False
löytyi = False


# Splitataan listan tuotteen kategorioihin: "koodi" ja "tilauksen_vuosi" alaviivan mukaan.

for tilaus in tilauskoodit:
    koodi, koodin_vuosi = tilaus.split("_")
    if koodin_vuosi == vuosi:
        print(koodi)
        löytyi = True


# Jos löytyi pysyi False tulostuu tämä, mutta jos se muuttui True se ei tulostu.
if not löytyi:
    print("Ei tilauksia kyseiseltä vuodelta")