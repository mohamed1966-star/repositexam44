# CONDITION
name= input("Enter your name:")
if len(name) > 0:
    print('Helllo  ' +name+ ' ,welcome to our program')
else:
    print('Sorry you did not write your name')

print('***************************************************')

age = int(input("Enter your age:"))
if age<14:
    print('Your are too young')
elif age > 14 and age < 18:
    print("You need your parent's permission")
else:
    print("You dont need permission")

print('***************************************************')


age1=int(input("Enter your age:"))
if age1>18:
    allowed = True
else:
   allowed = False

print(allowed)

print('***************************************************')

allowed = True if age1 > 18 else False

