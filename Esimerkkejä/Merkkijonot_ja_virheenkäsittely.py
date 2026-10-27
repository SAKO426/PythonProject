# Yhdistetään kaksi merkkijonoa
first_name =input("Anna etunimesi: ")
last_name = input("Anna sukunimesi: ")

full_name = first_name + " " + last_name
print(f"Koko nimesi on: {full_name}")

full_name = first_name + " " + last_name
print(full_name)
name_length = len(full_name.replace(" ", "")) # lasketaan montako merkkiä.  -1 koska poistetaan välilyönti
print(f"Nimessäsi on {name_length} merkkiä. ")

# tekstin splittaaminen
text = "Elli Esimerkki"
splitted = text.split(" ") # erottaa tekstin kahteen osaan, väli on nyt erottava merkki
print("Etunimi: "+splitted[0] + ",sukunimi: "+splitted[1])

