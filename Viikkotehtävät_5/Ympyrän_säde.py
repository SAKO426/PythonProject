#Ympyrän pinta-ala = 3.14(pi) * r^2

import math

while True:

    säde = float(input("Anna ympyrän säde:\n"))

    pinta_ala = math.pi * säde **2

    print(f"Ympyrän pinta-ala on: {pinta_ala:.2f}")

    #Tarkistetaan että vastaus on oikeassa muodossa
    jatko = input("Haluatko jatkaa? (k/e)").lower()

    while jatko != "k" and jatko != "e":
        print("Vastaa joko k tai e")
        jatko = input("Haluatko jatkaa? (k/e)").lower()
    if jatko == "e":
        print("Ohjelma päättyi")
        break