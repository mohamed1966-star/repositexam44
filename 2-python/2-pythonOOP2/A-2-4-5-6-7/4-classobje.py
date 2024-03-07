# 4-DECLARING CLASSES AND OBJECTS 
class Employee:
    pass

ahmed = Employee()
somya = Employee()
print(ahmed)
print(somya)
print(ahmed==somya)

print('*************************************')

ahmed.full_name = "Ahmed Kamal"
ahmed.title = "Accountant"
ahmed.salary = 3000

somya.full_name = "Somya Hassan"
somya.title = "Archive"
somya.salary = 3400

ali = Employee()


print(ahmed.full_name)
print(ahmed.title) 
print(ahmed.salary) 

print(ali.full_name)
print(ali.title) 
print(ali.salary)

