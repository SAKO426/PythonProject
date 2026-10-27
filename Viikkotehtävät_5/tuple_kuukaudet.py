kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu",
             "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
             "marraskuu", "joulukuu")

numero = int(input("Anna kuukauden numero (1-12):\n"))

#Tähän lisätään -1 koska kokoelma alkaa 0:sta, ei 1:stä
print(f"Kuukausi on: {kuukaudet[numero-1]}")