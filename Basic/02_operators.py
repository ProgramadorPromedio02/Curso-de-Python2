### Operadores ###

# Operadores Aritméticos

print("Operadores Aritméticos: ")
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# x = 6 + 10
# print(x)

print("Hola " + "Python")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))
print("Hola " * (10 // 2))

my_float = 3.5 ** 2
print("Hola " * int(my_float))

## ErrorSyntaxis
# print("Hola" - "Python")
# print("Hola " + 5)
# print("Hola " +  (2 ** 3 + 3 - 7 / 1 // 4))
# print("Hola " * (10 / 2))
# print("Hola " * (2.5 * 2))

# Operadores Comparativos

print("Operadores Comparativos: ")
print(3 > 4) # false
print(3 < 4) # true
print(3 >= 4) # false
print(3 <= 4) # true
print(3 == 4) # false
print(3 != 4) # true

print("Hola" > "Python") # false
print("Hola" < "Python") # true
print("Hola" >= "Zola") # false
print("Hola" <= "Python") # true
print("Hola" == "Hola") # true
print("Hola" != "Python") # true

print("Hola" >= "Zola") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("AAAA")) # Cuenta caracteres

# Operadores Lógicos

print("Operadores Lógicos: ")
print(3 > 4 and "Hola" > "Python") # false
print(3 > 4 or "Hola" > "Python") # false
print(3 < 4 and "Hola" < "Python") # true
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # true
# print(3 > 4 not "Hola" > "Python") # ErrorSyntaxis
print(not(3 > 4)) # true
print(not(3 < 4)) # false
print(not(3 > 4 and "Hola" > "Python")) # true
print(not(3 > 4 or "Hola" > "Python")) # true
print(not(3 < 4 and "Hola" < "Python")) # false
print(not(3 < 4 or ("Hola" > "Python" and 4 == 4))) # false

# Operadores Asignación Compuesta

# &= (Asignación AND bit a bit)
a = 5      # En binario: 0101
b = 3      # En binario: 0011
a &= b     # Resultado: 0001 (1 en decimal)
print(a)   # Salida: 1

# |= (Asignación OR bit a bit)
a = 5      # En binario: 0101
b = 3      # En binario: 0011
a |= b     # Resultado: 0111 (7 en decimal)
print(a)   # Salida: 7

# ^= (Asignación XOR bit a bit)
a = 5      # En binario: 0101
b = 3      # En binario: 0011
a ^= b     # Resultado: 0110 (6 en decimal)
print(a)   # Salida: 6

# >>= (Asignación de desplazamiento a la derecha)
a = 8      # En binario: 1000
a >>= 2    # Resultado: 0010 (2 en decimal)
print(a)   # Salida: 2

# <<= (Asignación de desplazamiento a la izquierda)
a = 3      # En binario: 0011
a <<= 2    # Resultado: 1100 (12 en decimal)
print(a)   # Salida: 12
