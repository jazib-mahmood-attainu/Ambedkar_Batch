n = int(input())
l = list(map(int,input().split()))

mx = max(l[0],l[1]) #6
mx2 = min(l[0],l[1]) #3

for i in range(n):
    if l[i]>mx:
        mx2 = mx
        mx = l[i]
    elif l[i]>mx2 and mx!=l[i]:
        mx2 = l[i]

x = mx
y = 2*mx2
print(x,mx2)
if x > y:
    print("YES")
else:
    print("NO")

