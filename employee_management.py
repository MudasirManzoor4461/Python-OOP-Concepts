class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    @classmethod
    def from_string_file(cls, emp_str):
        name,salary,department = emp_str.split(",")
        return cls(name, int(salary), department)

    def display(self):
        print(f"Name {self.name} Salary {self.salary} Department {self.department}")


emp1 = Employee("Mudasir", 18, "S.E")
emp2 = Employee.from_string_file("Ali,80000,IT")

emp1.display()
emp2.display()
