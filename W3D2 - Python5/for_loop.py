"""
For loops:

syntax:

to print numbers in a list

for i in [0,1,2,3,4,5]:
<tab>print(i)

or 

for i in range(6):
    print(i)


Q - print table of 5
"""


# for i in range(101):
#     if i%2==0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

a = int(input("Enter a number"))
for i in range(100,-1,-1):
    print("=============")
    for z in range(1,11): #[1.2.3.4.5.6.7,8,9,10]
        print(i,"x",z," = ",i*z)
