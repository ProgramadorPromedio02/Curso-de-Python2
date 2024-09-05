### Expresiones Regulares ###

import re

# Cadenas de ejemplo
my_string = 'Esta es la lección número 7: Lección llamada Expresiones Regulares'
my_other_string = 'Esta no es la lección número 6: Manejo de Ficheros'

# match(): busca si el patrón coincide desde el inicio de la cadena
# re.I (ignore case): hace la búsqueda ignorando mayúsculas y minúsculas
match = re.match('Esta es la lección', my_string, re.I)

# Verificar coincidencia en my_string
if match is not None:
    print(match)  # <re.Match object; span=(0, 18), match='Esta es la lección'>
    span = match.span()  # Devuelve las posiciones de inicio y fin del match
    print(span)  # (0, 18)
    start, end = span
    print(my_string[start:end])  # Muestra la parte coincidente: 'Esta es la lección'
else:
    print('Esta no es la lección')

# Verificar coincidencia en my_other_string
match_other = re.match('Esta es la lección', my_other_string)
if match_other is None:
    print('Esta no es la lección')  # Si no coincide, imprime el mensaje
else:
    start, end = match_other.span()
    print(my_other_string[start:end])  # Esta es la lección (si hubiese coincidencia)

# Intentar buscar 'Expresiones Regulares' en my_string
match_expr = re.match('Expresiones Regulares', my_string)
if match_expr is None:
    print('Esta no es la lección')  # Imprime si no coincide

# search(): busca el patrón en cualquier parte de la cadena
search = re.search('lección', my_string, re.I)
if search:
    print(search)  # <re.Match object; span=(13, 20), match='lección'>
    start, end = search.span()  # Devuelve el rango donde ocurrió la coincidencia
    print(my_string[start:end])  # 'lección'

# findall(): encuentra todas las ocurrencias del patrón en la cadena
findall = re.findall('lección', my_string, re.I)
print(findall)  # ['lección', 'Lección']

# split(): divide la cadena usando el patrón como delimitador
print(re.split(':', my_string))  # ['Esta es la lección número 7', ' Lección llamada Expresiones Regulares']

# sub(): sustituye las partes de la cadena que coinciden con el patrón
print(re.sub('Expresiones', 'expresiones', my_string))  # Sustituye 'Expresiones' por 'expresiones'
print(re.sub('lección', 'LECCIÓN', my_string, flags=re.I))  # Sustituye ignorando mayúsculas
print(re.sub('Expresiones Regulares', 'RegEx', my_string))  # Sustituye toda la frase por 'RegEx'
print(re.sub('lección|Lección', 'LECCIÓN', my_string))  # Sustituye ambas variantes de 'lección' por 'LECCIÓN'
print(re.sub('[l|L]ección', 'LECCIÓN', my_string))  # Sustituye tanto 'lección' como 'Lección'

# Definición de patrones personalizados
pattern = r'[lL]ección'
print(re.findall(pattern, my_string))  # ['lección', 'Lección']

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))  # ['lección', 'Lección', 'Expresiones']
print(re.match(pattern, my_string))  # None porque no empieza con el patrón

# Encontrar letras minúsculas
pattern = r'[a-z]'
print(re.findall(pattern, my_string))  # Lista de letras minúsculas encontradas

# Encontrar números
pattern = r'[0-9]'
print(re.findall(pattern, my_string))  # ['7']
print(re.search(pattern, my_string))  # <re.Match object; span=(26, 27), match='7'>

# Patrones adicionales para encontrar dígitos y no-dígitos
pattern = r'\d'  # Encuentra cualquier dígito
print(re.findall(pattern, my_string))  # ['7']

pattern = r'\D'  # Encuentra cualquier carácter que no sea un dígito
print(re.findall(pattern, my_string))  # Lista de caracteres no numéricos

# Encontrar todas las ocurrencias de letras que comienzan con 'l'
pattern = r'[l].'
print(re.findall(pattern, my_string))  # ['la', 'le', 'll', 'la']

# Encontrar todas las cadenas que empiezan con 'l' y siguen hasta el final
pattern = r'[l].*'
print(re.findall(pattern, my_string))  # ['la lección número 7: Lección llamada Expresiones Regulares']

# Validación de correos electrónicos con expresiones regulares
email = 'mouredev@mouredev.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern, email))  # Validación correcta

# Otros ejemplos de correos para validar
invalid_email = 'mouredev@@mouredev.'
print(re.findall(pattern, invalid_email))  # []

# Ejemplo de remover espacios adicionales de una cadena
text1 = ' Python    Exercises '
print("Original string:", text1)  # Original string:  Python    Exercises
print("Without extra spaces:", re.sub(r'\s+', '', text1))  # PythonExercises

# Página para probar expresiones regulares:
# https://regex101.com/
