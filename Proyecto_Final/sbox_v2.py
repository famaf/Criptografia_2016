# -*- coding: utf-8 -*-

def calcularPorcentaje(parte, total):
    return (parte*100)/float(total)

sbox = [3, 4, 5, 6, 7, 0, 1, 2]

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = []

delta_x = 3
delta_y = []

x_prima = []
y_prima = []

apariciones = []
porcentajes = []

largo = len(sbox)

for i in range(largo):
    y.append(sbox[i])
    x_prima.append(x[i]^delta_x)
    y_prima.append(sbox[x_prima[i]])


for i in range(largo):
    delta_y.append(y[i]^y_prima[i])


for i in range(largo):
    apariciones.append(delta_y.count(i))


for i in range(8):
    porcentajes.append(calcularPorcentaje(apariciones[i], 8))

print porcentajes
