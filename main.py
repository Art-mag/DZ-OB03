class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} is singing.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} is growling.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} is hissing.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} has been fed.")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} has been healed.")

# Пример использования
zoo = Zoo()
zoo.add_animal(Bird("Tweety", 2))
zoo.add_animal(Mammal("Simba", 3))
zoo.add_animal(Reptile("Rango", 5))

zoo.add_staff(ZooKeeper())
zoo.add_staff(Veterinarian())

animal_sound(zoo.animals)
