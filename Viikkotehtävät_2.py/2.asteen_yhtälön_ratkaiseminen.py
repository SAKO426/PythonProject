# Ohjelma joka ratkaisee toisen asteen yhtälön
# Kysyy käyttäjältään a, b, ja c arvoa
# Tulostaa lopuksi vastaukset ( neg ja pos)

# Käyttäjä antaa a, b, c
# ax**2 + bx + c = 0
# Ratkaisu riippuu diskriminantista:
# Jos D > 0 = kaksi ratkaisua
# Jos D = 0 = yksi ratkaisu
# Jos D < = ei reaalisia ratkaisuja

# Muistiinpano itselle: 2.Asteen yhtälöitä kerrattava. Onnistuu paperilla kyllä,
# mutta koko funktion hahmottaminen liian heikolla tasolla...

import math

a = float(input("Anna kerroin a: "))
b = float(input("Anna kerroin b: "))
c = float(input("Anna kerroin c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"kaksi ratkaisua: x1 = {x1}, x2 = {x2}")

elif D == 0:
    x = -b / (2*a)
    print(f"Yksi ratkaisu: x = {x}")

else:
    print("Ei reaalisia ratkaisuja ( diskriminantti on < 0).")