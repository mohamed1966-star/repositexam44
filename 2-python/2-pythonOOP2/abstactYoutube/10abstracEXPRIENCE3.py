
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