# -*- coding: utf-8 -*-


def calcularPorcentaje(parte, total):
    """
    Calcula el porcentaje de una parte correspecto al total.
    """
    return (parte*100)/float(total)


def getPorcentajes(sbox, length_sbox, delta_x):
    """
    Obtiene los porcentajes del S-box de la fila correspondiente al delta_x.
    """
    x = range(length_sbox) # Lista: 0, 1, 2, ..., largo_sbox - 1

    y = [] # Lista que contiene: Sbox(x)
    x_prima = [] # Lista que contiene: x XOR delta_x
    y_prima = [] # Lista que contiene: Sbox(x_prima)
    for i in xrange(length_sbox):
        y.append(sbox[i])
        x_prima.append(x[i] ^ delta_x)
        y_prima.append(sbox[x_prima[i]])

    delta_y = [] # Lista que contiene: y XOR y_prima
    for i in xrange(length_sbox):
        delta_y.append(y[i] ^ y_prima[i])

    apariciones = [] # Lista que contiene las apariciones de cada numero
    for i in xrange(length_sbox):
        apariciones.append(delta_y.count(i))

    porcentajes = [] # Lista que contiene los porcentajes de los delta_y segun el delta_x
    for i in xrange(length_sbox):
        porcentajes.append(calcularPorcentaje(apariciones[i], length_sbox))

    # Si la suma de los porcentajes de 100.0 devolver la lista
    if sum(porcentajes) == 100.0:
        return porcentajes
        # return porcentajes[1:] # Me duelve toda la lista menos el primer elemento
    # Sino devolver ### ERROR ###
    else:
        return "### ERROR ###"


def getTablaDiferencias(sbox, length_sbox):
    """
    Me devuelve la tabla de diferencias de un S-box.
    """
    tabla = [] # Lista que contiene las listas de porcentajes
    for delta_x in xrange(length_sbox):
        # print delta_x, obtenerPorcentajes(sbox, length_sbox, delta_x)
        tabla.append(getPorcentajes(sbox, length_sbox, delta_x))

    return tabla


def printTabla(tabla, length_sbox):
    """
    Imprime de forma legible la tabla de diferencias de un sbox
    """
    print "ΔX \ ΔY", range(length_sbox)
    for i in xrange(length_sbox):
        print i, "    ", tabla[i]


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

# CheckSum
# print sum(s1)
# print sum(s2)
# print sum(s3)
# print "----------"
# print sum(sbox_0)
# print sum(sbox_1)
# print sum(sbox_2)
# print sum(sbox_3)
# print sum(sbox_4)
# print sum(sbox_5)
# print sum(sbox_6)
# print sum(sbox_7)
