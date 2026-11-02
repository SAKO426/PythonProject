



nimilista = []


while True:

    toiminto = (input("1: Lisää nimi.\n"
                         "2: Näytä nimet.\n"
                         "3: Poista nimi.\n"
                         "4. Lopeta.\n"
                      "======================================\n"))

    if toiminto == "1":

        lisättävä_nimi = input("Syötä nimi jonka haluat lisätä:\n")
        nimilista.append(lisättävä_nimi)

    elif toiminto == "2":
        print("\nNimet:\n")

        for nimet in nimilista:
            print(nimet)


    elif toiminto == "3":
        poistettava = input("Poistetaan nimi:\n")

        if poistettava in nimilista:
            nimilista.remove(poistettava)
        else:
            print("Nimeä ei löytynyt")

    elif toiminto == 4:
        break

    else:
        print("Syötä luku 1-4")




