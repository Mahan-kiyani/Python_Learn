class Animal:
    def __init__(self, name: str):
        self.name = name
        self.kind = "Animal"

    def make_sound(self):
        print("Animal sound")


class Mammal(Animal):
    def __init__(self, name: str, feet: int):
        super().__init__(name)
        self.kind = "Mammal"
        self.feet = feet

    def make_sound(self):
        print("Mammal sound")


class Dog(Mammal):
    def __init__(self, name: str, race: str):
        super().__init__(name=name, feet=4)
        self.kind = "Dog"
        self.race = race

    def make_sound(self):
        print("hap hap hap")


a = Animal(name="mar")
m = Mammal(name="mahi", feet=0)

print(m.kind)  # Mammal
print(m.name)  # mahi
m.make_sound()
