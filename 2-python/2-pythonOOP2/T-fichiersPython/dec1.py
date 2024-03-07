from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%d-%m-%Y %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

    
daily_backup()
#---------------------------
class A:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30

obj = A()
print(obj.a)
print(obj._b)
#print(obj.__c)
#----------------------

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
 
    def get_age(self):
        print(self.__age)
    #def get_name(self):
     #   print(self.__name)

    def set_age(self, age):
        try:
            self.__age = int(age)
        except:
            print('age must be integer')

person1 = Person('omar',24)
#print(person1.__name,person1.__age)
person1.set_age(86)
person1.get_age()