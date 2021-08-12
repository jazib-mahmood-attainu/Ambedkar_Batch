from .animal import Animal
class Dog(Animal):
    def __init__(self, name, no_of_legs, has_tail,breed):
        self.breed = breed
        print("Dog is an animal")
        print("dog.py constructor is called")
        print("Dog's breed is",breed)
        super().__init__(name, no_of_legs, has_tail)

    def bark(self):
        print(self.name,"is barking")