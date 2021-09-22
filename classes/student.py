class Student:
    def __init__(self,roll,name,age):
        self.roll = roll
        self.name = name
        self.age = age
        
    def reads(self):
        print(self.name,"is reading")

preeti = Student(10,"Preeti",24)
print(preeti.name)
print(preeti.roll)
print(preeti.age)

preeti.reads()

print("**********")

sapna = Student(11,"Sapna",19)
print(sapna.name)
print(sapna.roll)
print(sapna.age)
sapna.reads()


    
