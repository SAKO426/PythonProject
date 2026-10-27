while True:

    luku = int(input("Anna luku:\n"))

    #Boolean-muuttuja: True jos jaollinen sekä 3:lla että 5:llä
    good_division = False

    #Tarkistetaan jaollisuus

    if luku % 3 == 0 and luku % 5 == 0:
        good_division = True

    else:
        good_division = False

    #Tulostaminen good_divisionin avulla

    if good_division:
        print("Luku on sopiva")

    else:
        print("Luku ei ole sopiva")

    # Luodaan uusi While True silmukka
    while True:
        uudestaan = input("Haluatko kokeilla uudestaan? (k/e)")

        if uudestaan == "k":
            # Jos "k": Tämä silmukka loppuu ja jatkuu ulommassa silmukassa
            break

        elif uudestaan == "e":
            print("Ohjelma päättyy.")
            exit()
        else:
            print("Virheellinen valinta, kirjoita k tai e.")