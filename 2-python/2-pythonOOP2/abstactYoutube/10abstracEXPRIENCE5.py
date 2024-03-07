
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