### Listas ###

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7
print(type(my_list)) # <class 'list'>

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list) # [35, 1.77, "Brais", "Moure"]
print(len(my_other_list)) # 4
print(type(my_other_list)) # <class 'list'>

print(my_other_list[0]) # 35
print(my_other_list[1]) # 1.77
print(my_other_list[-1]) # "Moure"
print(my_other_list[-3]) # 1.77
print(my_other_list[-4]) # 35
print(my_other_list.count("Brais")) # 1
print(my_list.count(30)) # 2
print(my_list.index(52)) # 3

age, height, name, surname = my_other_list
print(name) # Brais
print(type(name)) # <class 'str'>

age, age1, age2, age3, age4, age5, age6 = my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], my_list[5], my_list[6]
print(age5) # 30
print(type) # <class 'int'>

animals = ["cat", "dog", "bird", "elefant", "monkey", "mouse"]

animal, animal1, animal2, *animalRest = animals 
print(f"This is a {animal}, a {animal1}, a {animal2} and other for example {animalRest}, etc.") # This is a cat, a dog, a bird and other for example ['elefant', 'monkey', 'mouse'], etc.

print(my_list + my_other_list) # [35, 24, 62, 52, 30, 30, 17, 35, 1.77, 'Brais', 'Moure']  

my_other_list.append("MoureDev")
print(my_other_list) # [35, 1.77, 'Brais', 'Moure', 'MoureDev']

my_other_list.insert(1, "Rojo")
print(my_other_list) # [35, 'Rojo', 1.77, 'Brais', 'Moure', 'MoureDev']

my_other_list[1] = "Azul"

my_other_list.remove("Azul")
print(my_other_list) # [35, 1.77, 'Brais', 'Moure', 'MoureDev']

my_list.remove(30)
print(my_list) # [35, 24, 62, 52, 30, 17]

my_list.pop()
print(my_list) # [35, 24, 62, 52, 30]

print(my_list.pop(2)) # 62
print(my_list) # [35, 24, 52, 30]

del my_list[2]
print(my_list) # [35, 24, 30]

my_new_list = my_list.copy()

my_list.clear()
print(my_list) # []
print(my_new_list) # [35, 24, 30]

my_new_list.reverse()
print(my_new_list) # [30, 24, 35]

my_new_list.sort()
print(my_new_list) # [24, 30, 35]

my_new_list.sort(reverse=True)
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
my_str = my_list
print(my_str) # Hola Python
print(type(my_str)) # <class 'str'>

# IndexError
# print(my_other_list[-5]) # Error: fuera de rango
# print(my_other_list[4]) # Error: fuera de rango

# TypeError
# print(my_other_list[my_other_list.count()]) # Error: tiene como exactitud un argumento.
# print(my_other_list.count()) # Error: tiene como exactitud un argumento.
# print(my_list - my_other_list) # Error: no se puede concatenar con '-'

# ValueError
# age, height, name = my_other_list
# print(name) # Error: falta expresiones en la lista. Se debe incluir todas y su tipo de dato.