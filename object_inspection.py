class Student:
    school = "Multan University of Science and Technology"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name:{self.name} | Age:{self.age} | school {self.school}")

        

student1 = Student("Mudasir", 18)
student2 = Student("Ali", 20)

# Add new property in __dict__ in student2
student2.grade = "A+"

print(student1.__dict__)
print(dir(student1))

print(student2.__dict__)
print(dir(student2))

print(help(Student))