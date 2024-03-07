# DECORATORS 2 ******
# def decorator(function):
def decorator(function):
    def inner():
        print("=" * 20)
        function()
        print("=" * 20)
    return inner

def write():
   print("Hello world")
#write()
write = decorator(write)
write()

def mate():
    print("aaaaaaaaaaaaaaaaaaa")
    
mate = decorator(mate)
mate()
print('---------------------------------------------')

def decorator(function):
    def inner():
        print("=" * 20)
        function()
        print("=" * 20)
    return inner

def write():
   print("Hello world")
#write()
#write = decorator(write)
#write()
@decorator
def write():
   print("Hello world")
write()

@decorator
def title():
   print("New chapter")
write()
title()

print('---------------------------------------------')

def decorator1(function):
    def inner(*args, **kwargs):
        print("+" * 70)
        function(*args, **kwargs)
        print("+" * 50)
    return inner

@decorator1
def write(name):
   print(name)

write('TOOOP')
print('---------------------------------------------')

@decorator1
def mate():
    print("aaaaaaaaaaaaaaaaaaa")
    
#mate = decorator(mate)
mate()

print('---------------------------------------------')

def decorator2(function):
    def inner(*args, **kwargs):
        print("*." * 20)
        return function(*args, **kwargs)
        print("*." * 20)
    return inner

@decorator2
def write(name):
   return name

print(write('TOOOP'))

print('---------------------------------------------')

name = input('Enter your name :')
password  = input('Your password :')
def logged_in(function):
    def inner():
        if name == "jamal" and password == "123456":
            function()
        else:
            print('please login')
            return
    return inner    
@logged_in
def get_account():
    print("You are logged in, user name",name, "password",password)
get_account()


