
#         EXERCICE YOUTUBE

'''# 0
class Animal():
    def move(self):
        pass
class Bird():
    print("bird fly")
class Cat():
    print("cat run")

print(('********************************'))

# 1
class Animal():
    def move(self):
        pass
class Bird(Animal):
    print("bird fly")
class Cat(Animal):
    print("cat run")

print(('********************************'))

# 2
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass
class Bird(Animal):
    print("bird fly")
class Cat(Animal):
    print("cat run")

print(('********************************'))

# 3
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("bird fly")
class Cat(Animal):
    def move(self):
        print("cat run")

Cat().move()
Bird().move()

print(('********************************'))

# 4
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("bird fly")
class Cat(Animal):
    def move(self):
        print("cat run")

a=Animal()
a.move()

print(('********************************'))

# 5
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("bird fly")
class Cat(Animal):
    def move(self):
        print("cat run")

a=Animal()
a.move()

print("*******************************************")

'''# 6
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Bird(Animal):
    def move(self):
        print("bird fly")
class Cat(Animal):
    pass

a=Cat()



