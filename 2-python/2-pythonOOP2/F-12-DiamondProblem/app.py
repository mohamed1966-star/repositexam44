from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer
from Roles import *
from Payments import *

if __name__ == '__main__':
    Ahmad = Programmer('Ahmad','Jamal',3000,'PHP',['Website','Blog'])
    Sara = FreelancerProgrammer('Sara', 'Mazin',200,18, 'PHP', ['Website', 'Customer Service'])

print(Ahmad.info())
print(Sara.info())
print(Sara.calculate_salary())
print(Ahmad.calculate_salary())
