r,c = list(map(int,input().split()))
m = []
for i in range(r):
    row = list(map(int,input().split()))# ""
    m.append(row)

for i in range(c):
    for j in range(r):
        print(m[j][i],end=" ")
    print()

    
#Transpose
# m = [
#     [13,4,8,14,1],
#     [9,6,3,7,21],
#     [5,12,17,9,3]
#     ]
# c = len(m[0])
# r = len(m)



# m2 = []

# for i in range(c):
#     col = []
#     for j in range(r):
#         col.append(m[j][i])
#     m2.append(col)

# print(m2)
