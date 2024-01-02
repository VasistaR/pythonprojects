mylist = [1,2,3]
class Dog():
    def __init__(self,x,y,z):
        self.breed = x
        self.name = y
        self.spots = z
new_dog = Dog("Husky", "Rex", True)
print(new_dog.breed)
print(new_dog.name)
print(new_dog.spots)
