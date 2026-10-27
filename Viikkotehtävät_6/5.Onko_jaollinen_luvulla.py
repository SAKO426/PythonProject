
# Kysytään käyttäjältä rajat
alaraja = int(input(" Anna alueen alaraja: "))
yläraja = int(input("Anna alueen yläraja: "))

löytyi = False

for luku in range(alaraja, yläraja + 1):

    #Jos ei ole jaollinen viidellä -> hylätään ja jatketaan
    if luku % 5 != 0:
        print(f"{luku} ei ole jaollinen viidellä, hylätään")
        continue

    #Tässä vaiheessa luku on jaollinen viidellä
    #Tarkastetaan vielä onko jaollinen seitsemällä

    if luku % 7 != 0:
        print(f"{luku} on jaollien viidellä mutta ei seitsemällä, hylätään")
        continue

    #Jos päästään tänne -> luku on jaollinen 5 ja 7
    print(f"====== {luku} on jaollinen 5:llä ja 7:llä.======")
    print("Lopetetaan haku.")
    löytyi = True
    break
if not löytyi:
    print("Alueelta ei löytynyt sopivaa lukua.")