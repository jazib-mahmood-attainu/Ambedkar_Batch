n = int(input())
l = list(map(int,input().split()))
# print(l)

flag = 0

if l[0]<l[1]:
    for i in range(n-1):
        if l[i]<=l[i+1]:
            pass
        else:
            flag = 1
            break
else:
    for i in range(n-1):
        if l[i]>=l[i+1]:
            pass
        else:
            flag = 1
            break
            
if flag == 1:
    print("NO")
else:
    print("YES")