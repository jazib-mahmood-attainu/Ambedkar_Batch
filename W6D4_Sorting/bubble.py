def bubble(A):
    n = len(A)
    for i in range(n):
        for j in range(n-1):
            print(A)
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                

    return A
A = [8,5,6,3,9,8,3,9,1,8]
res = bubble(A)
print(res)

