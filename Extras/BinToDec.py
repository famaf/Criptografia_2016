# -*- coding: utf-8 -*-

# Binario a Decimal

b = 11001
# Convertimos el entero en una cadena y despues lo pasamos a binario
# Base 2
print(int(str(b), 2), type(int(str(b), 2)))

# -----------------------------------------------------------------------------

# Decimal a Binario

# Convertimos el entero 25 a binario
print(bin(25), type(bin(25)))  # Nos devulve una cadena
print(int(bin(25)[2:]), type(bin(25)[2:]))  # Convertimos el numero a entero
