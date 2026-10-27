# Ohjelma, joka laskee viikkopalkan
# Työtuntien ja tuntipalkan mukaan
# Ylitöistä maksetaan 50% korotus
# Ylitöitä ovat kaikki 40 tunnin yli menevät tunnit



# Määritetään miten palkka lasketaan ylitöiden kanssa ja ilman: (def, if ja else)

def laske_viikkopalkka(tunnit, tuntipalkka):
    if tunnit > 40:                                   #Jos ylitöitä niin laskee tämän.
        ylityöt = tunnit -40                          # Yli 40 menevät tunnit.
        peruspalkka = 40 * tuntipalkka                # peruspalkka ennen ylitöitä.
        ylityöpalkka = ylityöt * (tuntipalkka * 1.5)  # esim. 5h * (15€ * 50%)
        return peruspalkka + ylityöpalkka

    else:                                             #Jos ei ylitöitä laskee tämän mukaan
        return tunnit * tuntipalkka


#Käyttäjän syötteet
tunnit = float(input("Syötä viikon työtunnit:\n"))

tuntipalkka = float(input("Syötä tuntipalkka:\n"))

#laskenta
palkka = laske_viikkopalkka(tunnit, tuntipalkka)

print(f"Viikkopalkkasi on {palkka: .2f} €")     # .2f määrittää vastauksen 0.00 tarkkuudelle