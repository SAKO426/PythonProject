# Ohjelma, joka pyytää pistemäärän ja tulostaa sitä vastaavan arvosanan.
# Ilmoittaa käyttäjälle jos annettu pistemäärä ei ole mahdollinen
# eli pienempi kuin 0 tai yli 100


#pisteet

pisteet = float(input("Anna pistemäärä: "))

def arvosana(pisteet): # Määritetään funktio.
    if pisteet < 0 or pisteet > 100:
        print ("Pistemäärä ei ole mahdollinen.\n")

    elif 0 <= pisteet <= 50:
        print ("Arvosana: 0")

    elif 51 <= pisteet <= 60:
        print ("Arvosana: 1")

    elif 61 <= pisteet <= 70:
        print ("Arvosana: 2")

    elif 71 <= pisteet <= 80:
        print ("Arvosana: 3")

    elif 81 <= pisteet <= 90:
        print ("Arvosana: 4")

    elif 91 <= pisteet <= 100:
        print ("Arvosana: 5")


arvosana(pisteet) # Kutsutaan määritetty funktio.