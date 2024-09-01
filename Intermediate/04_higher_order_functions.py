### Funciones de orden superior ###

def sum_one(val):
  return val + 1

def sum_five(val):
  return val + 5

def sum_two_values_and_add_one(val1, val2, f_sum):
  return f_sum(val1 + val2)

print(sum_two_values_and_add_one(5, 2, sum_one)) # 8
print(sum_two_values_and_add_one(5, 2, sum_five)) # 12

def mul_two(val):
  return val * 2

def mul_two_values_and_add_one(val1, val2, f_mul):
  return f_mul(val1 + val2)

print(mul_two_values_and_add_one(6, 6, mul_two)) # 24

### Closures ###

def sum_ten():
  def add(val):
    return val + 10
  return add

add_closure = sum_ten()
print(add_closure(2)) # 12
print((sum_ten())(1)) # 11

def sum_twenty(val_origin):
  def add(val):
    return val + 20 + val_origin
  return add

add_closure = sum_twenty(5)
print(add_closure(2)) # 27
print((sum_twenty(5))(1)) # 26

### Built-in Higher Order Functions ###
nums = [2, 5, 10, 21, 3, 30]

# Map: Recorre todos los valores y ejecuta una función sobre ellos para modificar su valor.
def multiply_two(num):
  return num * 2

print(map(multiply_two, nums)) # <map object at 0x000001BC00F20280>
print(list(map(multiply_two, nums))) # [4, 10, 20, 42]
print(list(map(lambda num: num * 2, nums))) # [4, 10, 20, 42]

words = ["apple", "banana", "cherry", "date"]

# Usando map para convertir todas las palabras a mayúsculas
def to_upper(word):
    return word.upper()

print(list(map(to_upper, words)))  # ['APPLE', 'BANANA', 'CHERRY', 'DATE']
# Usando una función lambda
print(list(map(lambda word: word.upper(), words)))  # ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# Filter: Recorre todos los valores y ejecuta que retorna true o false para saber cómo filtrar los valores del iterado.

def filter_greater_that_ten(num):
  if num > 10:
    return True
  return False

print(filter(filter_greater_that_ten, nums)) # <filter object at 0x000001EECFB50190>
print(list(filter(filter_greater_that_ten, nums))) # [21, 30]
print(list(filter(lambda num: num > 10, nums))) # [21, 30]

words = ["apple", "banana", "cherry", "date"]

# Usando filter para seleccionar palabras con más de 5 caracteres
def is_long_word(word):
    return len(word) > 5

print(list(filter(is_long_word, words)))  # ['banana', 'cherry']

# Usando una función lambda
print(list(filter(lambda word: len(word) > 5, words)))  # ['banana', 'cherry']

# Reduce: aplicación una función de reducción de manera acumulativa a los elementos de un iterable(como una lista), reduciéndolo a un solor valor.

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

# Función para sumar dos números
def add_two_nums(x, y):
  return int(x) + int(y)

# Aplicar reduce para sumar todos los números en numbers_str
total = reduce(add_two_nums, numbers_str)
print(total)  # 15
total = reduce(lambda x, y: int(x) + int(y), numbers_str)
print(total)  # 15

def sum_two_values(val1, val2):
  return val1 + val2

print(reduce(sum_two_values, nums)) # 2 + 5 + 10 + 21 + 3 + 30 = 71
