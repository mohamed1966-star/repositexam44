class Employee:

    def __init__(self,first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
    
    
 
ahmed = Employee("Ahmed","Kamal","Comptable",4000) 
yassmine = Employee("Yassmine","Jomani","prof",8000) 

print(ahmed.first_name)
print(ahmed.last_name)
