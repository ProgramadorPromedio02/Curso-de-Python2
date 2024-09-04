### Manejo de Ficheros ###

# Syntax: open('filename', mode)
# Modes: 
#   'r'  - read (lectura)
#   'w'  - write (escritura, sobreescribe el archivo si existe)
#   'a'  - append (añadir contenido al final del archivo)
#   'x'  - create (crear un nuevo archivo, error si ya existe)
#   't'  - text mode (modo texto, predeterminado)
#   'b'  - binary mode (modo binario)
#   '+'  - read and write (lectura y escritura)

### 1. Crear y escribir en un archivo de texto ###

# Creamos un archivo de texto y escribimos contenido en él
with open('./files/06_my_file.txt', 'w+') as f:  # 'w+' permite leer y escribir
  f.write('Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python')

### 2. Leer el archivo completo ###

# Leemos el contenido completo del archivo
with open('./files/06_my_file.txt', 'r') as f:
    txt = f.read()
    print("Tipo de 'txt':", type(txt))  # <class 'str'>
    print("Contenido del archivo:")
    print(txt)
    # Salida esperada:
    # Mi nombre es Brais
    # Mi apellido es Moure
    # 35 años
    # Y mi lenguaje preferido es Python

### 3. Leer el archivo línea por línea ###

# Leemos el archivo línea por línea usando un bucle
with open('./files/06_my_file.txt', 'r') as f:
    print("Leyendo archivo línea por línea:")
    for line in f.readlines():
        print(line.strip())  # strip() elimina el salto de línea al final de cada línea

### 4. Añadir texto al archivo existente ###

# Añadimos más texto al final del archivo existente
with open('./files/06_my_file.txt', 'a') as f:  # 'a' permite añadir al final del archivo
    f.write('\nAunque también me gusta Kotlin')

### 5. Leer el archivo después de añadir texto ###

# Volvemos a leer el archivo para ver el contenido después de añadir texto
with open('./files/06_my_file.txt', 'r') as f:
  print("\nContenido del archivo después de añadir texto:")
  print(f.read())

### 6. Convertir un diccionario a JSON y guardarlo en un archivo ###

import json

# Creamos un diccionario
json_test = {
  'name': 'Brais',
  'surname': 'Moure',
  'age': 35,
  'language': 'Python',
  'website': 'https://moure.dev'
}

# Guardamos el diccionario como un archivo JSON
with open('./files/06_my_file.json', 'w') as json_file:
  json.dump(json_test, json_file, indent=2)

### 7. Convertir JSON a Diccionario y viceversa ###

# Ejemplo de JSON (como cadena) que se convierte a diccionario
person_json = '''{
  "name": "Asabeneh",
  "country": "Finland",
  "city": "Helsinki",
  "skills": ["JavaScrip", "React", "Python"]
}'''

# Convertimos el JSON a diccionario
person_dct = json.loads(person_json)
print(type(person_dct))  # <class 'dict'>
print(person_dct)
print(person_dct['name'])

# Convertimos un diccionario a JSON y lo imprimimos con formato
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

# Guardamos el diccionario como un archivo JSON
with open('./files/06_my_file_2.json', 'w') as json_file:
  json.dump(person, json_file, indent=2)

# Convertimos el diccionario a JSON con formato
person_json = json.dumps(person, indent=2)  # indent=4 para mejorar la legibilidad
print(type(person_json))  # <class 'str'>
print(person_json)

### 8. Eliminar el archivo (opcional) ###

# Si deseas eliminar el archivo creado
# import os
# os.remove('./files/06_my_file.txt')
# os.remove('./files/06_my_file.json')
