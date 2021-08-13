class Bird:
    def __init__(self,n):
        print("Bird constructor is running")
        self.name = n
    
    def eats(self, f):
        self.food = f
        # print(f"{self.name} eats food {self.food}")
        print(self.name,"eats food",self.food)
    def flies(self):
        print(self.name, "can fly")

# bird_obj = Bird("b1")
# bird_obj.eats("fish")
# bird_obj.flies()

class Ostrich(Bird):
    def __init__(self, n,legs):
        print("Ostrich constructor is running")
        self.no_of_legs = legs #1
        super().__init__(n)

        print(self.name,"has", self.no_of_legs, "no of legs")


    def flies(self):
        print(self.name ,"can't fly")
        super().flies()


ost_obj = Ostrich("ostrich1",1)
ost_obj.flies()



