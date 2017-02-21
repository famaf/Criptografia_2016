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


#------------------------------------------------------------------------------
# Funciones de Descomposicion Booleana

def f(x, y, z, w):
    """
    Escriba aqui la funcion 'f' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    return (~x & ~w & (y ^ z)) | (x & ~y & ~z) | (y & z & (x | w))


def g(x, y, z, w):
    """
    Escriba aqui la funcion 'g' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    return (y & w & ~(x ^ z)) | (~w & (x ^ z)) | (x & ~y & (~z | ~w))


def h(x, y, z, w):
    """
    Escriba aqui la funcion 'h' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    # return (x & ~y & z & w) | (~x & ~(y ^ w)) | (~z & ~w)
    return (x & ~y & z & w) | (~x & ((y & w) | (~y & ~w))) | (~z & ~w)


def i(x, y, z, w):
    """
    Escriba aqui la funcion 'i' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    return (x & ~y & ~z & w) | (~w & ~(x ^ y)) | (~x & z)

#------------------------------------------------------------------------------


def evaluateFunctions(funcion1, funcion2, funcion3, funcion4):
    """
    Evalua la funcion ingresada en la tabla de verdad.
    """
    t = tablaVerdad(4) # Generamos una tabla de verdad de 4

    for i in range(len(t)):
        print funcion1(t[i][0], t[i][1], t[i][2], t[i][3]), " | ",
        print funcion2(t[i][0], t[i][1], t[i][2], t[i][3]), " | ",
        print funcion3(t[i][0], t[i][1], t[i][2], t[i][3]), " | ",
        print funcion4(t[i][0], t[i][1], t[i][2], t[i][3])

        
        # Cada cuatro prints separar con lineas
        if i == 3 or i == 7 or i == 11:
            print "---------------------"


evaluateFunctions(f, g, h, i)