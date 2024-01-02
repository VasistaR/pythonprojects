# continuation from first lesson
class Dog():
    #Class object attribute, like static variable in java
    species = "mammal"
    def __init__(self,x,y):
        self.breed = x
        self.name = y
    # self parameter always needed
    def bark(self,number):
        print(f"{self.name} says 'Woof' {number} times")
new_dog = Dog("Husky", "Rex")
print(new_dog.breed)
print(new_dog.name)
print(new_dog.species)
new_dog.bark(2)
class Circle():
    pi = 3.141592653
    def __init__(self,x = 1):
        self.radius = x
    def get_circumference(self):
        return (2*Circle.pi*self.radius)
    def get_area(self):
        return (Circle.pi*self.radius**2)
circle1 = Circle(4)
print(circle1.get_circumference())
print(circle1.radius)
print(circle1.get_area())
