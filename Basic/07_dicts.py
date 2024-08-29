### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}

my_dict = {
  'Nombre': 'Brais',
  'Apellido': 'Moure',
  'Edad': 35,
  'lenguajes': {'Python', 'Swift', 'Kotlin'},
  1: 1.77
  }

my_dict_copy = my_dict.copy()

print(my_other_dict) # {'Nombre': 'Brais', 'Apellido': 'Moure', 'Edad': 35, 1: 'Python'}
print(my_dict) # {'lenguajes': {'Kotlin', 'Swift', 'Python'}, 1: 1.77}

print(len(my_other_dict)) # 4
print(len(my_dict)) # 2

print(my_other_dict['Nombre']) # Brais
print(my_dict['lenguajes']) # {'Swift', 'Python', 'Kotlin'}

my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre']) # Pedro
my_dict['lenguajes'] = {'Java', 'JavaScript', 'C#', 'C++'}
print(my_dict['lenguajes']) # {'JavaScript', 'Java', 'C#', 'C++'}

my_dict['Calle'] = 'Calle MoureDev'
print(my_dict) # {'Nombre': 'Pedro', 'Apellido': 'Moure', 'Edad': 35, 'lenguajes': {'JavaScript', 'Java', 'C++', 'C#'}, 1: 1.77, 'Calle': 'Calle MoureDev'}

my_dict.pop('Calle') # removing Calle MoureDev
del my_dict[1] # removing 1.77
print(my_dict)
my_dict.popitem() # removing 'lenguajes': {'Java', 'C++', 'JavaScript', 'C#'}
print(my_dict)

print('Moure' in my_dict) # False
print('Apellido' in my_dict) # True

print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellido', 'Moure'), ('Edad', 35)])
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad'])
print(my_dict.values()) # dict_values(['Pedro', 'Moure', 35])

my_list = ['Nombre', 1, 'Piso']

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # {'Nombre': None, 'Apellido': None, 'Edad': None}
my_new_dict = dict.fromkeys(my_dict, ('MoureDev'))
print(my_new_dict) # {'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev'}

my_values = my_new_dict.values()
print(type(my_values)) # <class 'dict_values'>

my_keys = my_new_dict.keys()
print(type(my_keys)) # dict_keys(['Nombre', 'Apellido', 'Edad'])

print(my_new_dict.values()) # dict_values(['MoureDev', 'MoureDev', 'MoureDev'])
print(my_new_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad']) 
print(list(my_new_dict)) # ['Nombre', 'Apellido', 'Edad']
print(tuple(my_new_dict)) # ('Nombre', 'Apellido', 'Edad')
print(set(my_new_dict)) # {'Nombre', 'Edad', 'Apellido'}