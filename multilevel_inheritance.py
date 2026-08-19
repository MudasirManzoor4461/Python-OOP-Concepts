class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name:{self.name}")

class Employee(Person):
        def __init__(self, name, emp_id):
            super().__init__(name)
            self.emp_id = emp_id

        def show(self):
           print(f"Employee ID:{self.emp_id}")

class Manager(Employee):
        def __init__(self, name, emp_id,team_size):
             super().__init__(name, emp_id)
             self.team_size = team_size

        def show(self):
            super().show()
            print(f"Name:{self.name}|Employee_Id:{self.emp_id}|Total_Person:{self.team_size}")

        def manage_team(self):
            print(f"Managing of a team {self.team_size} members")


m1 = Manager("Mudasir", 40, 12)
m1.show()
m1.manage_team()
    
