def my_decorators(func):
    def another_func():
        print('before this function')
        func()
        print('after this function')
    #print('decorators')
    return another_func()

@my_decorators
def say_hello():
    print('Hello python')

#say_hello()
#my_decorators()
#my_decorators(say_hello)
say_hello