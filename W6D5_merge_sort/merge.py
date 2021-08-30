"""
merge two sorted lists to give a sorted list
"""

def stupid_merge(A,B):
    C = list()
    for x in A:
        C.append(x) #O(n)
    for x in B:
        C.append(x) #O(m)
    print(C)
    C.sort()        #O((n+m)log(n+m))
    print(C)

def merge_two_lists(A,B):
    n = len(A)
    m = len(B)

    p1 = 0
    p2 = 0

    C = list()
    while p1<n and p2<m:
        if A[p1]<B[p2]:
            C.append(A[p1])
            p1 += 1
        else:
            C.append(B[p2])
            p2 += 1 

    print(p1,p2)
    while p2<m:
        C.append(B[p2])
        p2 += 1
    
    while p1<n:
        C.append(A[p1])
        p1 += 1

    return C

def merge(A,start_l,end_l,start_r,end_r):
    p1 = start_l
    p2 = start_r

    C = list()

    while p1<=end_l and p2<=end_r:
        if A[p1]<A[p2]:
            C.append(A[p1])
            p1 += 1
        else:
            C.append(A[p2])
            p2 += 1 

    # print(p1,p2)
    while p2<=end_r:
        C.append(A[p2])
        p2 += 1
    
    while p1<=end_l:
        C.append(A[p1])
        p1 += 1

    idx = 0
    while idx<len(C):
        A[start_l+idx]  = C[idx]
        idx += 1

def merge_sort(A,l,r):
    m = (l+r)//2
    if l==r:
        return
    merge_sort(A,l,m)

    merge_sort(A,m+1,r)
    print(A)

    merge(A,l,m,m+1,r)




if __name__=="__main__":
    A = [1,5,7] #n elements
    B = [2,6,9,14,17,18] #m elements
    # stupid_merge(A,B)

    # res_l = merge_two_lists(A,B)    
    # print(res_l,"result")

    A = [8,5,6,3,9,8,3,9]
    merge_sort(A,0,len(A)-1)
    print(A)


        