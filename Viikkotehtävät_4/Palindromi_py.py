while True:  # Suorittaa ohjelmaa alusta loppuun uudestaan kunnes vastaan tulee "break"

    syöte = input("Anna jokin teksti:\n").lower()

    if syöte == "":
        print("Antamasi teksti on tyhjä") # Ohjelma loppuu tähän jos syöte on tyhjä, muuten jatkuu

    else:
        käännetty = syöte[::-1]

        if syöte == käännetty:
            print("Palindromi: kyllä")

        elif sana != käännetty:
            print("Palindromi: ei")

    #Kysytään haluaako käyttäjä jatkaa
    uudestaan = input("Haluatko kokeilla uudestaan? (k/e):\n").lower()

    if uudestaan != "k":
                    print("Ohjelma päättyi.")
                    break                         # päättyyy