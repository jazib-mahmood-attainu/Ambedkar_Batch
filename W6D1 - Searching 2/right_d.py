A = [

        [1,2,3,4],
        [4,5,6,5],
        [7,8,9,6],

    ]
rows = len(A)
col = len(A[0])

sum = 0
for i in range(min(rows,col)):
    sum += A[i][col-i-1]

print(sum)