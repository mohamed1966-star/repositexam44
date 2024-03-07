from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer

if __name__ == '__main__':
    Sara = FreelancerProgrammer('Sara','Mazin',200,5,'PHP',['Website','Blog'])
    print(Sara.info())
    print(Sara.calculate_salary())
    Sara.assign_project('IOS App')
    print(Sara.get_projects())