"""
syntax:
if conditions:
<tab>do something
<tab>when above conditions are true
else:
<tab>we'll do something 
<tab>if above conditions are false

Q - divisibility by 4

Q - if weather is sunny and temperature is less than 32, then go to office, else stay at home.

Q - if a student gets more than 90% marks or has won the maths olympiad, then give him admission, else reject the student.

Q - if a number is div by 4, or div by 2 but not by 4.

Q - FizzBuzz, div by 3 - fizz, div by 5 - Fuzz, div by both - fizz-buzz
"""

# a = int(input("Enter value of a: "))
# if a%4==0:
#     print("number is divisible by 4")
# else:
#     print("number not divisible by 4")

# weather = "sunny"
# temperature = 9

# if weather == "sunny" and temperature<32 and temperature>10: 
#     print("go to office") #this runs when condition is true
# else : 
#     print("stay at home") #this runs when condition is false

# marks = 82
# olympiad = "lost"

# if marks>=90 or olympiad=="won":
#     print("Take admission")
# else:
#     print("reject the student")


# a = int(input("Enter value of a: "))

# if a%2==0:
#     n = a%100
#     if n%4==0:
#         print("div by 4 and div by 2")
#     else:
#         print("div by 2 but not by 4")
# else:
#     print("a is not divisible by 2, and not divisible by 4 also")

a = int(input("Enter value of a: "))

if a%3==0 and a%5==0:
    print("FIZZ_BUZZ")
elif a%3==0 :
    print("FIZZ")
elif a%5==0:
    print("FUZZ")
else:
    print("not div by 3 or 5")
    
n = 5 
if(n>3):
    print("greater than 5")
elif(n>4):
    print("greater than 4")