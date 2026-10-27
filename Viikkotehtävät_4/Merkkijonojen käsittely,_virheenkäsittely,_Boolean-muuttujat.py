from datetime import datetime

päivämäärä = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

asiakkaan_nimi = "Matti Meikäläinen"

syntymävuosi = 1984

saldo = 345

lopputulos = f"{asiakkaan_nimi}, {syntymävuosi}, {saldo}:€, päivitetty {päivämäärä}"

print(lopputulos)


