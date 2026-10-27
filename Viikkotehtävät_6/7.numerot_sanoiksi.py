
#Luodaan sanakirja numeroiden sanoille
numerot_sanoina = {
    "0": "nolla",
    "1": "yksi",
    "2": "kaksi",
    "3": "kolme",
    "4": "neljä",
    "5": "viisi",
    "6": "kuusi",
    "7": "seitsemän",
    "8": "kahdeksan",
    "9": "yhdeksän",
    "10": "kymmenen",
}

# Kysytään luku merkkijonona
luku = input("Anna luku (max 5 numeroa)")

# Tarkistetaan pituus
if len(luku) > 5:
    print("Luku on liian pitkä.")

else:
    #muutetaan jokainen merkki sanaksi
    sanat = []
    for merkki in luku:
        if merkki in numerot_sanoina:
            sanat.append(numerot_sanoina[merkki])
        else:
            print("Virhe: syötteen täytyy olla numeroita.")
            break

    else:
        # Tuloostetaan sanat välilyönneillä
        print(" ".join(sanat))