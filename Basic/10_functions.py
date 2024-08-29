### Funciones ###

# Declarando a la función
def my_function():
  print('Esto es una función.')
my_function() # Llamando a una función

# Funciones sin parámetros
def generar_nombre_completo():
  nombre = 'Brais'
  apellido = 'Moure'
  espacio = ' '
  nombre_completo = nombre + espacio + apellido
  print(nombre_completo)
generar_nombre_completo() 

def agregar_dos_numeros():
  num1 = 2
  num2 = 3
  total = num1 + num2
  print(total)
agregar_dos_numeros()

# Funciones retornando a un valor
def generar_nombre_completo():
  nombre = 'Brais'
  apellido = 'Moure'
  espacio = ' '
  nombre_completo = nombre + espacio + apellido
  return nombre_completo
print(generar_nombre_completo())

def agregar_dos_numeros():
  num1 = 2
  num2 = 3
  total = num1 + num2
  return total
print(agregar_dos_numeros())

# Funciones con parámetros
def sum_two_values(num1, num2):
  return num1 + num2
print(sum_two_values(2, 2))

def agregando(nombre):
  mensaje = nombre + ', bienvenido a Python para todos :).'
  return mensaje
print(agregando('Brais'))

def agregando_diez(num):
  ten = 10
  return num + ten
print(agregando_diez(20))

def numero_cuadrado(x):
  return x ** 2
print(numero_cuadrado(3))

def area_del_circulo(r):
  PI = 3.14
  area = PI * r ** 2
  return area
print(area_del_circulo(30))

def suma_de_numeros(n):
  total = 0
  for i in range(n+1):
    total+=i
  print(total)
suma_de_numeros(20)
suma_de_numeros(200)

def calcular_edad(anio_actual, anio_nacimiento):
  edad = anio_actual - anio_nacimiento
  return edad
print('Edad: ', calcular_edad(2024, 2002))

def peso_del_objeto(masa, gravedad):
  peso = str(masa * gravedad)+ ' N'
  return peso
print(f'El peso de un objeto en Newtons es: {peso_del_objeto(100, 9.81)}')

# Pasando argumentos con claves y valores
def nombre_completo(nombre, apellido):
  espacio = ' '
  nombre_completo = nombre + espacio + apellido
  print(nombre_completo)
nombre_completo(nombre = 'Emilie', apellido = 'Rosse')

def agregar_dos_numeros(num1, num2):
  total = num1 + num2
  print(total)
agregar_dos_numeros(num1 = 5, num2 = 7)


# Aplicando con 'return'
## string
def nombre_completo(nombre, apellido):
  espacio = ' '
  nombre_completo = nombre + espacio + apellido
  return nombre_completo
print(nombre_completo(nombre = 'Emilie', apellido = 'Rosse'))

## numero
def agregar_dos_numeros(num1, num2):
  total = num1 + num2
  return total
print(agregar_dos_numeros(num1 = 5, num2 = 7))

## booleano
def esta_incluido(n):
  if n % 2 == 0:
    print('Incluido')
    return True # 'return' va a detener la ejecución de la función, similar a 'break'
  return False
print(esta_incluido(10)) # True
print(esta_incluido(5)) # False

## lista
def mostrar_numeros_incluidos(n):
  incluidos = []
  for i in range(n + 1):
    if i % 2 == 0:
      incluidos.append(i)
  return incluidos
print(mostrar_numeros_incluidos(17))

# Función con parámetros por defecto
def agregando(nombre = 'Pablo'):
  mensaje = nombre + ', bienvenido a Python para todos :).'
  return mensaje
print(agregando())
print(agregando('Pedro'))

def generar_nombre_completo(nombre = 'Pablo', apellido = 'Escobar'):
  espacio = ' '
  nombre_completo = nombre + espacio + apellido
  return nombre_completo
print(generar_nombre_completo())
print(generar_nombre_completo('Pedro', 'Ramirez'))

def calcular_edad(anio_nacimiento, anio_actual = 2024):
  edad = anio_actual - anio_nacimiento
  return edad
print(f'Edad: {calcular_edad(2002)}')
print(f'Edad: {calcular_edad(2007, 2024)}')

def peso_del_objeto(masa, gravedad = 9.81):
  peso = str(masa * gravedad) + ' N' # El valor tiene para ser cambiado para la primera cadena
  return peso
print(f'El peso de un objeto en Newtons es: {peso_del_objeto(100)}')
print(f'El peso de un objeto en Newtons es: {peso_del_objeto(100, 1.62)}')

# Número arbitrario de argumentos
def sumar_todos_numeros(*nums):
  total = 0
  for num in nums:
    total += num
  return total
print(sumar_todos_numeros(2, 4, 6))

# Por defecto y número arbitrario de parametros en funciones
def generar_grupos(equipo,*args):
  print(equipo)
  for i in args:
    print(i)
generar_grupos('Las Panteras', 'Roberto', 'Elias', 'Manuel', 'Juan')

# Función como un parámetro de otra función
def numero_cuadrado(n):
  return n ** 2
def hacer_algo(f, x):
  return f(x)
print(hacer_algo(numero_cuadrado, 3))
