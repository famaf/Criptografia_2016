sbox = [3, 4, 5, 6, 7, 0, 1, 2]

delta_x = 3

x = [0, 1, 2, 3, 4, 5, 6, 7]

y = []
x_prima = []
y_prima = []
for i in range(len(sbox)):
    y.append(sbox[i])
    x_prima.append(x[i]^delta_x)
    y_prima.append(sbox[x_prima[i]])

delta_y = []
for i in range(len(sbox)):
    delta_y.append(y[i]^y_prima[i])


print "X =", x
print "Y =", y
print "X' =", x_prima
print "Y' =", y_prima
print "Delta_Y =", delta_y

lista = []
for i in range(8):
    lista.append(delta_y.count(i))

print lista

def porcentaje(parte, total):
    return (parte*100)/float(total)


for i in range(8):
    lista[i] = porcentaje(lista[i], 8)

print lista
