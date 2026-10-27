#Funktio tarkastaa onko arvo yli 10
def arvon_ylitys(arvo):
    if arvo > 10:
        print("ok")
    else:
        print("no")

#Funktio laskee kaksinkertaisen arvon ja arvioi sen tason
def tupla_arvo(arvo):
    arvo_tuplana = arvo * 2

    if arvo_tuplana < 20:
        print("low")

    else:
        print("high")

#Pääohjelma
arvon_ylitys(5)
tupla_arvo(15)