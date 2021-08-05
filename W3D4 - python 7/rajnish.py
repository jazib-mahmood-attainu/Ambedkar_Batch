number = int(input("Type here any number -> ")) 
sum = 0 
for value in range(1,number): 
    sum = value + sum 
    print(value,end="+") 
print(number)
sum = number+sum
print("Total sum of Natural number =" ,sum) 