#Kuukasui palkan laskeminen. Veoihin menee jokin summa ja ja paljono jä käteen?

kk_palkka = float(input("Anna kuukausi palkka: "))
veroprosentti = float(input("Anna veroprosenttisi: "))


verot = kk_palkka * (veroprosentti / 100)
print(f"Veroihin menee: {verot}€")
print(f"Kätenjäävä osuus: {kk_palkka - verot}€")
