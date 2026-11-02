
sanakirja = []

while True:

    sana =input("Anna sana:\n")

    if sana == "näytä sanakirja":
        print(sanakirja)


    elif sana == "lopeta":
        break

    else:
        sanakirja.append(sana)