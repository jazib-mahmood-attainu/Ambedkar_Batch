r,c = list(map(int,input().split()))
m = []
for i in range(r):
    row = list(map(int,input().split()))# ""
    m.append(row)

m2 = []
for i in m:
    m2.append(list(reversed(i)))

for i in range(r):
    for j in range(c):
        if m2[i][j]==0:
            m2[i][j] = 1
        else:
            m2[i][j] = 0

for i in range(r):
    for j in range(c):
        print(m2[i][j],end=" ")
    print()
