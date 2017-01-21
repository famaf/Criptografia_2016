# -*- coding: utf-8 -*-

from math import *


def calculateN(sbox):
    """
    Dado un SBOX calcula el numero maximo de bits necesarios.
    """
    m = max(sbox) + 1 # TAMBIEN PUEDE SER LEN SBOX

    return int(log(m)/log(2))


def calcularBias(evento, N):
    """
    Calcula es Bias de un evento.
    """
    return (evento - 2**(N-1))/float(2**N)


def getBinary(number):
    """
    Genera una lista con las componentes binarias de un numero.
    """
    binary_list = list(bin(number))
    binary_list = binary_list[2:]
    binary_list = [int(x) for x in binary_list]

    return binary_list


def getBinaryExtended(number, N):
    """
    Genera una lista con las componentes binarias de un numero de N bits.
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


#----------------------------------------------

def calcularIguales(sbox, delta, gamma, N):
    length = len(sbox)
    x = range(length)

    s_x = []
    for i in xrange(8):
        s_x.append(sbox[i])


    count = 0
    for i in xrange(length):
        a = multiplacion(s_x[i], delta, n)
        b = multiplacion(x[i], gamma, n)

        if a == b:
            count += 1

    return count


sbox = [6, 4, 1, 7, 0, 3, 5, 2]

delta = 4
n = calculateN(sbox) # Cantidad de bits necesarios
print "Delta =", delta
for gamma in xrange(8):
    count = calcularIguales(sbox, delta, gamma, n)
    bias = calcularBias(count, n)
    print "Gamma =", gamma, "--->", bias





