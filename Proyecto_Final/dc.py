# -*- coding: utf-8 -*-

from math import *


def calcularN(sbox, length_sbox):
    """
    Dado un S-box calcula el numero maximo de bits necesarios.
    """
    return int(log(length_sbox)/log(2))


def calcularDP(count, N):
    """
    Calcula la Probabilidad Diferencial de un eventos.
    """
    return count/float(2**N)


def calcularIguales(sbox, length_sbox, dx, dy, N):
    """
    Dado un S-box, dx (delta_x) y dy (deltas_y) calcula lo siguiente:
        #{x Є Z_{2}^{N} : S(x) XOR S(x XOR dx) = dy}
    """
    x = range(length_sbox)

    s_x = []
    for i in xrange(length_sbox):
        s_x.append(sbox[i])

    s_x_prima = []
    for i in xrange(length_sbox):
        s_x_prima.append(sbox[x[i] ^ dx])

    count = 0
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

    deltas_x = range(length_sbox)
    deltas_y = range(length_sbox)

    tabla_diferencias = []
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
    print "ΔX \ ΔY", range(length_sbox)
    for i in xrange(length_sbox):
        print i, "    ", tabla[i]
