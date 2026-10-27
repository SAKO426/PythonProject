# Ohjelma, joka kysyy kesäpäivän lämpötilaa
# Tulostaa riippuen lämpötilasta:
# "KYLMÄÄ", jos lämpötila 0-10 astetta.
# "KOLEAA", jos lämpötila 11-15 astetta.
# "MELKO LÄMMINTÄ", jos lämpötila 16-20 astetta
# "LÄMMINTÄ", jos lämpötila 21-25 astetta.
# "HELLETTÄ", jos lämpötila 26-30 astetta.

# lämpötila = int(input("Syötä päivän lämpötila (0-35C):\n"))

# if 0 <= lämpötila <= 10:
    #print("Kylmää")

# elif 10 <= lämpötila <= 15:
    #print("Koleaa")

# elif 15 <= lämpötila <= 20:
    #print("Melko lämmintä")

# elif 20 <= lämpötila <= 25:
    #print("Lämmintä")

#else:
    #lämpötila >= 25
    #print("Hellettä")

# Kystään pukeutumisvinkkejä:  ohjelma n.1

#pukeutumisvinkit =(input("Haluatko pukeutumisvinkkejä? (kyllä/en): \n""")).lower()
                                         # .lower() muuntaa ISOT kirjaimet pieniksi
# if pukeutumisvinkit == "kyllä":
   # if 0 <= lämpötila <= 10:
#        print("Suosittelen lämmintä takkia ja pitkähihaista, sekä pipo kannattaa laittaa päähän.")

#    elif 11 <= lämpötila <= 15:
#        print("Suosittelen ohutta takkia ja puseroa takin alle.")

#    elif 16 <= lämpötila <= 20:
#        print("Suosittelen ohuita lyhythihaista paitaa/toppia ja hengittäviä housuja.")

#    elif 21 <= lämpötila <= 25:
#       print("Suosittelen shortseja/hametta, sekä hengittävää paitaa.")

#    else:
#        lämpötila >= 26
#        print("Uimapuku/bikinit! Kannattaa pysytellä varjoissa ja muistaa nestytys!")

#else:
#    print("Selvä, ei pukeutumisvinkkejä. ohjelma päättyy.")

#Kystään pukeutumisvinkkejä: Ohjelma n.2
# Käytetään def

def pukeutumisvinkit(lämpötila):

    if 0 <= lämpötila <= 10:
        print("Suosittelen lämmintä takkia ja pitkähihaista, sekä pipo kannattaa laittaa päähän.")

    elif 11 <= lämpötila <= 15:
        print("Suosittelen ohutta takkia ja puseroa takin alle.")

    elif 16 <= lämpötila <= 20:
        print("Suosittelen ohutta lyhythihaista paitaa/toppia ja hengittäviä housuja.")

    elif 21 <= lämpötila <= 25:
       print("Suosittelen shortseja/hametta, sekä hengittävää paitaa.")

    elif 26 <= lämpötila <= 35:
        print("Uimapuku/bikinit! Kannattaa pysytellä varjoissa ja muistaa nestytys!")

lämpötila = int(input("Anna päivän lämpötila (0-35C):\n"))

#Lämpötilan luokittelu
if 0 <= lämpötila <= 10:
    print("Kylmää\n")

elif 10 <= lämpötila <= 15:
    print("Koleaa\n")

elif 15 <= lämpötila <= 20:
    print("Melko lämmintä\n")

elif 20 <= lämpötila <= 25:
    print("Lämmintä\n")

elif lämpötila >= 25:
    print("Hellettä\n")

vastaus = input("Haluatko pukeutumisvinkkejä?:\n").lower()

if vastaus == "kyllä":
    pukeutumisvinkit(lämpötila)
# Jos vastataan "kyllä", ohjelma tulostaa "pukeutumisvinkit" -funktion joka määrittyy
# "lämpötila" -funktion mukaan
# Eli def pukeutumisvinkit(lämpötila) tallentaa funktion muistiin mutta ei suorita sitä
# Jää odottamaan, että se kutsutaan myöhemmin lopussa




