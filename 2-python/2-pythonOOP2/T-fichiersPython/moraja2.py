class Employee:

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
    
    def info(self):
        return f'Name:{self.first_name} {self.last_name}, job title: {self.title}'
    
    def change_salary(self,addition):
        self.salary = self.salary + addition
        return self.salary

ahmed = Employee("Ahmed","Kamal","Comptable",4000) 
yassmi = Employee("Yassmine","Jomani","prof",8000) 

print(yassmi.salary)
yassmi.change_salary(500)
print(yassmi.salary)
