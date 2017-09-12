# -*- coding: utf-8 -*-

from math import *


def calcularN(sbox, length_sbox):
    """
    Dado un S-box calcula el numero maximo de bits necesarios.
    """
    return int(log(length_sbox) / log(2))


def calcularDP(count, N):
    """
    Calcula la Probabilidad Diferencial de un eventos.
    """
    return count / float(2**N)


def calcularIguales(sbox, length_sbox, dx, dy, N):
    """
    Dado un S-box, dx (delta_x) y dy (deltas_y) calcula lo siguiente:
        #{x Є Z_{2}^{N} : S(x) XOR S(x XOR dx) = dy}
    """
    x = range(length_sbox)  # Lista [0, 1, 2, ..., length_sbox - 1]

    # Contiene S(x)
    s_x = [sbox[i] for i in xrange(length_sbox)]

    # Contiene S(x XOR delta_x)
    s_x_prima = [sbox[x[i] ^ dx] for i in xrange(length_sbox)]

    count = 0  # Contador que aumenta si S(x) = S(x XOR delta_x)
    for i in xrange(length_sbox):
        tmp = s_x[i] ^ s_x_prima[i]

        if tmp == dy:
            count += 1

    return count


def getTablaDiferencias(sbox, length_sbox):
    """
    Me devuelve la tabla de diferencias de un S-box.
    """
    n = calcularN(sbox, length_sbox)

    deltas_x = range(length_sbox)  # Lista [0, 1, 2, ..., length_sbox - 1]
    deltas_y = range(length_sbox)  # Lista [0, 1, 2, ..., length_sbox - 1]

    tabla_diferencias = []  # Contiene la tabla de diferencias
    for dx in deltas_x:
        row = []
        for dy in deltas_y:
            count = calcularIguales(sbox, length_sbox, dx, dy, n)
            dp = calcularDP(count, n)
            row.append(dp)

        tabla_diferencias.append(row)

    return tabla_diferencias


def printTabla(tabla, length_sbox):
    """
    Imprime de forma legible la tabla de diferencias de un sbox
    """
    print("ΔX \ ΔY", range(length_sbox))
    for i in xrange(length_sbox):
        print(i, "    ", tabla[i])
