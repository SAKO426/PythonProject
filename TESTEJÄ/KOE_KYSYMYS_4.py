def laske_keskiarvo():

    parametrit =[]

    for i in range (10):
        lämpö = float(input("Anna lämpötila"))

        parametrit.append(lämpö)

    keskiarvo = sum(parametrit) / len(parametrit)