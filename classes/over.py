class Parent:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def occupation(self):
        print("Works in government office")

class Child(Parent):
    def __init__(self, name, gender,namec,genderc):
        super().__init__(name, gender)
        self.namec = namec
        self.genderc = genderc

    def occupation(self):
        print("Works in Microsoft")

objc = Child("Arun","male","Govind","male")

objc.occupation()
