def fib(n):
    a, b=0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print() 
fib(100)

print('*****************************************')

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
print(fib2(1000))

