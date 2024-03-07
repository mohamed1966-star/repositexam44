# LISTS
cars=['bmw','mercedes','toyota','kia','renault']
squares=[2,6,9,18,25,30]
print(cars[2])
print(squares[3])
print(squares+[36,40,88,100])
cars[4]='motoboto'
print(cars)
print(len(squares))
squares.insert(0,1)
print(squares)
squares.insert(5,19)
squares.pop()
print(squares)
cars.sort()
print(cars)
print(cars.index("toyota"))
cars.sort(reverse = True)
print(cars)
print('bmw' in cars)
cars.clear()
print(cars)


