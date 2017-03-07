# -*- conding: utf-8 -*-


##################################################################
### Funciones para la generacion del S-Box 'a' del Ejercicio 4 ###
##################################################################

###################
# Notacion:       #
#     &   : AND   #
#     |   : OR    #
#   NOT() : NOT   #
#     ^   : XOR   #
###################


def NOT(x):
    """
    Operador not
    """
    if x == 1:
        return 0
    elif x == 0:
        return 1

#------------------------------------------------------------------------------
# Funciones de Descomposicion Booleana del S-box S0 de Serpent
# S0 = 3 8 15 1 10 6 5 11 14 13 4 2 7 0 9 12

def f(x, y, z, w):
    """
    Escriba aqui la funcion 'f' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = NOT(x) & NOT(w) & (y ^ z)
    a2 = NOT(y ^ z) & (w | x)
    return a1 | a2


def g(x, y, z, w):
    """
    Escriba aqui la funcion 'g' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = y & w & NOT(x ^ z)
    a2 = NOT(w) & (x ^ z)
    a3 = x & NOT(y) & (NOT(z) | NOT(w))

    return a1 | a2 | a3


def h(x, y, z, w):
    """
    Escriba aqui la funcion 'h' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = x & NOT(y) & z & w
    a2 = NOT(x) & NOT(y ^ w)
    a3 = NOT(z) & NOT(w)

    return a1 | a2 | a3


def i(x, y, z, w):
    """
    Escriba aqui la funcion 'i' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = x & NOT(y) & NOT(z) & w
    a2 = NOT(w) & NOT(x ^ y)
    a3 = NOT(x) & z

    return a1 | a2 | a3

#------------------------------------------------------------------------------
