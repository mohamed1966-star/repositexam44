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
    def calculate_salary(self):
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

class Freelancer(Employee):
    def __init__(self, first_name, last_name, hour_rate, work_hours):
        Employee.__init__(self,first_name, last_name)
        self.hour_rate = hour_rate
        self.work_hours = work_hours

    def info(self):
        return f'Name:{self.first_name} {self.last_name}, Job title: {self.__class__.__name__},Work hours: {self.work_hours}'

    def calculate_salary(self):
        return self.hour_rate * self.work_hours

    @classmethod
    def from_string(cls, string):
        first_name, last_name, hour_rate, work_hours = string.split('-')
        hour_rate, work_hours = int(hour_rate), int(work_hours)
        return cls(first_name, last_name, hour_rate, work_hours)