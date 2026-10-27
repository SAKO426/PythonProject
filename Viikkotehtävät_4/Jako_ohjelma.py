while True:
    try:
        eka_numero = float(input("Anna ensimmäinen numero:\n"))
        toka_numero = float(input("Anna toinen numero:\n"))

        if toka_numero == 0:
            print("Nollalla ei saa jakaa\n")

        else:
            tulos = eka_numero / toka_numero
            print(f"{eka_numero} / {toka_numero} = {tulos}\n")

    #Ohjelma odottaa floattia eli numeroa, mutta jos se ei tunnista numeroa tulee value error
    except ValueError:
        print("Virheellinen muoto")

    uudestaan = input("haluatko jatkaa laskuja? (k/e)\n").lower()

    if uudestaan != "k":
        print("Ohjelma päättyi")
        break