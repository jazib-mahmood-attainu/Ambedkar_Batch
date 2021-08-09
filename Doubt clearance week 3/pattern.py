# n  = int(input("Enter value of n"))

# for i in range(n):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()

A = []
n = int(input("Enter number of elements in the list"))
for i in range(n):
    print("Enter value number",i+1)
    v = int(input())
    
    A.append(v)

print("your list is", A)