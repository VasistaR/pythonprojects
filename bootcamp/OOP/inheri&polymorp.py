# inheritance
class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    def who_am_i(self):
        Animal.who_am_i(self)
        print("I am a dog")
    def eat(self):
        Animal.eat(self)
        print("I am a dog eating")
mydog = Dog()
mydog.who_am_i()
mydog.eat()
print("-----------------------------------------------")
# polymorphism
class Cat():
    def __init__(self,x):
        self.name = x
    def speak(self):
        return self.name + " says meow"
class Cow():
    def __init__(self,x):
        self.name = x
    def speak(self):
        return self.name + " says moo"
niko = Cat("niko")
felix = Cow("felix")
print(niko.speak())
print(felix.speak())
for x in [niko,felix]:
    print(type(x))
    print(x.speak())
def pet_speak(pet):
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
