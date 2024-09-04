## Tipos de Error ###

# SyntaxError
# print 'Hola a todos' # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print('Hola a todos') # Corregido

# NameError
# print(age) # NameError: name 'age' is not defined
# print(language) # NameError: name 'age' is not defined
age = 22
language = 'Spanish'
print(age, language) # Corregido

# IndexError
nums = [1, 2, 3, 4, 5]
# print(nums[5]) # IndexError: list index out of range
print(nums[4]) # Corregido
nums.append(6) # Corregido
print(nums[5]) # Corregido
print(nums)

# ModuleNotFoundError
# import maths # ModuleNotFoundError: No module named 'maths'
import math # Corregido

# AttributeError
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi) # Corregido

# KeyError: '<string>'
users = {'name': 'Mario', 'age': 35, 'country': 'Italy'}
print(users['name'])
# print(users['county']) # KeyError: '<county'
# print(users['brother']) # KeyError: '<brother'
users['brother'] = 'Luigi' # Corregido
print(users['brother']) # Corregido

# TypeError
# print(4 + '4') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(4 + int('4')) # Corregido

# ImportError
# from math import power # ImportError: cannot import name 'power' from 'math' (unknown location)
from math import pow # Corregido
print(pow(2, 5)) 

# ValueError
# print(int('24abc')) # ValueError: invalid literal for int() with base 10: '24abc'  
print(int('24'))

# ZeroDivisionError
# print(1/0) # ZeroDivisionError: division by zero
print(24/2)
