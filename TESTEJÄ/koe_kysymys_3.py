opiskelijat = []

while True:

    toiminto = input(
        "\n1 = Lisää opiskelija\n"
        "2 = Hae opiskelija\n"
        "0 = Lopeta\n"
        "Valinta: "
    )

    if toiminto == "1":

        tiedot = input(
            "Syötä nimi, syntymävuosi ja arvosana pilkulla eroteltuna: "
        )

        nimi, vuosi, arvosana = tiedot.split(",")

        opiskelijat.append({
            "name": nimi,
            "year": int(vuosi),
            "grade": int(arvosana)
        })

    elif toiminto == "2":

        haettava = input("Syötä haettava nimi: ")

        loydetty = False

        for opiskelija in opiskelijat:

            if opiskelija["name"] == haettava:

                print(f"Nimi: {opiskelija['name']}")
                print(f"Syntymävuosi: {opiskelija['year']}")
                print(f"Arvosana: {opiskelija['grade']}")

                loydetty = True
                break

        if not loydetty:
            print("Nimellä ei löytynyt tietoja.")

    elif toiminto == "0":
        break

    else:
        print("Virheellinen valinta.")