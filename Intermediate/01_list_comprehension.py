### Comprensión en Lista ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]
print(my_original_list)
my_other_original_list = ['Jenny', 'Nora', 'Brad', 'Tuck', 'Sheldeon', 'Vexuz']

my_list = [i for i in my_original_list]
print(my_list) # [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in my_other_original_list]
print(my_list) # ['Jenny', 'Nora', 'Brad', 'Tuck', 'Sheldeon', 'Vexuz']

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7] # reference
my_list = [i for i in range(8)]
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i for i in range(81)]
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

my_list = [i + 1 for i in range(8)]
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
my_list = [i * 2 for i in range(8)]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49]

def sum_five(number):
  return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]
