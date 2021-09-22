class Vehicle:
    def __init__(self,tire,type):
        self.tire = tire
        self.type = type

    def run(self):
        print(self.type,"is running on",self.tire,"tires")



        