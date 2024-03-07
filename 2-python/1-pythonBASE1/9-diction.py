#DICTIONAIRE
employees={'Mohamed':1300,'Ahmed':3200,'Sami':3100}

employees['Karim']=3200
print(employees)

del employees['Ahmed']
print(employees)

print(list(employees))

print('Ahmed' in employees)
print('Karim' in employees)
print('Sami' in employees)

print(employees.get('Mohamed'))


