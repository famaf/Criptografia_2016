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


def calcularInversoModular(p, q, e):
    """
    Calcula el inverso modular de e.
    """
    m = (p-1)*(q-1)
    (s, d, w) = euclides(e, m)

    if d < 0:
        d += m

    return d


def main():
    print "Ecuacion a resolver:"
    print "e * d ≡ 1 (mod (p-1)*(q-1))\n"

    p = int(raw_input("Ingrese p: "))
    q = int(raw_input("Ingrese q: "))
    e = int(raw_input("Ingrese e: "))

    d = calcularInversoModular(p, q, e)

    print "\n%d * d ≡ 1 (mod %d) ==> d = %d" % (e, (p-1)*(q-1), d)


if __name__ == "__main__":
    main()
