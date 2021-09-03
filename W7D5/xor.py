L = [5,4,4,6,6,3,3,8,8,7,7,9,9]

ans = L[0]
for i in range(1,len(L)):
    ans = ans^L[i]

print(ans)