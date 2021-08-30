def running_sum(A):
    R = list()
    R.append(A[0])
    for i in range(1,len(A)):
        R.append(R[i-1]+A[i])
    return R

def solve(R,i,j):
    if i == 0:
        return R[j]
    return R[j]-R[i-1]

A = [1,3,-4,0,5,6,1,2]
R = running_sum(A)
print((solve(R,i = 2,j = 5)))
