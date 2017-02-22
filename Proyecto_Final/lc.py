# -*- coding: utf-8 -*-

from math import *


def calcularN(sbox, length_sbox):
    """
    Dado un S-box calcula el numero maximo de bits necesarios.
    """
    return int(log(length_sbox)/log(2))


def calcularBias(E, N):
    """
    Calcula es Bias (Sesgo) de un evento E.
    """
    return (E - 2**(N-1))/float(2**N)


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
    n = calcularN(sbox, length_sbox)

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
