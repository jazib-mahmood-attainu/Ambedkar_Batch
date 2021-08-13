# from animal.animal import Animal
from animals.dog import Dog


if __name__=="__main__":
    dog = Dog("scotchy",4,True,"GSD")
    dog.eat()
    dog.walk()
    dog.bark()

