class Manager():
    def __init__(self, first_name, last_name, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary




    def get_employees(self):
        print("Employees :")
        print("=" * 11)
        employees_list = []
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1},{employee.info()}")
        return '\n'.join(employees_list)

    def info(self):
        return f'Name :{self.first_name} {self.last_name}, Salary :{self.salary}, Job title : {self.__class__.__name__}'

    def caculate_salary(self):
        return


    '''@classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split("-")
        salary = int(salary)
        return cls(first_name, last_name, salary)'''









anwar = Manager("Anwar", "Gharib",5000)


print(anwar.info())