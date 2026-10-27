# Ohjelma joka kysyy ensin ajatko sähkö vai bensiini/diesel autolla
# riippuen vastaatko sähkö vai bensiini/diesel ohjelma laskee kulutuksen
# reitin matka-ajon ja kaupunkiajon perusteella

# Kulutus kokomatkalta (kWh/100km tai l/100km) =
# matka-ajon keskiarvo kulutus / 100 * matka-ajon matka +
# kaupunkiajon keskiarvikulutus / 100 * kaupunkiajon matka
#Sähkö (kWh/100km)

# Tässä tuli nyt uutena mm: "==", "if" "elif" ja "or"
# HUOM. MUISTIIN ITSELLE: "=" TARKOITTAA YHTÄ KUIN JA "==" TARKISTAA ONKO SE

auton_tyyppi =  input("Ajatko sähkö vai bensiini/diesel autolla? (vastaa sähkö / bensiini tai diesel): ")

if auton_tyyppi == "sähkö":
    matka_ajo_sähköllä = float(input("Matka-ajon kilometrit: "))
    m_ajo_sähköllä_kulutus = float(input("Matka-ajon kulutus kWh/100km: "))

    kaupunkiajo_sähköllä = float(input("Kaupunkiajon kilometrit: "))
    k_ajo_sähköllä_kulutus = float(input("Kaupunkiajon kulutus kWh/100km: "))

    sähkönkulutus = m_ajo_sähköllä_kulutus / 100 * matka_ajo_sähköllä + k_ajo_sähköllä_kulutus / 100 * kaupunkiajo_sähköllä

    print(f"Sähkönkulutus: {sähkönkulutus}kWh/100")

elif auton_tyyppi == "bensiini" or auton_tyyppi == "diesel":
    matka_ajo = float(input("Matka-ajon kilometrit: "))
    m_ajo_kulutus = float(input("Matka-ajon kulutus/100km "))
    kaupunkiajo = float(input("Kaupunkiajo kilometrit: "))
    k_ajo_kulutus = float(input("Kaupunkiajo kulutus/100km: "))
    kulutus = m_ajo_kulutus / 100 * matka_ajo + k_ajo_kulutus / 100 * kaupunkiajo
    print(f"Kulutus: {kulutus}l")