class Shape():
    def area(self, area=0):
        self.area = area
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        self.area = 3.14*int(self.radius)*int(self.radius)
        return self.area
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        return self.area

generic_shape = Shape()
circle = Circle(6)
rectangle = Rectangle(2,3)

print(generic_shape.area())
print(circle.area())
print(rectangle.area())

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def describe(self):
        return f"{self.name}, age {self.age}, grade {self.grade}"

generic_person = Person("John", 30)
student = Student("Alice", 20, "A")

print(generic_person.name, generic_person.age)
print(student.name, student.age, student.grade)

class Appliance():
    def power_usage(self):
        return 100
class Fridge(Appliance):
    def power_usage(self):
        return 150
class Fan(Appliance):
    def power_usage(self):
        return 50

generic_appliance = Appliance()
fridge = Fridge()
fan = Fan()

print(generic_appliance.power_usage())
print(fridge.power_usage())
print(fan.power_usage())