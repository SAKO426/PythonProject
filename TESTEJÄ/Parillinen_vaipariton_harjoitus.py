

def tarkista_luku():

    luku = int(input("Anna luku:\n"))

    if luku % 2 == 0:
        print(f"Luku {luku} on parillinen\n")

    else:
        print(f"Luku {luku} on pariton\n")

while True:
    luku = tarkista_luku()

    if luku  == 0:
        break