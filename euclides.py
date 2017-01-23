# -*- coding: utf-8 -*-


def euclides(a, b):
    """
    Algoritmo de Euclides extendido.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        (d, s, t) = euclides(b, a%b)

    return (d, t, s-(a/b)*t)
