# -*- coding: utf-8 -*-

def euclides(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, s, t) = euclides(b, a%b)

    return (d, t, s-(a/b)*t)


e = int(raw_input("Ingrese el primer numero: "))
m = int(raw_input("Ingrese el segundo numero: "))

(q, d, w) = euclides(e, m)

if d < 0:
    d += m

print "Inverso de 'e=%d': 'd=%d'" % (e, d)


# def euclides(a, b):
#     """
#     Algoritmo de Euclides extendido.
#     """
#     if b == 0:
#         return (a, 1, 0)
#     else:
#         (d, s, t) = euclides(b, a%b)

#     return (d, t, s-(a/b)*t)


# def calcularInversoModular(p, q, e):
#     """
#     Calcula el inverso modular de e.
#     """
#     m = (p-1)*(q-1)
#     (s, d, w) = euclides(e, m)

#     if d < 0:
#         d += m

#     return d


# p = int(raw_input("Ingrese p: "))
# q = int(raw_input("Ingrese q: "))
# e = int(raw_input("Ingrese e: "))

# d = calcularInversoModular(p, q, e)
# print "%d * d ≡ 1 (mod %d) ==> d=%d" % (e, (p-1)*(q-1), d)
