def repetition(sub):
    for i in range(len(sub)):
        if sub[i] in sub[0:i]+sub[i+1:]:
            return True
    return False

def solve(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i,n):
            sub = s[i:j+1] 
            if not repetition(sub):
                max_len = max(max_len,len(sub))
    return max_len

print(solve("APPLE"))
                    

