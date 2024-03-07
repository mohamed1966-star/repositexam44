from Employee import Employee, Freelancer

class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects =[]
        self.projects = projects

    def info(self):
        return f'Name:{self.first_name} {self.last_name}, Job title: {self.__class__.__name__}'

    
    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary, lang = string.split("-")
        salary = int(salary)
        return cls(first_name, last_name, salary, lang) 

    def assign_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        print("Projects :")
        print("=" * 11)
        projects_list =[]
        for number, project in enumerate(self.projects):
            projects_list.append(f"{number + 1 },  {project}")
        return '\n'.join(projects_list)



class FreelancerProgrammer(Freelancer,Programmer):
    def __init__(self, first_name, last_name, hour_rate, work_hours, lang, projects):
        Freelancer.__init__(self,first_name, last_name, hour_rate, work_hours)
        Programmer.__init__(self,first_name,last_name,lang,projects)
        