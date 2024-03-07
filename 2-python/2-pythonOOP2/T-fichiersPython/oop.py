'''
class Human():
    Name = ""
    Birth = ""

sami = Human()
sami.Name = 'sami err'
sami.Birth = 2000

print(sami.Name)
print(sami.Birth)

aya = Human()
aya.Name = 'aya ram'
aya.Birth = 2005
print(aya.Name)
print(aya.Birth)
'''
#========================
'''
class Human:
    name = 'جميلة رامي'
    birth = 1990

    def Talk(self):
        print('Hello '+ self.name)
x = Human()
x.Talk()

class Toman:
    name = 'Sami Rami'
    birth = 1980

    def Talk(self):
        print('Hello '+ self.name)
    
    def calc_age(self):
        age = 2023 - self.birth
        print('My age is :',age)
x = Toman()
x.Talk()
x.calc_age()
#==================================

class Human:
    def __init__(self,Name,Birth):
        self.Name = Name
        self.Birth = Birth
        
kin = Human("toto",1994)
print(kin.Name)
print(kin.Birth)
#=======================
class Human:
    def __init__(self,name,birth):
        self.name = name
        self.__birth = birth
        self.__max_age = 100
    # getter method
    def get_birth(self):
        return self.__birth
    #setter method
    def set_birth(self, value):
        self.__birth = value
x = Human("Toto",1992)
print(x.get_birth())
#========================

class Human:
    def __init__(self,name,birth):
        self.name = name
        self.__birth = birth
        self.__max_age = 100
    # getter method
    
    def get_birth(self):
        return self.__birth
    #setter method
    
    def set_birth(self, value):
        if 1920 < value < 2021:
            self.__birth = value
            print("new value assigned")
        else:
            print("enter a valid birth year:")
x = Human("Toto",1999)
print(x.set_birth(1982))
'''
#-----------------------------
class Human:
    def __init__(self,name,birth):
        self.name = name
        self.__birth = birth
        self.__max_age = 100
# getter method
    @property
    def birth(self):
        return self.__birth
    #setter method
    @birth.setter
    def birth(self, value):
        if 1920 < value < 2021:
            self.__birth = value
            print("new value assigned")
        else:
            print("enter a valid birth year:")
x = Human("gogo",2001)
x.birth = 11
x.birth