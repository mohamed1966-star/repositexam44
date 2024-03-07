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
        return cls(first_name, last_name)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True


ahmed = Employee("Ahmad", "Jawad")


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

anwar = Manager("anwar","khalid",5000)