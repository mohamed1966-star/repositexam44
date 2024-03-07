import datetime

class Employee:
    total = 0
    __salary_raise = 1.1
    def __init__(self,first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        
        self.__salary = salary
        Employee.total += 1
    
    def info(self):
        return f'Name:{self.first_name} {self.last_name}'
    
    def get_salary(self):
        return self.__salary * self.__salary_raise
    
    
    def set_salary(self,salary):
        if salary <= 0:
            raise ValueError
        self.__salary = salary
 

    @classmethod
    def __change_raise(cls,amount):
        cls.__salary_raise = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary) 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True  

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees):
        super().__init__(first_name, last_name, salary)
        self.employees = employees
        
    def get_employees(self):
        print("Employees :")
        print("=" * 11)
        employees_list =[]
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1 },{employee.info()}")
        return '\n'.join(employees_list)

class Accountant(Employee):
    pass

class Programmer(Employee):
    pass

ahmad = Employee("Ahmad","Kamal",3000)
sami = Employee("Sami","Navil",4200)
lamiss = Employee("Lamiss","KHarobi",3500)

anwar = Manager("Anwar","Gharib",5000,[ahmad,sami,lamiss])

print(anwar.get_employees())