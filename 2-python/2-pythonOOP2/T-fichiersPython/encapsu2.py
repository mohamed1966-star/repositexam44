import datetime

class Employee:
    total = 0
    salary_raise = 1.1

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.__salary = salary
        Employee.total += 1

    def info(self):
        return f'Name:{self.first_name} {self.last_name}, job title: {self.title}'
    
    def set_salary(self,salary):
        if salary <= 0:
            raise ValueError
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    #def set_salary(self,salary):
     #   if salary <= 0:
      #      raise ValueError
       # self.__salary = salary

    #def get_salary(self):
     #   return self.__salary 

    @classmethod
    def change_raise(cls, amount):
        cls.salary_raise = amount
#print(Employee.salary_raise)
#Employee.change_raise(200)
#print(Employee.salary_raise)
#print(Employee.total)

#ahmed = Employee('Ahmed','Kareem','Accountant',3000)

#print(Employee.total)

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary) 


    #@staticmethod
    #def is_workday(day):
     #   if day.weekday() == 4 or day.weekday() == 5:
      #      return False
       # return True

#date = datetime.date(2021,5,21)
#print(Employee.is_workday(date))

ahmed = Employee('Ahmed','Kareem',33,3000)
#print(ahmed.is_workday(date))

#print(ahmed.salary)

print(ahmed.get_salary())