"""
Matrix, is a list of lists(of equal size).
Matrix in python:
[    
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


A[2][2] = 9
A[0][1] = 2
A[1][2] = 6
"""
# r = int(input("Enter number of rows"))
r = 3
# c = int(input("Enter number of cols"))
c = 4
mat = [[input("here") for i in range(c)] for i in range(r)]

print(mat)

"""[
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
    ]
"""

for i in range(r):
    for j in range(c):
        print(mat[i][j], end = " ")
    print()

for i in range(c):
    
    print(mat[0][i], end=" ")