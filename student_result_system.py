class Student:
    total_marks = 500
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        percentage = (self.marks/Student.total_marks) * 100
        if percentage >= 80:
            return "Grade A+"
        elif percentage >= 70:
            return "Grade A"
        elif percentage >= 60:
            return "Grade B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 45:
            return "D"
        else:
            return "Fail"


    def is_passed(self):
        percentage = (self.marks/Student.total_marks) * 100
        if percentage >= 45:
            return True
        else:
            return False

    def display_result(self):
        return f"Student Name:{self.name} Roll-No:{self.roll_no} Marks:{self.marks}"


s1 = Student("Mudasir", 40, 450)        
s2 = Student("Sara", 1, 340) 

print(s1.display_result())
print(s2.display_result())

print(s1.calculate_grade())
print(s2.calculate_grade())

print(s1.is_passed())
print(s2.is_passed())
