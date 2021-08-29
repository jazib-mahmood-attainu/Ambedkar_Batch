n = int(input())

def count(n):
    ctr = 0
    while(n<1):
        if n%2==0:
            n = n//2
            ctr+=1
        else:
            n = 3*n+1
            ctr+=1
    return ctr

print(count(n))