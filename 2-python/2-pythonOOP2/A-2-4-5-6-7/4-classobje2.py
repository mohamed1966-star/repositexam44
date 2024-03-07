# 4-DECLARING CLASSES AND OBJECTS 

class Employee:
  def __init__(self, first_name, last_name, title, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.title = title	
    self.salary = salary
    

ahmed = Employee('Ahmed', 'Kareem','Accountant', 3000)
somya = Employee('Somya', 'Barkach', 'Archive', 4000)
 
print(ahmed.first_name)
print(ahmed.last_name)
print(somya.title)
print(somya.salary)

print('*******************************************')


class Employee:

  def __init__(self, first_name, last_name, title, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.title = title	
    self.salary = salary
    
  def info(self):
    return f'Name : {self.first_name} {self.last_name}, Job title: {self.title}'
    '''return self.first_name, self.last_name, self.title, self.salary'''


ahmed = Employee('Ahmed', 'Kareem','Accountant', 3000)
somya = Employee('Somya', 'Barkach', 'Archive', 4000)
 
print(ahmed.info())
print(somya.info())

print('*******************************************')


class Employee:

    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
    
    def info(self):
        return f'Name:{self.first_name} {self.last_name}, job title: {self.title}'

    def change_salary(self,addition):
        self.salary = self.salary + addition
        return self.salary


ahmed = Employee("Ahmed","Kamal","Comptable",4000) 
yassmin = Employee("Yassmine","Jomani","prof",8000) 

print("yasmin's salary :",yassmin.salary)
yassmin.change_salary(500)
print("yasmin's salary :",yassmin.salary)

print('*******************************************')


# EXERCICE
class Product:

   def __init__(self, name, model, price, cylinders):
      self.name = name
      self.model = model
      self.price = price
      self.cylinders = cylinders

   def info(self):
       return f'Name : {self.name}, Model : {self.model}, Price : {self.price}, cylinders : {self.cylinders}  '

   def change_price(self,discount):
      self.price = self.price - discount
      return self.price

toyota = Product('momo', 'ma145', 45000000, 'v14')
peugeot = Product('mokho', 're657', 58000000, 'v16')

print(peugeot.info())
print("price's peugeot :",peugeot.price)
peugeot.change_price(8000000)
print("price's peugeot :",peugeot.price)


