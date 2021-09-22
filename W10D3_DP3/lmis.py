def max_len_subseq(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

arr = [5,1,7,8,2,15,20]
res = max_len_subseq(arr)
print(res)