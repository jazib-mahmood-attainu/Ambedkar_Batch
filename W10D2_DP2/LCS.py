dp = [[None for _ in range(1000)] for _ in range(1000)]
def LCS(str1,str2,idx1,idx2):
    if idx1>=len(str1) or idx2>=len(str2):
        return 0
    if dp[idx1][idx2] is not None:
        return dp[idx1][idx2]
    
    if str1[idx1]==str2[idx2]:
        ans =  1+LCS(str1,str2,idx1+1,idx2+1)
    else:
        ans =  max(LCS(str1,str2,idx1+1,idx2),LCS(str1,str2,idx1,idx2+1))
    
    dp[idx1][idx2] = ans
    return dp[idx1][idx2]
ans = LCS("ABCDGH","AEDFHR",0,0)
print(ans)
