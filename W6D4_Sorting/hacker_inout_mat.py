r,c = map(int,input().split())
m = []
for i in range(r):
    row = list(map(int,input().split()))
    m.append(row)
    

print(m)

for i in range(r):
    for j in range(c):
        print(m[i][j],end = " ")
    print()

    