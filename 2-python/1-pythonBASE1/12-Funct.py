# FONCTION
def odd_numbers():
    """ Calculate Odd Numbers """
    for number in range(0,15):
        if number %2 == 0:
            continue
        print(number , sep=",")
odd_numbers()
print(' ********************************')
def odd_numbers(end,start=0):
    """ Calculate Odd Numbers """
    for number in range(start,end):
        if number %2 == 0:
            continue
        print(number , sep=",")
odd_numbers(20)
print(' ********************************')
def get_info(name,age,married):
    print("Name :",name,", Age :",age," ,  Married :",married)
get_info("Sami",38,True)
print(' ********************************')
def divide(x,y):
    print(x/y)
divide(18,6)
print(' ********************************')
#correction si on divise par 0
def divide(x,y):
    if(y==0):
        print("You can not divide by zero!")
        return
    print(x/y)
divide(4,2)
print(' ********************************')
def divide(x,y):
    if(y==0):
        print("You can not divide by zero!")
        return
    return x/y
print(divide(4,1))

