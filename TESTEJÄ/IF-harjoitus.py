# Kystään käyttäjän ikä. jos alle 18 == alaikäinen, jos yli 18 aikuinen

def iän_tarkistus():

    ikä = int(input("Syötä ikä:\n"))

    if ikä < 18:
        print("Alaikäinen")

    elif ikä >= 18:
        print("Aikuinen")


iän_tarkistus()
