# -*- conding: utf-8 -*-


# Algoritmo de la Division
def division(a, b):
    """
    Calcula la division de dos numeros enteros (el divisor mayor que 0) y lo
    expresa como:
            Dividendo = Divisor * Cociente + Resto
    """
    if a >= 0 and b > 0:
        cociente = a/b
        resto = a%b
        print "%d = %d * %d + %d" % (a, b, cociente, resto)
    else:
        print "### ERROR ###"


# Algotimo de Euclides Recursivo
def mcd(a, b):
    """
    Calcula el MCD entre dos numeros usando el Algoritmo de Euclides Recursivo.
    """
    if b == 0:
        return a
    else:
        resto = a%b
        return mcd(b, resto)

print "### Algoritmo de Euclides Recursivo ###"
a = int(raw_input("Ingrese el primer numero: "))
b = int(raw_input("Ingrese el segundo numero: "))
print "MCD(%d, %d) = %d" % (a, b, mcd(a, b))


# Algotimo de Euclides Imperativo
def mcd(a, b):
    """
    Calcula el MCD entre dos numeros usando el Algoritmo de Euclides Imperativo.
    """
    while b != 0:
        a, b = b, a%b
    return a

print "### Algoritmo de Euclides Imperativo ###"
a = int(raw_input("Ingrese el primer numero: "))
b = int(raw_input("Ingrese el segundo numero: "))
print "MCD(%d, %d) = %d" % (a, b, mcd(a, b))


# Algotimo de Euclides Extendido
def euclides(a, b):
    """
    Algoritmo de Euclides extendido.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        (d, s, t) = euclides(b, a%b)

    return (d, t, s-(a/b)*t)
