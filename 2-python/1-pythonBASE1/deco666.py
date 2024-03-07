def decorator(function):
    def inner(*args, **kwargs):
        print("=" * 20)
        function(*args, **kwargs)
        print("=" * 20)
    return inner

'''def write():
   print("Hello world")
#write()
#write = decorator(write)
#write()'''
@decorator
def write(name):
   print(name)


@decorator
def title():
   print("New chapter")
write("momo")   
title()