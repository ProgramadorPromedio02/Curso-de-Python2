## Lambdas ###
## Lambdas: es una función que se pueda pasar cualquier o número de argumentos, pero se puede solo si tiene una expresión, similar la función flecha => en JavaScript.

sum_two_values = lambda val1, val2: val1 + val2

print(sum_two_values(5, 5)) # 10
print(sum_two_values('Hola', 'Mundo')) # HolaMundo

x = lambda a : a + 10
print(x(5)) # 15
y = lambda a, b, c : (a + b)**c - (b + a - c)**c + (b * a)**c 
print(y(1, 3, 2)) # 21

multiply_values = lambda val1, val2: val1 * val2 - 3
print(multiply_values(5, 5)) # 22

def sum_three_values(val):
  return lambda val1, val2 : val1 + val2 + val

print(sum_three_values(5)(5, 3)) # 13