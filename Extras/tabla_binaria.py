# -*- conding: utf-8 -*-


def tablaVerdad(bits):
    """
    Genera una Tabla de Verdad de X bits.
    """
    table = []
    print("Tabla de verdad de " + str(bits) + " bits")
    # Generamos las 2^bits filas de la tabla
    for i in range(pow(2, bits)):
        elemento = [0] * bits  # Generamos una fila con todo 0's
        for j in reversed(range(bits)):  # Iteramos: bits, bits-2, bits-3,.., 0
            if i <= 1:
                elemento[j] = i
                if i == 1:
                    i = 0
            else:
                elemento[j] = i % 2
                i = i // 2  # Division Entera (Floor)
        table.append(elemento)
        # print(str(elemento))
    return table
