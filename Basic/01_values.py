### Variables ###

# Int
my_int_var = 5
print(my_int_var)

# Float
my_float_var = 5.5
print(my_float_var)

# Complex
my_complex_var = 2j + 5j
print(my_complex_var)

# String
my_str_var = "My String Var"
print(my_str_var)

# Bool
my_bool_var = True
print(my_bool_var)

# List
my_list_var = ["a", 1, "b", 5]
print(my_list_var)

# Tuple
my_tuple_var = ('c', 3, 'd', 6)
print(my_tuple_var)

# Diccionary
my_dict_var = {
    'id': 1,
    'firstname': 'Ruth',
    'lastname': 'Diaz',
    'country': 'Argentina',
    'city': 'Buenos Aires'
}
print(my_dict_var)

# Set
my_set_var = {9.6, 6.4, 3.3, "a", 2, 0}
print(my_set_var)

# Examples:
"""
name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 20
is_married = True
skills = ['HTML', 'CSS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}
"""

# Algunos métodos
# abs(): devuelve un método no negativo
# Example:
num_negative = abs(-10)
print(num_negative)

# len(): duvuelve la cantidad de carácteres de un valor str.
cantidad_str = len("Python")
print(cantidad_str)

# Transformar tipos de datos
# int(): Convierte un tipo de dato a entero.
# float(): Convierte un tipo de dato a flotante.
# complex(): Convierte un tipo de dato a complejo.
# str(): Convierte un tipo de dato a cadena.
# bool(): Convierte un tipo de dato a booleano.
# list(): Convierte un tipo de dato a una lista.
# tuple(): Convierte un tipo de dato a una tupla.
# dict(): Convierte un tipo de dato a un diccionario.
# set(): Convierte un tipo de dato a un conjunto.

# Examples:
"""
str_int = '5'
my_str_to_int = int(str_int)
my_int_to_float = float(my_int_var)
my_int_to_complex = complex(my_int_var)
my_int_to_str = str(my_int_var)
str_bool = 'True'
my_str_to_bool = bool(str_bool)
my_set_to_list = list(my_set_var)
my_list_to_tuple = tuple(my_list_var)
list_dict = [("a", 1), ("z", 10)]
my_list_to_dict = dict(list_dict)
my_list_to_set = set(my_list_var)

print(my_str_to_int)
print(my_int_to_float)
print(my_int_to_complex)
print(my_int_to_str)
print(my_str_to_bool)
print(my_set_to_list)
print(my_list_to_tuple)
print(my_list_to_dict)
print(my_list_to_set)
"""

# Concatenación de variables en un print
my_int_to_str = str(my_int_var)
print(my_str_var, my_int_to_str, my_bool_var)
print("Este es el valor de: ", my_bool_var)

# Algunas funciones del sistema
print(len(my_str_var))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo", name, surname, ". Mi edad es: ", age ,".Y mi alias es: ", alias, ".")

# Inputs
"""
name = input('¿Cuál es tu nombre?\n ')
age = input('¿Cuántos años tienes?\n ')
print(name)
print(age)
"""
# Cambiamos su tipo
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forza tipos(no recomendable)?
# address: str = "Mi dirección"
# address = True
# address = 5
# address = 1.2
# print(type(address))