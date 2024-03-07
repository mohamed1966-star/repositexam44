
# 2
from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass
class Bird(Animal):
    print("bird fly")
class Cat(Animal):
    print("cat run")
