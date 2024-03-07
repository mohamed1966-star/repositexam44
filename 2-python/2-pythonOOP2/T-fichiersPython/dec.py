def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)  # prints 11
#-------------------------------------------------
def add_one(number):
    return number + 1

print(add_one(2))
#---------------------------------
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

make_pretty(ordinary())
#---------------------
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()
parent()
#---------------------------------------
def my_function():

    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.

#description = my_function
my_function()
#-----------------------
def outer_function():

    def inner_function():

        print('I came from the inner function.')

    # Executing the inner function inside the outer function.
    inner_function()
outer_function()
#-----------------------
def outer_function():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()
homework()
#----------------------------
def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')
# Calling the friendly_reminder function with the action function used as an argument.

friendly_reminder(action)


