#Pallon tilavuus

# Lisää ohjelmaan toiminto, joka kysyy pallon sädettä ja laskee pallon
# tilavuuden. Ohjelmassa käytetään kaavaa 𝑉𝑉 =4/3 · 𝜋 · 𝑟3. Pyöristä
# tulos kahteen desimaaliin.
# Huom! Tarkista laskeeko ohjelma pallon tilavuuden oikein, esim. arvolla
# r = 1.0 tilavuus V = 4.19

import math

r = float(input("Anna pallon säde (cm): "))

pallon_tilavuus = (4/3) * math.pi * r**3

pallon_tilavuus = round(pallon_tilavuus, 2)

print(f"Pallon tilavuus: {pallon_tilavuus}cm")
print("\n")