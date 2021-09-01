def solve(s):
    hash_table = dict()
    n = len(s)
    max_len = 0
    

    start = 0
    end = 0

    while end<n:
        if s[end] not in hash_table:
            hash_table[s[end]] = end
            cur_len = end-start+1
            max_len = max(max_len,cur_len)
            end += 1

        else:
            while s[end] in hash_table:
                hash_table.pop(s[start])
                start += 1
            hash_table[s[end]] = end
            end += 1
    print(hash_table)
    return max_len

s = "ADOBECODEBANC"
print(solve(s))