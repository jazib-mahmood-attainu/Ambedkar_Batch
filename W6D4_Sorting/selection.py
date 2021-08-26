def sel_sort(A):
    B = []
    for i in range(len(A)):
        min_ele = A[0]
        min_ele_indx = 0
        for indx in range(len(A)):
            if A[indx]<min_ele:
                min_ele = A[indx]
                min_ele_indx = indx

        B.append(A[min_ele_indx])
        A.remove(A[min_ele_indx])

    return B

n = int(input("how many numbers should be there?"))
# A = [int(input("Enter value")) for i in range(n)]
A = list(map(int,input().split()))
#input().split() => ['8','5','6','3','9','8','3','9','1','8']
#map(int,['8','5','6','3','9','8','3','9','1','8'])=> [8,5,6,3,9,8,3,9,1,8]
#list([8,5,6,3,9,8,3,9,1,8])

res = sel_sort(A)
print(res)
