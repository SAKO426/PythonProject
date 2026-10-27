
# Tallennetaan suurin luku tähän muuttujaan. Se on ohjelman alussa 0
suurin = 0


# Luodaan silmukka joka toistuu 5 kertaa
for i in range(5):
    while True:
        try:
            luku = int(input("Anna numero: "))
            if luku > 0:
                break # Kun luku on ok eli positiivinen kokonaisluku alkaa taas uusi silmukka
            else:
                print("Virhe: Anna vain positiivisia kokonaislukuja.")
        except ValueError: # Jos luku ei vastaa integer, tulee VallueError
            print("Virhe: Syötteen täytyy olla kokonaisluku.")

# Jos uusi luku on suurempi kuin suurin tallennettu luku tallentuu se "suurin" -muuttujaan
    if luku > suurin:
        suurin = luku

print("Suurin käyttäjän luku:", suurin)