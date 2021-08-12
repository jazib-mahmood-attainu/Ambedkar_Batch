class Animal:
    def __init__(self,name,no_of_legs,has_tail):
        """
        Animal: constructor for the class Animal

        """

        self.name = name
        self.no_of_legs = no_of_legs
        self.has_tail = has_tail


    def eat(self):
        print(self.name,"is eating")

    def walk(self):
        print(self.name,"is walking")



