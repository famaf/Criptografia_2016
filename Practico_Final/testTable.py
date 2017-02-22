# -*- conding: utf-8 -*-

# from ejercicio_4a import *
from ejercicio_1_6s0 import *


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

# t = tablaVerdad(4)
# for j in xrange(len(t)):
#     print f(t[j][0], t[j][1], t[j][2], t[j][3])
#     if (j == 3) or (j == 7) or (j == 11):
#         print "---"

# print i(0, 0, 0, 0)
