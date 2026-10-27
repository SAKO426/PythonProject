print("Hello World!")
print("Samu Koponen")
print("1999")
print("Kokeilukatu 666 15 a, 12345 Vuokatti")
print()

hinta = float(input("Anna hinta ilman alv: "))
hinta_alv = hinta * 1.24
print(f"Hinta alv:n kanssa: {hinta_alv: .2f} €")
print()
print()
#SELITYKSET
# input =
# tulostaa tekstin konsoliin: Anna hinta ilman alv:
# Ohjelma pysähtyy ja odottaa, että käyttäjä kirjoittaa numeron konsoliin, EI KOODIIN!
# Syöte palautuu ohjelmaan tekstinä

# float =
# koska input palauttaa vastauksen tekstinä, sitä ei voi laskea. Siksi käytetään float()
# ilman floatia python ei voi tehdä siitä laskua

# f =
# "Tämän merkkijonon sisällä on muuttujia"
# ilman f-kirjainta {} ei toimisi

# {} =
# muuttujia tekstin sisällä
# Tämä kertoo pythonille: "laita tähän kohtaan muuttujan arvo"

# .2f =
# muotoilee kahdella desimaalilla
# .2 = kaksi desimaalia
# f = floating point number


matka = float(input("Anna matkan pituus (km): "))
kulutus_per_100km = float(input("Anna arvioitu keskikulutus per 100km (l): "))

kulutus = matka * kulutus_per_100km / 100

print(f"Kulutus: {kulutus:.1f} litraa")
print("\n")

# // = kokonaislukujako
# % = jakojäännös
# input() = palauttaa aina tekstin (string), vaikka käyttäjä kirjoittaisi numeron
# eli kun laittaa käyttäjä laittaa 67, python näkee sen "67"
# int() = muuttaa tekstin numeroksi

minuutit = int(input("Anna minuutit: "))
tunnit = minuutit // 60
jäännös = minuutit % 60
print(f"{tunnit}h {jäännös}min")
print("\n")

raha = int(input("Anna 1-100 senttiä: "))
kolikot50 = raha // 50
jäljellä = raha % 50

kolikot20 = jäljellä // 20
jäljellä = jäljellä % 20

kolikot10 = jäljellä // 10
jäljellä = jäljellä % 10

kolikot5 = jäljellä // 5
jäljellä = jäljellä % 5

kolikot2 = jäljellä // 2
jäljellä = jäljellä % 2

kolikot1 = jäljellä // 1
jäljellä = jäljellä % 1
print()
print(f"50 snt kolikoita {kolikot50} kpl)")
print(f"20 snt kolikoita {kolikot20} kpl")
print(f"10 snt kolikoita {kolikot10} kpl")
print(f"5 snt kolikoita {kolikot5} kpl")
print(f"2 snt kolikoita {kolikot2} kpl")
print(f"1 snt kolikoita {kolikot1} kpl")
print()
