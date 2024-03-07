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

    JawadProfile = Profile('Iraq Baghdad', '0607423580', 'pppppp@gmail.com', True)


    print(JawadProfile)


