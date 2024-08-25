### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set)) # <class 'set'> 
print(type(my_other_set)) # <class 'dict'> 

my_other_set = {"Brais", "Moure", 35}
print(my_other_set) # {'Brais', 'Moure', 35}
print(type(my_other_set)) # <class 'set'>
print(len(my_other_set)) # 3

my_other_set.add("MoureDev") # Un set no es una estructura ordenada.
print(my_other_set) # {'MoureDev', 'Moure', 35, 'Brais'}
my_other_set.add("MoureDev") # Un set no acepta repetidos.
print(my_other_set) # {'MoureDev', 'Moure', 35, 'Brais'}

print("Moure" in my_other_set) # True
print("Dalto" in my_other_set) # False

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits) # {'potato', 'orange', 'onion', 'banana', 'tomato', 'carrot', 'cabbage', 'mango', 'lemon'}

my_other_set.remove("Moure") 
print(my_other_set) # {'Brais', 'MoureDev', 35}

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(fruits) # {'orange', 'mango', 'lemon'}

my_other_set.clear()
print(len(my_other_set)) # 0

del my_other_set
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Brais", "Moure", 35, 1.77}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # Ignora los dos .union(my_new_set), porque son repetidos, pero el .union({"JavaScript", "C#"}) si lo incluye, porque son nuevos elementos en la colección.

print(my_new_set.difference(my_set))