import json

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

    def save_zoo(self, filename):
        with open(filename, 'w') as file:
            # Сохраняем информацию о животных и сотрудниках в формате JSON
            data = {
                "animals": [(type(animal).__name__, animal.name, animal.age) for animal in self.animals],
                "staff": [type(staff).__name__ for staff in self.staff]
            }
            json.dump(data, file)

    def load_zoo(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            # Загружаем информацию о животных
            for animal_type, name, age in data["animals"]:
                if animal_type == "Bird":
                    self.add_animal(Bird(name, age))
                elif animal_type == "Mammal":
                    self.add_animal(Mammal(name, age))
                elif animal_type == "Reptile":
                    self.add_animal(Reptile(name, age))
            # Загружаем информацию о сотрудниках
            for staff_type in data["staff"]:
                if staff_type == "ZooKeeper":
                    self.add_staff(ZooKeeper())
                elif staff_type == "Veterinarian":
                    self.add_staff(Veterinarian())

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} has been fed.")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} has been healed.")

# Пример использования
zoo = Zoo()
zoo.load_zoo('zoo_data.json')  # Загружаем данные зоопарка
animal_sound(zoo.animals)      # Воспроизводим звуки животных
zoo.save_zoo('zoo_data.json')  # Сохраняем текущее состояние зоопарка
