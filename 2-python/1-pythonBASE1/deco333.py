def decorator(function):
    def inner():
        print("=" * 20)
        function()
        print("=" * 20)
    return inner

'''def write():
   print("Hello world")
#write()
#write = decorator(write)
#write()'''
@decorator
def write():
   print("Hello world")


@decorator
def title():
   print("New chapter")
write()   
title()