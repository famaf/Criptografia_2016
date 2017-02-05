# -*- coding: utf-8 -*-

from math import *


def calcularN(sbox):
    """
    Dado un S-box calcula el numero maximo de bits necesarios.
    """
    m = len(sbox)

    return int(log(m)/log(2))


def calcularBias(E, N):
    """
    Calcula es Bias (Sesgo) de un evento E.
    """
    return (E - 2**(N-1))/float(2**N)


def getBinary(number):
    """
    Genera una lista con las componentes binarias de un numero.
    """
    binary_list = list(bin(number)[2:])
    # binary_list = binary_list[2:]
    binary_list = [int(x) for x in binary_list]

    return binary_list


def getBinaryExtended(number, N):
    """
    Genera una lista con las componentes binarias de un numero, de largo N bits.
    """
    binary_list = list(bin(number))
    binary_list = binary_list[2:]
    binary_list = [int(x) for x in binary_list]

    while len(binary_list) < N:
        binary_list.insert(0, 0)

    return binary_list


def multiplacion(x, y, N):
    """
    Notacion:
        x = x1 x2 ... xN
        y = y1 y2 ... yN
        Representacion binaria de 'x' e 'y' de N bits
    
    Realiza la multiplacion de x por y de la siguiente forma:
        x * y = x1*y1 XOR x2*y2 XOR ... XOR xN*yN
    """
    x_binary = getBinaryExtended(x, N)
    y_binary = getBinaryExtended(y, N)

    tmp = []
    for i in xrange(N):
        tmp.append(x_binary[i] * y_binary[i])

    xor = reduce(lambda i, j: i ^ j, tmp)

    return xor


def calcularIguales(sbox, length_sbox, delta, gamma, N):
    """
    Dado un S-box, delta y gamma calcula lo siguiente:
        #{x Є Z_{2}^{N} : S(x) * delta = x * gamma}
    """
    x = range(length_sbox)

    s_x = []
    for i in xrange(length_sbox):
        s_x.append(sbox[i])


    count = 0
    for i in xrange(length_sbox):
        a = multiplacion(s_x[i], delta, N)
        b = multiplacion(x[i], gamma, N)

        if a == b:
            count += 1

    return count


def getTablaMascaras(sbox, length_sbox):
    """
    Me devuelve la tabla de mascaras de un S-box.
    """
    n = calcularN(sbox)

    deltas = range(length_sbox)
    gammas = range(length_sbox)

    tabla_mascaras = []
    for delta in deltas:
        row = []
        for gamma in gammas:
            count = calcularIguales(sbox, length_sbox, delta, gamma, n)
            bias = calcularBias(count, n)
            row.append(bias)

        tabla_mascaras.append(row)

    return tabla_mascaras


def printTabla(tabla, length_sbox):
    """
    Imprime de forma legible la tabla de diferencias de un sbox
    """
    print "Δ \ Γ", range(length_sbox)
    for i in xrange(length_sbox):
        print i, "  ", tabla[i]


def inputMode(text):
    """
    Metodo de entrada de un S-Box.
    """
    string_input = raw_input(text)

    # Separa la entrada por espacios, y los mete en una lista.
    input_list = string_input.split()

    # Procesa los elementos de la lista de entrada para pasarlos a tipo int.
    input_list = [int(a) for a in input_list]

    return input_list


def main():
    print "################################################################"
    print "# Bienvenido a la calculadora de Tabla de Mascaras de un S-box #"
    print "################################################################\n"
    sbox = inputMode("Ingrese el S-Box: ")
    print "\nTabla de Mascaras\n=================\n"
    tabla_mascaras = getTablaMascaras(sbox, len(sbox))
    printTabla(tabla_mascaras, len(sbox))
    print "\n"


#------------------------------------------------------------------------------
# S-boxes de prueba (estan en la carpeta, paginas 15 y 16)
s1 = [3, 4, 5, 6, 7, 0, 1, 2]
s2 = [6, 5, 2, 7, 3, 4, 1, 0]
s3 = [6, 4, 1, 7, 0, 3, 5, 2]
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# S-boxes de Serpent
sbox_0 = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12]
sbox_1 = [15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4]
sbox_2 = [8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2]
sbox_3 = [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14]
sbox_4 = [1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13]
sbox_5 = [15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1]
sbox_6 = [7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0]
sbox_7 = [1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6]
#------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
