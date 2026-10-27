summa = 0

for i in range(12):
    sade = float(input("Anna kuukauden sademäärä (mm):"))
    summa += sade

keskiarvo = summa / 12

print(f"Vuoden keskiarvo on n. {keskiarvo:.1f}mm")
