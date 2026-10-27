# Ohjelma, joka laskee, onko syötetty vuosi karkausvuosi.
# Karkausvuosi = jaollinen 4 mutta ei 100
# Kuitenkin vuosi joka on jaollinen 400 on karkausvuosi

# % jakojäännös

# 1. tapa.
#vuosi = int(input("Anna vuosi:"))

#if vuosi % 400 == 0:
#    print("Karkausvuosi.")

#elif vuosi % 100 == 0:
#    print("Ei karkausvuosi.")

#elif vuosi % 4 == 0:
#    print("Karkausvuosi.")

#else:
#    print("Ei karkausvuosi.")

# 2. tapa.
vuosi = int(input("Anna vuosi: "))

if vuosi % 4 ==0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Karkausvuosi.")
        else:
            print("Ei karkausvuosi.")
    else:
        print("Karkausvuosi.")
else:
    print("Ei karkausvuosi.")