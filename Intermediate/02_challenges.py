### Retos ###

# Reto 1.
print('Reto 1.\n')

"""
  EL FAMOSO "FIZZ BUZZ"
  Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salta de línea entre cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

# bucle while
print('while\n')
def fizz_buzz():
  seq = 1
  while seq > 101:
    if seq % 3 == 0 and seq % 5 == 0:
      print(f'fizzbuzz: {seq}')
    elif seq % 3 == 0:
      print(f'fizz: {seq}')
    elif seq % 5 == 0:
      print(f'buzz: {seq}')
    else:
      print(seq)
      seq += 1

fizz_buzz()

# bucle for
print('for:\n')
def fizzbuzz():
  for index in range(1, 101):
    if index % 3 == 0 and index % 5 == 0:
      print(f'fizzbuzz: {index}')
    elif index % 3 == 0:
      print(f'fizz: {index}')
    elif index % 5 == 0:
      print(f'buzz: {index}')
    else:
      print(index)

fizzbuzz()
print()

# Reto 2.
print('Reto 2.\n')

"""
  ¿ES UN ANAGRAMA?
  Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
  - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
  - NO hace falta comprobar que ambas palabras existan.
  - Dos palabras exactamente iguales no son anagrama.
"""

str1 = input('Ingrese una palabra:\n')
str2 = input('Ahora ingrese de nuevo esa palabra, PERO AL REVÉS:\n')

def is_anagram(word1, word2):
  if word1.lower() == word2.lower():
    print(False)
    print('No es anagrama\n')
  elif sorted(word1.lower()) == sorted(word2.lower()):
    print(True)
    print('Es anagrama\n')
  else:
    print('Error: Vuelva a ejercutar el programar y vuelva a intentarlo.')

is_anagram(str1, str2)

# Reto 3.
print('Reto 3.\n')

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacii se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13 ...
"""

def fibonacci_sequence(limit):
    seq = []
    a, b = 0, 1
    while len(seq) < limit:
        seq.append(a)
        a, b = b, a + b
    return seq

fibonacci_numbers = fibonacci_sequence(50)
print(fibonacci_numbers)
print()

# Reto 4.

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(limit):
    primes = []
    for num in range(1, limit + 1):
        if is_prime(num):
            primes.append(num)
    print(primes)

# Imprimimos los números primos entre 1 y 100
print_primes_up_to(100)
print()

# Reto 5.

"""
INVIRTIENDO CADENAS(SIN FUNCIONES)
Crea una programa que inverta el orden de una cadena de texto sin usar funciones propias del lenguajes que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverse(text):
  text_len = len(text) - 1
  reversed_text = ""
  for i in range(0, len(text)):
    reversed_text += text[text_len - i]
  return reversed_text

print(reverse('Hola mundo'))