"""
slicing - using some range of values for index

A[start:end:step] - start from index "start", go till "end", but exclude end, and take a step size of "step"

negative index - from right side indices start from -1

A[start:end] - if you ignore start python takes 0,
                if you ignore end, python takes last index



"""
n = int(input("enter a number"))
#    0 1 2 3  4  5 6
A = [2,5,7,8,15,20,30]
print(len(A))

print(A[3])

A[3] = n

print(A[2:5]) # index starting from 2 and ending at 5, excluding 5

print(A[2:6:2]) # index - 2,4

print(A[0:len(A):2])#index - 0 2 4 6

print(A[-1])

print(A[-2])

print(A[0:-2])

print(A[::-1])

print(A[:])

print(A)

