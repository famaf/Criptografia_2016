# -*- coding: utf-8 -*-

def calcularPorcentaje(parte, total):
    return (parte*100)/float(total)


def obtenerPorcentajes(sbox, largo_sbox, delta_x):
    x = range(largo_sbox) # Lista: 0, 1, 2, ..., largo_sbox - 1

    y = [] # Lista que contiene: Sbox(x)
    x_prima = [] # Lista que contiene: x XOR delta_x
    y_prima = [] # Lista que contiene: Sbox(x_prima)
    for i in xrange(largo_sbox):
        y.append(sbox[i])
        x_prima.append(x[i] ^ delta_x)
        y_prima.append(sbox[x_prima[i]])

    delta_y = [] # Lista que contiene: y XOR y_prima
    for i in xrange(largo_sbox):
        delta_y.append(y[i] ^ y_prima[i])

    apariciones = [] # Lista que contiene las apariciones de cada numero
    for i in xrange(largo_sbox):
        apariciones.append(delta_y.count(i))

    porcentajes = [] # Lista que contiene los porcentajes de los delta_y segun el delta_x
    for i in xrange(largo_sbox):
        porcentajes.append(calcularPorcentaje(apariciones[i], largo_sbox))

    # Si la suma de los porcentajes de 100.0 devolver la lista
    if sum(porcentajes) == 100.0:
        return porcentajes
        # return porcentajes[1:]
    # Sino imprimir: ### ERROR ###
    else:
        return "### ERROR ###"


def criptoanalisis(sbox):
    largo_sbox = len(sbox) # Largo del Sbox

    for delta_x in xrange(largo_sbox):
        print "Delta_X :", delta_x, obtenerPorcentajes(sbox, largo_sbox, delta_x)



sbox1 = [3, 4, 5, 6, 7, 0, 1, 2]
sbox2 = [6, 5, 2, 7, 3, 4, 1, 0]
sbox3 = [6, 4, 1, 7, 0, 3, 5, 2]

# criptoanalisis(sbox3)
