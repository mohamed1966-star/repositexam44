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
        self.profile = None

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True

