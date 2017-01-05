# -*- conding: utf-8 -*-


def tablaVerdad(bits):
    """
    Genera una Tabla de Verdad de X bits.
    """
    table = []
    print("Tabla de verdad de " + str(bits) + " bits")
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
        #print(str(elemento))
    return table


t = tablaVerdad(4) # Guardamos la tabla de verdad generada


##################################################################
### Funciones para la generacion del S-Box 'a' del Ejercicio 4 ###
##################################################################

###############
# Notacion:   #
#   & : AND   #
#   | : OR    #
#   ~ : NOT   #
#   ^ : XOR   #
###############

def f(x, y, z, w):
    return (x & ~y) | (x & w) | (~x & y & z)


def g(x, y, z, w):
    return (~x & y & ~z & ~w) | (~x & ~y & (w | z)) | (x & ((~y & ~w) | (~z & w)))


def h(x, y, z, w):
    return (~x & y & ~z) | (z & w & (~x | ~y)) | (x & ~w & (z | ~y))


def g(x, y, z, w):
    return (~x & y & ~z & w) | (~y & w & (x | z)) | (~w & (x ^ z))


def evaluateFunction(funcion):
    """
    Evalua la funcion ingresada en la tabla de verdad.
    """
    for i in range(len(t)):
        print funcion(t[i][0], t[i][1], t[i][2], t[i][3])
        # Cada cuatro prints separar con lineas
        if i == 3 or i == 7 or i == 11:
            print "---"


# evaluateFunction(f)
