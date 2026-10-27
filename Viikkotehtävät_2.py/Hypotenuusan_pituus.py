# Lasketaan kolmion hypotenuusan pituus
# c**2 = a**2 + b**2

import math

a = float(input("Anna kolmion ensimmäinen kateetti: "))
print("\n")

b = float(input("Anna kolmion toisen kateetin pituus "))
print("\n")

c = math.sqrt( a**2 + b**2 )

print(f"Hypotenuusan pituus on: {c}cm")
