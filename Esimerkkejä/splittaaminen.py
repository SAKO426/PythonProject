# tekstin splittaaminen
text = "Elli Esimerkki"
splitted = text.split(" ") # erottaa tekstin kahteen osaan, väli on nyt erottava merkki
print("Etunimi: "+splitted[0] + ",sukunimi: "+splitted[1])

#nimipäivä muodossa dd-mm
name_day = "07-01"

day = name_day[0-2]
month = name_day[3-5]

print(f"Päivä on {day}")
print(f"Kuukausi on {month}")

# Sama split funktion avulla
date = name_day.split(" ")
print(date)
print(f"Päivä on {date[0]}") # Ekassa alkiossa on nyt päivä muistissa
print(f"Kuukausi on {date[1]}") #Tokassa alkiossa on muistissa kuukausi