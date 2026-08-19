class Temperature:
    def __init__(self, celsius=0.0):
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c*9/5)+32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f-32)* 5/9

    def display(self):
        print(f"Celcius is {self.celsius}")

    @classmethod
    def create_default(cls):
        return cls(0.0)

t1 = Temperature(9)

print(Temperature.celsius_to_fahrenheit(7))
t1.display()
