# -*- conding: utf-8 -*-

from ejercicio_4a import *
# from ejercicio_1_6s0 import *


def tablaVerdad(bits):
    """
    Genera una Tabla de Verdad de X bits.
    """
    table = []
    # print "Tabla de verdad de " + str(bits) + " bits"
    # Generamos las 2^bits filas de la tabla
    for i in range(pow(2,bits)):
        elemento = [0]*bits # Generamos una fila con todo 0's
        for j in reversed(range(bits)): # Iteramos: bits, bits-2, bits-3, ..., 0
            if i <= 1:
                elemento[j] = i
                if i == 1:
                    i = 0
            else:
                elemento[j] = i%2
                i = i//2 # Division Entera (Floor)
        table.append(elemento)

    return table


def decimalToHex(number):
    """
    Convierte un numero de formato decimal a hexadecimal.
    """
    return hex(number)[2:]


def main():
    """
    Evalua la funcion ingresada en la tabla de verdad.
    """
    t = tablaVerdad(4) # Generamos una tabla de verdad de 4

    rows_dec = []

    # Obtenemos el S-box en formato decimal
    for j in range(len(t)):
        f_valuate = f(t[j][0], t[j][1], t[j][2], t[j][3])
        g_valuate = g(t[j][0], t[j][1], t[j][2], t[j][3])
        h_valuate = h(t[j][0], t[j][1], t[j][2], t[j][3])
        i_valuate = i(t[j][0], t[j][1], t[j][2], t[j][3])

        row_list = [str(f_valuate), str(g_valuate), str(h_valuate), str(i_valuate)]

        row_string = "".join(row_list)

        rows_dec.append(int(row_string, 2))

    # Convertimos el S-box de formato decimal a hexadecimal.
    rows_hex = []
    for j in range(len(rows_dec)):
        rows_hex.append(decimalToHex(rows_dec[j]).upper())

    print "\nS-Box en Dec:", rows_dec
    print "\nS-Box en Hex:", rows_hex, "\n"


if __name__ == "__main__":
    main()
