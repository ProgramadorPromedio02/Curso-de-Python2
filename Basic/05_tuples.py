### Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple) # (35, 1.77, 'Brais', 'Moure')
print(type(my_tuple)) # <class> 'tuple'

my_other_tuple = (35, 24, 62, 52, 30, 30, 17)
print(my_other_tuple) # (35, 24, 62, 52, 30, 30, 17)
print(type(my_other_tuple)) # <class> 'tuple'

print(my_tuple[0]) # 35
print(my_tuple[-1]) # Moure

print(my_other_tuple.count(30)) # 2
print(my_other_tuple.index(52)) # 3

print(my_tuple + my_other_tuple) # (35, 1.77, 'Brais', 'Moure', 35, 24, 62, 52, 30, 30, 17)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # (35, 1.77, 'Brais', 'Moure', 35, 24, 62, 52, 30, 30, 17)
print(my_sum_tuple[3:6]) # ('Moure', 35, 24)

my_tuple = list(my_tuple)
print(type(my_tuple)) # class 'list'

my_tuple[1] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple) # (35, 'Azul', 'MoureDev', 'Brais', 'Moure')
print(type(my_tuple)) # class 'tuple'

del my_tuple
del my_other_tuple

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(f"Results:\n 1. First Fruit: {first_fruit}.\n 2. Second Fruit: {second_fruit}. \n 3. Last Fruit: {last_fruit}.")

# IndexError
# print(my_tuple[4]) # Error: fuera de rango en la tupla.
# print(my_tuple[-6]) # Error: fuera de rango en la tupla.

# TypeError
# my_tuple[1] = 1.80
# print(my_tuple) # Error: no se puede reasignar elementos en una tupla.
# del my_tuple[2] # Error: no se puede seleccionar la indexación para eliminar un elemento en una tupla. 

# NameError
# print(my_tuple) # El nombre de la variable 'my_tuple' no esta definido.
# print(my_other_tuple) # El nombre de la variable 'my_other_tuple' no esta definido.