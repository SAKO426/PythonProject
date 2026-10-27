# Ohjelma, joka kysyy kaksi kokonaislukua
# Tulostaa suuremman luvun takaisin näytölle
# Jos numerot yhtä suuria, tulostaa tekstin
# "Numerot ovat yhtä suuria"

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

if luku1 > luku2:
    print (f"Suurempi luku = {luku1}")

elif luku1 < luku2:
    print (f"Suurempi luku = {luku2}")

else:
    print ("Numerot ovat yhtä suuria.")