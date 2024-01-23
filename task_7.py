import pickle


class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name},  {self.species}, говорит '{self.sound}'")


animals = [
    Animal("Барсик", "кот", "мяу"),
    Animal("Шарик", "собака", "гав"),
    Animal("Зорька", "лошадь", "иго-го"),
    Animal("Рыжик", "лиса", "тыф-тыф"),
    Animal("Серый", "волк", "аууу")
]


with open("animals.pkl", "wb") as file:
    pickle.dump(animals, file)


with open("animals.pkl", "rb") as file:
    loaded_animals = pickle.load(file)

    for animal in loaded_animals:
        animal.make_sound()
