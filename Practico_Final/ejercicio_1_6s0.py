# -*- conding: utf-8 -*-


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
    return (x & ~y & z & w) | (~x & ~(y ^ w)) | (~z & ~w)


def i(x, y, z, w):
    """
    Escriba aqui la funcion 'i' correspondiente siguiendo la notacion expuesta
    arriba, de la siguiente forma:

    return "Aqui escribo la funcion"
    """
    return (x & ~y & ~z & w) | (~w & ~(x ^ y)) | (~x & z)

#------------------------------------------------------------------------------
