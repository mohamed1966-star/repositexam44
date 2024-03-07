# list comprehension
numbers=[2,9,14,24,30,33,56,79,85,105]

newNumbers=[]
for number in numbers:
    if number >30 :
        newNumbers.append(number)
print(newNumbers)

newNumbers=[number for number in numbers if number > 30]
print(newNumbers)

divideby2=[number for number in numbers if number %2 == 0 ]
print(divideby2)

numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)

print('------------------------------------')
fruits = ['orange','banan','apple','apricot','grapes']

Fruits = []

for fruit in fruits:
    Fruits.append(fruit.title())

print(Fruits)

Fruits=[fruit.title()for fruit in fruits]
print(Fruits)
