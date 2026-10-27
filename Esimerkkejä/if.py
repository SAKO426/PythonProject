# Kysytään käyttäjän ikä ja määritellään lipun hinta sen mukaan
# 0-6 vuotta - hinta 0
# 7-12 vuotta - hinta 5€
# 13-17 vuotta - hinta 10€
# 18 vuotta - hinta 15€

age = input("Anna ikäsi: ") # age on string tyyppinen
age = int(age) # muutetaan string -> int tyyppiseksi

if age <= 6:
    print("Ikäsi on 6 tai alle")

elif 7 <= age <= 12:
    print("Olet 7-12 vuotta")

elif 13 <= age <= 17:
    print("Olet 13-17 vuotta")

elif age >= 18:
    print("Olet 18 vuotta")
