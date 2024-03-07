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