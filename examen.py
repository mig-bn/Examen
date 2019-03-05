from Funciones_examen import creciente, decreciente


def numero():
    conteo = 0
    redondeo = 0.0
    n = 99

    while int(redondeo) != 99:
        n = n + 1
        if (creciente(n) == False) and (decreciente(n) == False):
            conteo = conteo + 1
            redondeo = (conteo * 100.0) / n
            # print(redondeo, n)
    print('El número mínimo para el cual la proporción de números de rebote de 99 porciento es :', n)
numero()
