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
# Funciones de Descomposicion Booleana

def f(x, y, z, w):
    """
    Escriba aqui la funcion 'f' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = x & (NOT(y) | w)
    a2 = NOT(x) & y & z

    return a1 | a2


def g(x, y, z, w):
    """
    Escriba aqui la funcion 'g' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = NOT(x) & y & NOT(z) & NOT(w)
    a2 = NOT(x) & NOT(y) & (w | z)
    a3 = x & ((NOT(y) & NOT(w)) | (NOT(z) & w))

    return a1 | a2 | a3


def h(x, y, z, w):
    """
    Escriba aqui la funcion 'h' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = NOT(x) & y & NOT(z)
    a2 = z & w & (NOT(x) | NOT(y))
    a3 = x & NOT(w) & (z | NOT(y))

    return a1 | a2 | a3


def i(x, y, z, w):
    """
    Escriba aqui la funcion 'i' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    a1 = NOT(x) & y & NOT(z) & w
    a2 = NOT(y) & w & (x | z)
    a3 = NOT(w) & (x ^ z)

    return a1 | a2 | a3

#------------------------------------------------------------------------------
