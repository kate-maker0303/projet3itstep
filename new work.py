class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        print("Woof, woof")


dog1 = Dog('Lucy', 20, 'Border Collie')
print(dog1.name)
print(dog1.age)
print("Lucy says...")
dog1.speak()

class Cat(Animal):
    def __init__(self, name, age, lives):
        super().__init__(name, age)
        self.lives = lives
    def speak(self):
        print("Meow, meow")


cat1 = Cat('Murka', 19, 7)
print(cat1.name)
print(cat1.age)
print("Murka says...")
cat1.speak()



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Driver(Human):
    def __init__(self, name, age, licence):
        super().__init__(name, age)
        self.licence = licence
        #self.years = years
human1 = Human('Natalie', 34, 0o765)
print(human1.name)
print(human1.age)
print(human1.license)