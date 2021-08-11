from student import Student

if __name__=="__main__":
    name = input("Enter name of student")
    age = int(input("Enter age of student"))
    birth = int(input("Enter birth year of student"))
    student1 = Student(name,age,birth)

    print(student1.name)
    print(student1.age)
    student1.read()

    name = input("Enter name of student")
    age = int(input("Enter age of student"))
    birth = int(input("Enter birth year of student"))
    student2 = Student(name,age,birth)

    print(student2.name)
    print(student2.age)
    student2.read()


    



