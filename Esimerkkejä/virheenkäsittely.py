
try:
    number = input("Anna numero:\n")
    numer = int(number)
    print(f"Numerosi {number}")
except ValueError:
    print("Annoit tekstiä! Aja ohjelma uudelleen!")


try:
    year = input("Anna syntymävuotesi: ")
    year = int(year)
    print(year)
except ValueError:
    print("Vuosi pitää olla pelkkiä numeroita")
    year = 0
print(f"Ohjelma jatkuu, vuosi = {year}")
