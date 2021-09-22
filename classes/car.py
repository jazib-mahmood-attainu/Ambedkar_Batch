from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, tire, type,model):
        super().__init__(tire, type)
        self.model = model


obj1 = Car(4,"car","Swift")
print(obj1.model)
print(obj1.tire)
obj1.run()

