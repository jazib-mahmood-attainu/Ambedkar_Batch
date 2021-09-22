# #brute force
# A = [2,5,-10,7,8]
# max_sum = float("-inf")
# n = len(A)
# for i in range(n):
#     for j in range(i,n):
#         sum = 0
#         for k in range(i,j+1):
#             sum+=A[k]
#             max_sum = max(max_sum,sum)

# print(max_sum)    


#running_sum

# A = [1,2,3,-2,5]
# max_sum = float("-inf")
# n = len(A)
# r = [A[0]]
# for i in range(1,n):
#     r.append(A[i]+r[i-1])
# print(r)
# for i in range(1,n):
#     for j in range(i,n):
#         sum = r[j]-r[i-1]
#         max_sum = max(max_sum,sum)
# print(max_sum)

def kadane(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    for i in range(1,len(arr)):
        cur_sum = max(cur_sum+arr[i],arr[i])
        max_sum = max(max_sum,cur_sum)
    print(max_sum)

A = [-5,2,3,-4,10]
kadane(A)

