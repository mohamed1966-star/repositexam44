from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer
from Roles import *
from Payments import *
from Profile import Profile

if __name__ == '__main__':
    Ahmad = Programmer('Ahmad','Jamal',3000,'PHP',['Website','Blog'])
    Sara = FreelancerProgrammer('Sara', 'Mazin',200,18, 'PHP', ['Website', 'Customer Service'])
    AhmadProfile = Profile('Inzgane AGADIR','0610376702','pooop@gmail.com',True)

Ahmad.profile = AhmadProfile


print(Ahmad.profile.email)
print(Ahmad.profile.phone_number)
