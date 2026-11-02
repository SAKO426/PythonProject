numerot = []

while True:
    numero = input("Anna numero:\n")

    if numero == "0":
        print(f"Annoit {len(numerot)} numeroa")
        break

    else:
        numerot.append(int(numero))
