def kadane(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    start = 0
    end = 0
    for i in range(1,len(arr)):
        if cur_sum+arr[i]<arr[i]:
            cur_sum = arr[i]
            startc = i
        else:
            cur_sum = cur_sum+arr[i]
            endc = i
        if max_sum<cur_sum:
            max_sum = cur_sum
            start = startc
            end = endc
        else:
            end = endc
        
    print(max_sum,start,end)

A = [-5,2,3,-4,10,-1]
kadane(A)
