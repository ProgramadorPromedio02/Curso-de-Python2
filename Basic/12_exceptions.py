### Excepciones ###

print('Try 1:\n')
try:
  print(10 + '5')
except:
  print('Algo salió mal :(.\n')

print('Try 2:\n')
try:
  print(10 / 0)
except ZeroDivisionError:
  print('ZeroDivisionError: Error de división por 0 :(.\n')

print('Try 3:\n')
try:
  numberOne = 5
  numberTwo = 1
  numberTwo = '1'
  print(numberOne + numberTwo)
except TypeError as e:
  print(e)
  print()

print('Try 4:\n')
try:
  name = input('Ingresa tu nombre:\n')
  year_born = input('Ingresa tu año de nacimiento:\n')
  age = 2019 - year_born
  print(f'Tu eres {name}. Y tu edad es {age}.')
except TypeError:
  print('TypeError: Error de tipado de la variable :(.\n')

print('Try 5:\n')
try:
  def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

  lst = [1, 2, 3, 4, 5]
  print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
except TypeError:
  print('TypeError: Error de tipado de la variable :(.\n')

print('Try 6:\n')
try:
  lista = [1, 2, 3]
  print(lista[5])
except IndexError:
  print('IndexError: Error de indice\n')

print('Try 7:\n')
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print(f"ValueError: Ingresaste un valor no numérico.")
else:
    print(f"El número ingresado es: {numero}.")
finally:
    print("Este mensaje se muestra siempre, ocurra o no una excepción.\n")

print('Try 8:\n')
def dividir(a, b):
    if b == 0:
        raise ValueError("El denominador no puede ser cero.")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Error: {e}\n")

print('Try 9:\n')
class SaldoInsuficienteError(Exception):
  pass

def retirar_dinero(saldo, cantidad):
  if cantidad > saldo:
    raise SaldoInsuficienteError("Saldo insuficiente para realizar esta operación.")
  saldo -= cantidad
  return saldo

try:
  saldo_actual = retirar_dinero(100, 150)
except SaldoInsuficienteError as e:
  print(f"Error: {e}\n")

print('Try 10:\n')
try:
  numero = int(input("Ingresa un número: "))
  resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e: # Manejar múltiples excepciones
  print(f"Ocurrió un error: {e}\n")

print('Try 11:\n')
def calcular_raiz_cuadrada(x):
  assert x >= 0, "El número debe ser no negativo."
  return x ** 0.5

try:
  print(calcular_raiz_cuadrada('a'))
except AssertionError as e:
  print(f"Error: {e}\n")
except TypeError as e:
  print(f"Error de tipo: {e}\n")
