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


def tablaVerdad(bits):
    """
    Genera una Tabla de Verdad de X bits.
    """
    table = []
    # print "Tabla de verdad de " + str(bits) + " bits"
    # Generamos las 2^bits filas de la tabla
    for i in range(pow(2,bits)):
        elemento = [0]*bits # Generamos una fila con todo 0's
        for j in reversed(range(bits)): # Iteramos: bits, bits-2, bits-3, ..., 0
            if i <= 1:
                elemento[j] = i
                if i == 1:
                    i = 0
            else:
                elemento[j] = i%2
                i = i//2 # Division Entera (Floor)
        table.append(elemento)

    return table

#------------------------------------------------------------------------------
# Funciones de Descomposicion Booleana

def f(x, y, z, w):
    return (x & ~y) | (x & w) | (~x & y & z)


def g(x, y, z, w):
    return (~x & y & ~z & ~w) | (~x & ~y & (w | z)) | (x & ((~y & ~w) | (~z & w)))


def h(x, y, z, w):
    return (~x & y & ~z) | (z & w & (~x | ~y)) | (x & ~w & (z | ~y))


def i(x, y, z, w):
    return (~x & y & ~z & w) | (~y & w & (x | z)) | (~w & (x ^ z))

#------------------------------------------------------------------------------

def evaluateFunction(funcion):
    """
    Evalua la funcion ingresada en la tabla de verdad.
    """
    t = tablaVerdad(4) # Generamos una tabla de verdad de 4

    for i in range(len(t)):
        print funcion(t[i][0], t[i][1], t[i][2], t[i][3])
        
        # Cada cuatro prints separar con lineas
        if i == 3 or i == 7 or i == 11:
            print "---"


def decimalToHex(number):
    """
    Convierte un numero de formato decimal a hexadecimal.
    """
    return hex(number)[2:]


def main():
    """
    Evalua la funcion ingresada en la tabla de verdad.
    """
    t = tablaVerdad(4) # Generamos una tabla de verdad de 4

    rows = []

    # Obtenemos el S-box en formato decimal
    for j in range(len(t)):
        f_valuate = f(t[j][0], t[j][1], t[j][2], t[j][3])
        g_valuate = g(t[j][0], t[j][1], t[j][2], t[j][3])
        h_valuate = h(t[j][0], t[j][1], t[j][2], t[j][3])
        i_valuate = i(t[j][0], t[j][1], t[j][2], t[j][3])

        row_list = [str(f_valuate), str(g_valuate), str(h_valuate), str(i_valuate)]

        row_string = "".join(row_list)

        rows.append(int(row_string, 2))

    # Convertimos el S-box de formato decimal a hexadecimal.
    for j in range(len(rows)):
        rows[j] = decimalToHex(rows[j]).upper()

    print "\nS-Box"
    print "====="
    print "\n", rows, "\n"


if __name__ == "__main__":
    main()
