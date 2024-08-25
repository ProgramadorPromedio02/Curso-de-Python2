### Strings ###

my_string = "Mi String"
my_other_string = "Mi Otro String"

print(len(my_string)) # 9
print(len(my_other_string)) # 14

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación."
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado."
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) # Estilo nuevo(.format)
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Estilo antiguo(%())
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Estilo +
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # f-strings

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a) 
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[0:2]
print(language_slice)

language_slice = language[2:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:6:2] # Cada 2 pasos
print(language_slice)

# Reversión

reversed_language = language[::-1]
print(reversed_language)

# Funciones

word = "manzana"
phrase = "Me gusta Python y JavaScript"

print(word.capitalize())
print(word.upper())
print(word.count("a"))
print(word.isnumeric()) # false
print('1'.isnumeric()) # true
print(word.lower())
print(word.upper().isupper()) # true
print(phrase.startswith("Me")) # true
print(phrase.startswith("Python")) # false
print(phrase.endswith("on")) # false
print(phrase.endswith("Script")) # true
