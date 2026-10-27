# Luodaan lista

shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]

# Luodaan silmukka, joka tulostaa nimet
print("Kuitti ostoksistasi:")
print()
for item in shopcart: #Koska tämä on silmukka tulostuu "-" aina ennen nimeä!!
    print("-", item["name"])

#Luodaan muuttuja johon tallennetaan summat
summa = 0

# Luodaan silmukka joka käy summat läpi
for item in shopcart:
    summa += item["price"]

print()

# Tulostetaan summa
print("Yhteensä:", summa, "€")

print("Tervetuloa uudelleen!")