import datetime
from math import floor
from abc import ABC, abstractmethod


class Employee(ABC):
    total = 0
    __salary_raise = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        Employee.total += 1

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate__salary(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True


#ahmed = Employee("Ahmad", "Jawad")


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        if employees is None:
            employees = []
        self.employees = employees

    def get_employees(self):
        print("Employees :")
        print("=" * 11)
        employees_list = []
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1},{employee.info()}")
        return '\n'.join(employees_list)


    def info(self):
        return f'Name:{self.first_name} {self.last_name}, job title: {self.__class__.__name__}'


    def calculate__salary(self):
        return self.__salary


    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split("-")
        salary = int(salary)
        return cls(first_name, last_name, salary)



class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'Name:{self.first_name} {self.last_name}, job title: {self.__class__.__name__}'

    def calculate__salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary, lang = string.split("-")
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)

    def assign_project(self, project):
        self.projects.append(project)


    def get_projects(self):
        print("Projects :")
        print("=" * 11)
        projects_list =[]
        for number, project in enumerate(self.projects):
            projects_list.append(f"{number + 1 },{project.info}")
        return '\n'.join(projects_list)


class Projects():
    def __init__(self, name, description, days, done, info):
        self.name = name
        self.description = description
        self.days = days
        self.done = done
        self.info = info


ahmad = Employee("Ahmad","Jawad",3000)
sami = Employee("Sami","Navil",4200)
lamiss = Employee("Lamiss","KHarobi",3500)

project1 = Projects("PROJECT1","Old",50,False,'test')
project2 = Projects("PROJECT2","NEW",24,True,'test')

anwar = Manager("Anwar","Gharib",5000,[ahmad,sami,lamiss])
amr = Programmer("Amr"," Adib",5000,"python",[project1,project2])
print(anwar.get_employees())
print(amr.get_projects())
print(amr.info())
