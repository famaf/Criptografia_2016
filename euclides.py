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
