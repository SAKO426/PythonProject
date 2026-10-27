# Tässä ohjelmassa tarkistetaan, että henkilötunnus on oikeanlainen

ssn = input("Anna henkilötunnus ")
ssn_ok = True # oletetaan, että hetu oikeanmuotoinen

length = len(ssn)

if length != 11:
    print("Vääränmittainen hetu")
    ssn_ok = False

#Jos hetussa ei ole "-" tai "A"
if "-" not in ssn and "A" not in ssn:
    print("Hetussa pitää olla joko väliviiva tai A")
    ssn_ok = False


# Jos löytyi väliviiva, niin oletetaan, että se on erotin merkki alku ja loppuosan välillä
if "-" in ssn:
    # splitataan hetu erotinmerkin avulla kahteen osaan
    parts = ssn.split("-")
    # tarkastetaan onko ensimmäisen osan eri pituus kuin 6
    if len(parts[0]) != 6:
        print("Alkuosa on väärän pituinen")
        ssn_ok = False
    if len(parts[1]) != 4:
        print("Loppuosa on väärän pituinen")
        ssn_ok = False
    if not parts[0].isnumeric():
        print("Alkuosa pitäisi olla pelkkiä numeroita")
        ssn_ok = False
    if not parts[1].isalnum():
        print("Loppuosassa ei saa olla muita kuin numeroita ja kirjaimia")
        ssn_ok = False


elif "A" in ssn:
    parts = ssn.split("A")
    # Tämä menee samoin kuin yllä

if ssn_ok:
    print(f"Sosiaaliturvatunnuksesi oli ok")

