#DECORATORS 1 ******
#x = int(input("Enter the number :"))
def incrase(x):
    return x+1

def decrase(x):
    return x-1

def calcula(operat,x):
    return operat(x)

print(calcula(incrase,5))
print(calcula(decrase,4))
