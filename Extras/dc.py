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
    x = range(length_sbox)

    s_x = [sbox[i] for i in xrange(length_sbox)]

    s_x_prima = [sbox[x[i] ^ dx] for i in xrange(length_sbox)]

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
    print("ΔX \ ΔY", range(length_sbox))
    for i in xrange(length_sbox):
        print(i, "    ", tabla[i])


def inputMode(text):
    """
    Metodo de entrada de un S-box.
    """
    string_input = raw_input(text)

    # Separa la entrada por espacios, y los mete en una lista.
    input_list = string_input.split()

    # Procesa los elementos de la lista de entrada para pasarlos a tipo int.
    input_list = [int(a) for a in input_list]

    return input_list


def main():
    print("###################################################################")
    print("# Bienvenido a la calculadora de Tabla de Diferencias de un S-box #")
    print("###################################################################\n")

    sbox = inputMode("Ingrese el S-box: ")

    print("\nTabla de Diferencias\n====================\n")

    tabla_diferencias = getTablaDiferencias(sbox, len(sbox))
    printTabla(tabla_diferencias, len(sbox))

    print("\n")

# -----------------------------------------------------------------------------
# S-boxes de prueba (estan en la carpeta, paginas 15 y 16)
s1 = [3, 4, 5, 6, 7, 0, 1, 2]
s2 = [6, 5, 2, 7, 3, 4, 1, 0]
s3 = [6, 4, 1, 7, 0, 3, 5, 2]
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# S-boxes de Serpent
sbox_0 = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 4, 2, 7, 0, 9, 12]
sbox_1 = [15, 12, 2, 7, 9, 0, 5, 10, 1, 11, 14, 8, 6, 13, 3, 4]
sbox_2 = [8, 6, 7, 9, 3, 12, 10, 15, 13, 1, 14, 4, 0, 11, 5, 2]
sbox_3 = [0, 15, 11, 8, 12, 9, 6, 3, 13, 1, 2, 4, 10, 7, 5, 14]
sbox_4 = [1, 15, 8, 3, 12, 0, 11, 6, 2, 5, 4, 10, 9, 14, 7, 13]
sbox_5 = [15, 5, 2, 11, 4, 10, 9, 12, 0, 3, 14, 8, 13, 6, 7, 1]
sbox_6 = [7, 2, 12, 5, 8, 4, 6, 11, 14, 9, 1, 15, 13, 3, 10, 0]
sbox_7 = [1, 13, 15, 0, 14, 8, 2, 11, 7, 4, 12, 10, 9, 3, 5, 6]
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()
