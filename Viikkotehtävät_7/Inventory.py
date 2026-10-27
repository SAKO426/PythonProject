# Tehdään kolme listaa: fruits, berries ja vegetables

fruits = ["apple", "pear", "banana"]

berries = ["strawberry", "blueberry", "blackberry"]

vegetables = ["carrot", "kale", "cucumber"]

# Luodaan uusi lista, joka sisältää
# aiemmat kolme listaa

inventory = [fruits, berries, vegetables]


# Luodaan silmukka toisen silmukan sisään
# Mitä tapahtuu:
# Lista saa arvon fruits ja käy sen läpi
# Lista saa arvon berries ja käy sen läpi
# Lista saa arvon vegetables ja käy sen läpi

# Koska listan sisällä on kaksi listaa
# Tarvitaan kaksi silmukkaa: Ulommalle ja sisemmälle

for lista in inventory:
    for sana in lista:
        print(sana)

