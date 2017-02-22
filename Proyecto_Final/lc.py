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
    binary_list = list(bin(number)) # Genera una lista con la descomposicion binaria de un numero
    binary_list = binary_list[2:] # Le sacamos los primeros dos elementos, los cuales no son relevantes
    binary_list = [int(x) for x in binary_list] # Convertimos todos los elementos de la lista a enteros

    # Extendemos la descomposion binaria a N bits
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
    x_binary = getBinaryExtended(x, N) # Obtenemos la descomposion binario de x
    y_binary = getBinaryExtended(y, N) # Obtenemos la descomposion binario de y

    tmp = [] # Obtenemos la lista [x1*y1, x2*y2, ..., xN*yN]
    for i in xrange(N):
        tmp.append(x_binary[i] * y_binary[i])

    xor = reduce(lambda i, j: i ^ j, tmp) # Hacemos el XOR de todos los elementos de 'tmp'

    return xor


def calcularIguales(sbox, length_sbox, delta, gamma, N):
    """
    Dado un S-box, delta y gamma calcula lo siguiente:
        #{x Є Z_{2}^{N} : S(x) * delta = x * gamma}
    """
    x = range(length_sbox) # Lista [0, 1, 2, ..., length_sbox - 1]

    s_x = [] # Contiene S(x)
    for i in xrange(length_sbox):
        s_x.append(sbox[i])


    count = 0 # Contador que aumenta si S(x) * delta = x * gamma
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

    deltas = range(length_sbox) # Lista [0, 1, 2, ..., length_sbox - 1]
    gammas = range(length_sbox) # Lista [0, 1, 2, ..., length_sbox - 1]

    tabla_mascaras = [] # Contiene la tabla de diferencias
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
