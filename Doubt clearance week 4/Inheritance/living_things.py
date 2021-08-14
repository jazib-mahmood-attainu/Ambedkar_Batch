class LivingThings:
    def __init__(self,eyes,legs,fur,tail):
        self.no_of_eyes = eyes
        self.no_of_legs = legs
        self.fur = fur
        self.tail = tail

    def breath(self):
        print("Can breath")
    
class sapiens:
    pass  



class Humans(LivingThings):
    def __init__(self, eyes, legs, fur, tail,name,caste):
        self.caste = caste
        self.name = name
        super().__init__(eyes, legs, fur, tail)

    def study(self):
        print("Is Studying")


obj_hum = Humans(2,2,False,False,"Jazib","Pathan") 

print(obj_hum.name,"has",obj_hum.no_of_eyes," eyes",obj_hum.no_of_legs,"legs")

if obj_hum.fur == True:
    print("This human has fur")
else:
    print("This human is normal")






class Dog(LivingThings):
    def __init__(self, eyes, legs, fur, tail,breed):
        self.breed = breed
        super().__init__(eyes, legs, fur, tail)