# EXERCICE
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
    
    '''def get_salary(self):
        return self.__salary * self.__salary_raise
    
    
    def set_salary(self,salary):
        if salary <= 0:
            raise ValueError
        self.__salary = salary
 

    @classmethod
    def __change_raise(cls,amount):
        cls.__salary_raise = amount'''

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary) 

    '''@staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True  '''

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees):
        super().__init__(first_name, last_name, salary)
        self.employees = employees
        
    def get_employees(self):
        print()
        print("Employees :")
        print("=" * 11)
        employees_list =[]
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1 },{employee.info()}")
        return '\n\n'.join(employees_list)

class Accountant(Employee):
    pass

class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects):
        super().__init__(first_name, last_name, salary)
        self.lang = lang
        self.projects = projects

    def get_projects(self):
        print()
        print("Projects :")
        print("=" * 11)
        projects_list =[]
        for number, project in enumerate(self.projects):
            projects_list.append(f"{number + 1 },{project.info}")
        return '\n\n'.join(projects_list)


class Projects():
    def __init__(self, name, description, days, done, info):
        self.name = name
        self.description = description
        self.days = days
        self.done = done
        self.info = info


ahmad = Employee("Ahmad","Kamal",3000)
sami = Employee("Sami","Navil",4200)
lamiss = Employee("Lamiss","KHarobi",3500)

project1 = Projects("PROJECT1","Old",50,False,'test')
project2 = Projects("PROJECT2","NEW",24,True,'test')

anwar = Manager("Anwar","Gharib",5000,[ahmad,sami,lamiss])
amr = Programmer("Amr"," Adib",5000,"python",[project1,project2])
print(anwar.get_employees())
print(amr.get_projects())
print()
print(amr.info())


