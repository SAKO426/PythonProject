# Kysytään koepisteet.
# Arvosana 5 jos 90 tai yli
# Arvossna 4 jos 80 tai yli
# Arvosana 3 jos 70 tai yli
# Arvosana 2 jos 60 tai yli
# Arvosana 1 jos 50 tai yli
# Hylätty jos alle 50

def arvosana_laskuri():

    pisteet = int(input("Syötä pisteet (0-100)"))

    if 50 > pisteet:
        arvosana = "Hylätty"

    elif 50 <= pisteet <= 59:
        arvosana = "1"

    elif 60 <= pisteet <= 69:
        arvosana = "2"

    elif 70 <= pisteet <= 79:
        arvosana = "3"

    elif 80 <= pisteet <= 89:
        arvosana = "4"

    elif 90 <= pisteet <= 100:
        arvosana = "5"


    print(arvosana)

arvosana_laskuri()