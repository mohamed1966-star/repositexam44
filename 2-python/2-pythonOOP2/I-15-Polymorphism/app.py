from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer
from Roles import *
from Payments import *
from Profile import Profile

if __name__ == '__main__':
    Jawad = Programmer('Jawad', 'Kareem', 4000,'Python','HR system')
    Maha = FreelancerProgrammer('Maha', 'Amil', 50,30, 'PHP', ['Website'])
    Ahmad = Manager('Ahmad', 'Saeed', 5000, ['Jawad','Maha'])

for employee in (Jawad, Maha, Ahmad):
    print(f'{employee.first_name} {employee.last_name} is paid :')
    print(employee.calculate_salary())
    print('=' * 20)


