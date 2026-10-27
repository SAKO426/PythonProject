
import random
import string

# Kysytään merkkimäärä
merkkimäärä = int(input("Monenko merkin salasanan haluat?"))

if merkkimäärä < 8:
    print("Salasanan täytyy olla vähintään 8 merkkiä.")

else:
    pienet =  string.ascii_lowercase
    isot = string.ascii_uppercase
    numerot = string.digits
    erikoismerkit = "_~?$#!+%@"

    # Varmistetaan että jokainen vaatimus täyttyy
    salasana = [
        random.choice(pienet),
        random.choice(isot),
        random.choice(numerot),
        random.choice(erikoismerkit),
    ]

# Loput merkit satunnaisesti kaikista merkeistä
kaikki = pienet + isot + numerot + erikoismerkit

for _ in range(merkkimäärä - 4):
    salasana.append(random.choice(kaikki))

# Sekoitetaan järjestys

random.shuffle(salasana)

# Muutetaan lista merkkijonoksi
salasana = "".join(salasana)

print("Ehdotettu salasana: " + salasana)