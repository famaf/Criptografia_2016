# -*- conding: utf-8 -*-

# Division
def division(a, b):
    if(a >= 0 and b > 0):
        cociente = a/b
        resto = a%b
        print "%d = %d * %d + %d" % (a, b, cociente, resto)
    else:
        print "### ERROR ###"


# Algotimo de Euclides Recursivo
def mcd (a, b):
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
def mcd (a, b):
    while b != 0:
        a, b = b, a%b
    return a

print "### Algoritmo de Euclides Imperativo ###"
a = int(raw_input("Ingrese el primer numero: "))
b = int(raw_input("Ingrese el segundo numero: "))
print "MCD(%d, %d) = %d" % (a, b, mcd(a, b))
