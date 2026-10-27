sana = str(input("Anna salattava sana:\n"))
siirtoluku = int(input("Anna salauksen siirtoluku:\n"))

salattu =""

for merkki in sana:
    # muunnetaan kirjain numeroksi 0-25
    numero = ord(merkki) - ord('a')
    uusi_numero = (numero + siirtoluku) % 26
    uusi_merkki = chr(uusi_numero + ord('a'))
    salattu += uusi_merkki

print("Salattu sana:", salattu)






