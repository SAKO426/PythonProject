#Arvotaan satunnaisia lukuja
#Satunnaislukuja varten on olemassa oma "random" -kirjasto

import random
guess = random.randint(1,10)
print(f"Arvottu luku: {guess}")
print("\n")

# Tulostaa näytölle suorakulmion pinta-alan (a*b), jossa kahden eri sivun
# pituudet on arvottu 2:n ja 10:n välillä. Tulostaa arvottujen sivujen pituudet
# sekä laskee pinta-alan.

sivu_a = random.randint(2,10)
sivu_b = random.randint(2,10)

print(f"Arvottu 1. sivu a: {sivu_a}")
print(f"Arvottu 2. sivu b: {sivu_b}")
print(f"Arvotuista sivuista laskettu pinta-ala: {sivu_a*sivu_b}")