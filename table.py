# -*- conding: utf-8 -*-


def tablaVerdad(bits):
    table = []
    print("Tabla de verdad de " + str(bits) + " bits")
    for i in range(pow(2,bits)):
        elemento = [0]*bits
        for j in reversed(range(bits)):
            if i <= 1:
                elemento[j] = i
                if i == 1:
                    i = 0
            else:
                elemento[j] = i%2
                i = i//2
        table.append(elemento)
        #print(str(elemento))
    return table

t = tablaVerdad(4)

def f(x, y, z, w):
    return (x & ~y) | (x & w) | (~x & y & z)


def g(x, y, z, w):
    return (~x & y & ~z & ~w) | (~x & ~y & (w | z)) | (x & ((~y & ~w) | (~z & w)))


def h(x, y, z, w):
    return (~x & y & ~z) | (z & w & (~x | ~y)) | (x & ~w & (z | ~y))


def g(x, y, z, w):
    return (~x & y & ~z & w) | (~y & w & (x | z)) | (~w & (x ^ z))

def printTable(funcion):
    for i in range(16):
        print funcion(t[i][0], t[i][1], t[i][2], t[i][3])
        if i == 3 or i == 7 or i == 11:
            print "---"

printTable(f)
