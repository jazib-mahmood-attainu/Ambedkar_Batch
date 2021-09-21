dp = [None]*1000

def solve(start_pos,n):
    if start_pos == n:
        return 1
    if start_pos>n:
        return 0
    if dp[start_pos] is not None:
        return dp[start_pos]
    one_step = solve(start_pos+1,n)
    two_step = solve(start_pos+2,n)
    dp[start_pos] = one_step + two_step
    return dp[start_pos]

if __name__=="__main__":
    ans = solve(0,400)
    print(ans,"no of ways")