products = ["PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
                   "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
                   "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
                   "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
                   "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
                   "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]

# Yksittäinen tuotetunniste koostuu seuraavasta kaavasta:
# VALMISTAJA_TUOTENIMI_MALLI_VUOSI_KUUKAUSI_PAIVA_C_KATEGORIA
# Kategorioiden numerot ovat välillä 1-3, ja ne vastaavat seuraavia
# selitteitä:
# 1 = Pienlaitteet
# 2 = Kylmälaitteet
# 3 = Sekoittimet

#kategoriat listassa (ideksi vastaa numeroa)
categories = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

for product in products:
    parts = product.split("_")

    valmistaja = parts[0]
    nimi = parts[1]
    malli = parts[2]
    vuosi = parts[3]
    kuukausi = parts[4]
    päivä = parts[5]
    kategoria_numero = int(parts[7]) # 1,  2 tai 3
    kategoria = categories[kategoria_numero]

    print(f"Valmistaja: {valmistaja}")
    print(f"Nimi ja malli: {nimi} ({malli})")
    print(f"Kategoria: {kategoria}")
    print(f"Lisäyspäivämäärä: {päivä}.{kuukausi}.{vuosi}")
    print()