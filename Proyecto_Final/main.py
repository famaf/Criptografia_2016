# -*- coding: utf-8 -*-

import dc
import lc


def inputMode(text):
    """
    Metodo de entrada de un S-Box.
    """
    string_input = raw_input(text)

    # Separa la entrada por espacios, y los mete en una lista.
    input_list = string_input.split()

    # Procesa los elementos de la lista de entrada para pasarlos a tipo int.
    input_list = [int(a) for a in input_list]

    return input_list


def main():
    """
    Menu de seleccion para el calculo de una tabla para un S-box.
    """
    print("##############################################################################")
    print("# Bienvenido a la calculadora de Tabla de Diferencias y Mascaras de un S-box #")
    print("##############################################################################\n")

    sbox = inputMode("Ingrese el S-Box: ")

    # Menu de opciones
    while True:
        print("\nSeleccione una de las siguentes opciones:\n")
        print("#1 Tabla de Diferencias.")
        print("#2 Tabla de Mascaras.")
        print("#3 Salir.\n")

        opcion = raw_input("Ingrese una de las opciones: ")

        if opcion == "1":
            print("\nTabla de Diferencias\n====================\n")
            tabla_diferencias = dc.getTablaDiferencias(sbox, len(sbox))
            dc.printTabla(tabla_diferencias, len(sbox))
            print("\n")
        elif opcion == "2":
            print("\nTabla de Mascaras\n=================\n")
            tabla_mascaras = lc.getTablaMascaras(sbox, len(sbox))
            lc.printTabla(tabla_mascaras, len(sbox))
            print("\n")
        elif opcion == "3":
            print("\nSaliendo del programa.\n")
            break
        else:
            raw_input("No se a pulsado una opcion valida, pulse una tecla para continuar")


if __name__ == "__main__":
    main()
