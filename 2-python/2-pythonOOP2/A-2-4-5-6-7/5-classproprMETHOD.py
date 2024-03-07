# 5-CLASS PROPERTIES AND METHODS
class Employee:
    total = 0

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
        Employee.total +=1
    
print("Number of employees :",Employee.total)    

ahmed = Employee("Ahmed","Kamal","Comptable",4000) 
yassmin = Employee("Yassmine","Jomani","prof",8000) 

print("Number of employees :", Employee.total)

print('**************************************************')


class Employee1:
    #total = 0
    salary_raise = 1.1

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
        #Employee1.total +=1
    
    @classmethod
    def change_raise(cls, amount):
        cls.salary_raise = amount


print(Employee1.salary_raise)
Employee1.change_raise(200)
print(Employee1.salary_raise)

print('**************************************************')


class Employee2:
    total = 0
    salary_raise = 1.1

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
        Employee2.total +=1
    
    def info(self):
        #return f'Name: {self.first_name} {self.last_name}, job title: {self.title}'
        return print('Name :', self.first_name, self.last_name, 'Job title :', self.title)
            
    @classmethod
    def change_raise(cls, amount):
        cls.salary_raise = amount
    
    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary)


ahmed = Employee2.from_string("Ahmed-Kamal-accountant-4500")
    
print(ahmed.info())
print('**************************************************')

