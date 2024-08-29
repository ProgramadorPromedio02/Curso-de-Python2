### Clases ###

print('MyEmptyPerson\n')
class MyEmptyPerson: # Se tiene que escribir en PascalCase
  pass

print(MyEmptyPerson)
print(MyEmptyPerson())
print()

print('Person\n')
class Person:
  def __init__(self, name, surname): # Constructor de clase
    self.name = name # Propiedad name definida con self
    self.surname = surname # Propiedad surname definida con self

my_person = Person('Brais', 'Moure') 
print(my_person)
print(my_person.name) # Mostrar el valor de la propiedad name
print(my_person.surname) # Mostrar el valor de la propiedad surname
print()

print('Person2\n')
class Person2:
  def __init__(self, nombre, apellido, edad, pais, ciudad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.pais = pais
    self.ciudad = ciudad

p = Person2('Pablo', 'Corrinel', 20, 'Chile', 'Gran Santiago')
print(f'{p.nombre}\n{p.apellido}\n{p.edad}\n{p.pais}\n{p.ciudad}\n')

print('Person3\n')

class Person3:
  def __init__(self, name, surname):
    self.full_name = f'{name} {surname}'

  def walk(self):
    print(f'{self.full_name} está caminando.')

my_person = Person3('Brais', 'Moure')
print(my_person.full_name)
my_person.walk()
print()

print('Person4\n')

class Person4:
  def __init__(self, name, surname, alias = 'sin alias'):
    self.full_name = f'{name} {surname} ({alias})' # Propiedad pública
    self.__name = name # Propiedad privada

  def get_name(self):
    return self.__name

  def walk(self):
    print(f'{self.full_name} está caminando.')

my_person = Person4('Brais', 'Moure')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person4('Brais', 'Moure', 'MoureDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'Pablo Escobar (El Profeta)'
print(my_other_person.full_name)

my_other_person.full_name = 24
print(my_other_person.full_name)
print()

print('Person5\n')
class Person5:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person5()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person5('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

class Student(Person5):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
print()
