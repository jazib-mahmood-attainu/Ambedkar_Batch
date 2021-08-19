class Solution:
    def conv_int_to_list(self,n):
        r = list()
        for i in str(n):
            r.append(int(i))
        return r
    
    def plusOne(self, digits):
        
        digits_str =[str(i) for i in digits]
        dig_str = "".join(digits_str)
        if int(dig_str)==0:
            digits[-1] = 1
            return digits
        ans = int(dig_str)+1
        
        return self.conv_int_to_list(ans)
    
    
obj = Solution()
result = obj.plusOne([9,9,9])
print(result)