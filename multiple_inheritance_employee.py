class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee Id:{self.emp_id}|Name:{self.name}|Salary:{self.salary}")

class TechnicalSkills:
    def __init__(self, primamry_skill, experience_years):
        self.primary_skill = primamry_skill
        self.experience_years = experience_years

    def show(self):
        print(f"Skill:{self.primary_skill}|Experience:{self.experience_years}")

class Developer(Employee,TechnicalSkills):
    def __init__(self, emp_id, name, salary, primamry_skill,experience_years, project_name):
        Employee.__init__(self,emp_id, name, salary)
        TechnicalSkills.__init__(self, primamry_skill, experience_years)
        self.project_name = project_name

    def show_developer_info(self):
        super().show()
        print(f"Your Assigned Project is:{self.project_name}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size, department):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size
        self.department = department

    def show_manager_info(self):
        super().show()
        print(f"Your Department is:{self.department} with team Size {self.team_size}")



deve = Developer(40,"Mudasir",1000,"Python",1,"Online Proctoring System")
deve.show_developer_info()

manager = Manager(1,"Ali",1200,12,"Software Engineer")
manager.show_manager_info()

print(Developer.mro())

