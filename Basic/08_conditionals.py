### Condicionales ###

my_condition = True

if my_condition: # Es lo mismo que if my_condition == True:
  print('¡Es verdadero!')

my_condition = 3 * 2

if my_condition == 10:
  print('¡Es verdadero x2!')

if my_condition >= 10:
  print('¡Es verdadero x3!')

my_question = input('¿Quieres agregarle potencia a tu número? Si o No:\n')
my_question = my_question.capitalize()
# print(my_question)

if my_question == 'Si':
  potencia = int(input('Ingrese un número para potenciar la condición:\n'))
  my_condition **= potencia
  print(my_condition)

  if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20.')
  elif my_condition == 1:
    print('Es igual a 1.')
  elif my_condition >= 20:
    print('Es mayor o igual a 20.')
  else:
    print('Es cero')

  my_string = 'Mi cadena de texto'

  if my_string:
    print("Mi cadena de texto no es vacía.")

  if not my_string == "Mi cadena de textoooooo":
    print('Estas cadenas de texto coinciden.')
elif my_question == 'No':
  if my_condition > 10 and my_condition < 20:
    print('Es mayor que 10 y menor que 20.')
  elif my_condition == 1:
    print('Es igual a 1.')
  elif my_condition >= 20:
    print('Es mayor o igual a 20.')
  else:
    print('Es cero')

  my_string = 'Mi cadena de texto'

  if my_string:
    print("Mi cadena de texto no es vacía.")

  if not my_string == "Mi cadena de textoooooo":
    print('Estas cadenas de texto coinciden.')
else:
  print('Responda entre \'Si\' o \'No\' y vuelva a intentarlo, por favor.')

print('La ejecución a finalizado.')