while True:
    try:
        määrä = int(input("Kuinka monta oppilasta?"))
        if määrä > 0:
            break
        else:
            print("Väärä luku.")
    except ValueError:
        print("syötteen täytyy olla kokonaisluku")

summa = 0 #Tänne kerätään kaikkien arvosanojen summa

# Tässä kohdassa määritetään montako silmukkaa ohjelma tekee (oppilaiden määrä)
for i in range(määrä):
    while True:
        try:
            arvosana = float(input("Anna opiskelijan arvosana (0-5): "))
            if 0 <= arvosana <= 5:
                break # Jos syötetty arvosana on 0-5 jatkuu ohjelma alempana lisäämällä arvosana summaan.
            else:
                print("Arvosanan täytyy olla välillä 0-5.")
        except ValueError:
            print("Syötteen täytyy olla numero.")

    # Lisätään arvosana muuttujaan summa
    summa += arvosana

ka = summa / määrä
print(f"\nKeskiarvo: {ka:.2f}")

# Sanallinen arvio
if 0<= ka < 1:
    print("Huono tulos")
elif 1 <= ka < 2:
    print("Heikko tulos")
elif 2 <= ka < 3:
    print("Tyydyttävä tulos")
elif 3 <= ka < 4:
    print("Hyvä tulos")
elif 4 <= ka < 5:
    print("Kiitettävä tulos")