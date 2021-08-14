class Animals:
    def __init__(self,no_of_legs,has_tail,has_external_ears,has_fur):
        self.no_of_legs = no_of_legs
        self.has_tail = has_tail
        self.has_external_ears = has_external_ears
        self.has_fur = has_fur

    def Eat(self,food):
        self.food = food
        print("Animal is eating", self.food)
#######################################################
n = int(input("Enter value of no of legs"))
animal1 = Animals(n,True,True,True)



print(animal1.no_of_legs)
print(animal1.has_tail)
print(animal1.has_external_ears)
print(animal1.has_fur)
food = input("Enter food habit of the animal")
animal1.Eat(food)
animal1.Eat(food)







        
