
#Luodaan silmukka
while True:
    try:
        luku = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman."))

        # Luodaan ohjelman lopetus komento
        if luku == 0:
            print("Ohjelma loppui.")
            break

        # Kertotaulun tulostus mikäli syötetty luku on 1 tai 10 tai siltä väliltä
        if 1 <= luku <= 10:
            for i in range(1, 11):
                print(f"{luku} x {i} = {luku * i}")
            print()

        else:
            print("Väärä luku. \n")


    except ValueError:
        print("Syötteen täytyy olla kokonaisluku. \n")