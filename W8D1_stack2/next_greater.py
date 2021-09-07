def solve(A):
    n = len(A)
    stack = list()

    B = [0]*n

    for idx,val in enumerate(A):
        if len(stack)==0:
            stack.append(idx) #idx=2, val=7
        else:
            cur = val
            while len(stack)!=0 and A[stack[-1]]<cur:
                x = stack.pop()
                B[x] = cur
            stack.append(idx) # 
    
    while len(stack)!=0:
        x = stack.pop()
        B[x] = None

    return B




if __name__=="__main__":
    A = [2,1,7,4]
    print(A)
    print((solve(A)))