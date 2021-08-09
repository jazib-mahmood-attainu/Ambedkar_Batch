A = list()
A = [4,5,6]
# n = int(input("Enter length of the list"))

# for i in range(n):
#     #something to add into list
#     x = int(input("Enter the number"))
#     A.append(x)

print(A)

A.append("something")

print("After for loop",A)

A.insert(-1,10)

print("After insert", A)
amar = A.pop()
print(amar)

print(A)

ankit = A.pop(2)
print(ankit)

print(A)