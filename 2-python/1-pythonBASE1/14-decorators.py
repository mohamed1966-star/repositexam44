# DECORATORS 1 ******
#x = int(input("Enter the number :"))
def incrase(x):
    return x+1

def decrase(x):
    return x-1

def calculate(operation,x):
    return operation(x)

print(calculate(incrase,5))
print(calculate(decrase,4))
print(" *********************************************")
def parent():
    print("This is parent function")
    def child1():
        print("This is child 1 function")
    def child2():
        print("This is child 2 function")
    child2()
    child1()
parent()
print(" *********************************************")
def vote(age):
    def allow():
        print("You are allowed to vote")
    def not_allowed():
        print("You are not allowed to vote")
    if age>18:
        return allow
    else:
        return not_allowed
person1=vote(15)
person2=vote(19)

person1()
person2()



