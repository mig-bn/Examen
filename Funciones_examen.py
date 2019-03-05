# Funciones para el examen


def creciente(numero):
        abandera = True
        StrNumb = str(numero)
        for i in range(len(StrNumb) - 1):
            if int(StrNumb[i]) > int(StrNumb[i + 1]):
                abandera = False
                break
        return abandera


def decreciente(numero):
    bbandera = True
    StrNumb = str(numero)
    for i in range(len(StrNumb) - 1):
        if int(StrNumb[i]) > int(StrNumb[i + 1]):
            bbandera = False
            break
    return bbandera