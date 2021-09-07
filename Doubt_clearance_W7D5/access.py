"""

Public
Protected
Private

"""

class Student:
    def __init__(self,x,y):
        self.__a = x
        self.__b = y

    def show(self):
        print(self.__a,self.__b)    


class ali(Student):
    def __init__(self,z, x, y):
        self.z = z
        super().__init__(x, y)
        self.a1 = super().__a
        print(self.a1)


# obj = Student(5,10)
# obj.show()
# print(obj.__a,"attribute a" )


obj2 = ali(2,3,4)