import time

# def Fib(n): # n  = 5
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     ans = Fib(n-2,dp)+Fib(n-1,dp) #3 + 2 = 5
#     return ans

def Fib(n,dp): # n  = 5
    if n == 0:
        dp[0] = 0
        return 0
    if n == 1:
        dp[1] = 1
        return 1
    if dp[n]!=None:
        return dp[n]

    ans = Fib(n-2,dp)+Fib(n-1,dp) #3 + 2 = 5
    dp[n] = ans
    return ans


# def Fib_bu(n):
    
#     n_1 = 0
#     n_2 = 1
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     for i in range(2,n+1):
#         c = n_1+n_2
        
#         n_2 = n_1
#         n_1 = c
#     return c
    

if __name__=="__main__":
    print(time.time())
    dp =[None]*1000
    res = Fib(40)
    print(res)
    print(time.time())
    
