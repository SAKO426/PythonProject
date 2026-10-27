# Ohjelma laskee kirjeiden ja pakettien lähetyshintoja

# Kirjeiden hinnat:
#   perushinta: 0.50€
#   jos paino 200g-500g: + 0.04€ / 100g
#   Jos paino yli 500g: + 0.07€ / 100g
#   yli 500g kirjeistä peritään 2€ lisämaksu jos kirje ei mahdu postilaatikkoon

#pakettien hinnat:

#   perushinta: 2€
#   jos paino 200g-500g: + 0.08€ /100g
#   jos paino yli 500g: ´0.14€ / 100g

import math

print("Postihintalaskuri")

lähetystyyppi = input("Kirje vai paketti: ").lower()
paino = float(input("Syötä paino grammoina: "))

# Kirjeen hinnat
kirje_perus = 0.50
kirje_200_500 = 0.04    # €/100g
kirje_yli_500 = 0.07    # €/100g

# Paketin hinnat
paketti_perus = 2.0
paketti_200_500 = 0.08  # €/100g
paketti_yli_500 = 0.08  # €/100g

# Kirjeen laskenta
if lähetystyyppi == "kirje":
    hinta = kirje_perus

    #painon mukaan määräytyvät lisämaksut lasketaan täyttyneiltä sadoilta grammoilta
    #Esim. 499g -> 499/100 = 4.99math.floot = 4

    if paino < 200:
        pass # ei lisämaksua

    elif 200 <= paino <= 500:
        sadat = math.floor(paino / 100)
        hinta += sadat * kirje_200_500

    else:   #yli 500g
        sadat = math.floor(paino / 100)
        hinta += sadat * kirje_yli_500

        #Yli 500g kirjeistä peritään 2€ lisämaksu, jso kirje ei mahdu postilaatikkoon
        mahtuuko = input("Mahtuuko kirje postilaatikkoon? (Kyllä/ei): ").lower()
        if mahtuuko != "kyllä":
            hinta += 2.00


# Paketin laskenta
elif lähetystyyppi == "paketti":
    hinta = paketti_perus

    # Sama logiikka kuin kirjeillä mutta eri hinnoin
    if paino < 200:
        pass

    elif 200 <= paino <= 500:
        sadat = math.floor(paino / 100)
        hinta += sadat * paketti_200_500

    else: # yli 500g
        sadat = math.floor(paino /100)
        hinta += sadat * paketti_yli_500

else:
    print("Tuntematon lähetystyyppi, yritä uudelleen.")
    exit()

print(f"Lähetyksen hinta on {hinta:.2f} euroa.")