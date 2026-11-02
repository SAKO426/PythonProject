luvut = [2, 7, 10, 3, 8, 5]

summa = 0
parilliset =[]

for numerot in luvut:
    if numerot % 2 == 0:
        parilliset.append(numerot)
        summa += numerot

    else:
        continue

määrä = len(parilliset)

print(f"Parillisia on {määrä} ja summa on {summa}")