
#Kun halutaan tulostaa näitä, niin eka on key ja toinen value
elokuva = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Rikos, Draama",
    "duration": 154
}

print("Tulostus silmukalla:\n")
for key, value in elokuva.items():
    print(f"{key}: {value}")


print("\nTulostus ilman silmukkaa:\n")
print(elokuva["name"])
print(elokuva["year"])
print(elokuva["director"])
print(elokuva["genre"])
print(elokuva["duration"])