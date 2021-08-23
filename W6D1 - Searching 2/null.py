n = int(input())
l = list(map(int,input().split()))
ls = 0

flag = 0
for i in range(n):
    if ls == sum(l[i+1:]):
        print(i)
        flag = 1
        break
    ls = sum(l[0:i])
    rs = sum(l[i+1:])
    if ls == rs:
        flag = 1
        print(i)
        break
if flag == 0:
        print(-1)