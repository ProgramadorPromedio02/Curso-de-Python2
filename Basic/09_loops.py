### Bucles/Ciclos ###

# while
print('while\n')
my_condition = 0

print('loop while 1')
while my_condition < 10:
  print(my_condition)
  my_condition += 1
else: # Es opcional
  print('Mi condición es mayor o igual que 10.')

my_condition = 0

print('loop while 2')
while my_condition < 12:
  print(my_condition)
  my_condition += 2
else:
  print('Mi condición es mayor o igual que 12.')

my_condition = 0

print('loop while 3')
while my_condition < 20:
  if my_condition == 15:
    print('Mi condición es 15, y se detiene la ejecución.')
    break
  print(my_condition)
  my_condition += 1
else:
  print('Mi condición es mayor o igual que 20.')

# for
print('for\n')
my_list = [35, 24, 62, 52, 30, 30, 17]

print('loop for 1')
for element in my_list:
  print(element)

my_tuple = (35, 1.77, "Brais", "Moure")

print('loop for 2')
for element in my_tuple:
  print(element)

my_set = {"Brais", "Moure", 35}

print('loop for 3')
for element in my_set:
  print(element)

my_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}

print('loop for 4')
for element in my_dict:
  if element == 'Edad':
    break
  print(element)

print('loop for 4.1')
for element in my_dict:
  if element == 'Edad':
    continue
  print(element)

print('loop for 5')
for element in my_dict.values():
  print(element)

word = 'World'

print('loop for 6')
for i in word:
  print(i)

print('loop for 7')
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

